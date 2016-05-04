# coding: utf-8
'''
Created on 2016年4月28日

@author: likun
'''

from django.core.cache import cache
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

import time, hashlib, string, random, urllib, urllib2, json

from common.utils import debug
from trustwho.settings import WECHAT_APPID, WECHAT_APPSECRET, WECHAT_TOKEN


class JSSdk():
    def __init__(self, openId, url):
        self.appId = WECHAT_APPID
        self.appSecret = WECHAT_APPSECRET

        self.url = self.escape(url)
        self.access_token_api = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}' \
                                .format(self.appId, self.appSecret)

        self.jsapi_ticket_api = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={0}&type=jsapi' \
                                .format(self.__get_access_token())
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': self.__get_jsapi_ticket(),
            'timestamp': self.__create_timestamp(),
            'url': self.url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def __get_jsapi_ticket(self):
        key = 'wecoffee_jsapi_ticket_{0}'.format(self.appId)
        result = cache.get(key)
        if not result:
            res = urllib.urlopen(self.jsapi_ticket_api)
            result = json.loads(res.read())
            cache.set(key, result, 6000)
        return result.get('ticket')

    def __get_access_token(self):
        key = 'wechat_access_token_{0}'.format(self.appId)
        result = cache.get(key)
        if not result:
            res = urllib.urlopen(self.access_token_api)
            result = json.loads(res.read())
            cache.set(key, result, 6000)
        return result.get('access_token')

    def escape(self, url):
        url = urllib.unquote(url.encode('utf-8'))
        urls = url.split('?')
        if urls[1:]:
            domain, pattern = urls[0], urls[1]
            params = []
            for param in pattern.split('&'):
                p = param.split('=')
                if p[1:]:
                    k, v = p[0], p[1]
                    params.append('%s=%s' % (k, urllib.quote(v, '')))
            pattern = '&'.join(params)
            url = '%s?%s' % (domain, pattern)
        return url

    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        self.ret['signature'] = hashlib.sha1(string).hexdigest()
        self.ret['appId'] = self.appId
        return self.ret
    

class WXSdk():
    def __init__(self):
        self.appId = WECHAT_APPID
        self.appSecret = WECHAT_APPSECRET
        self.token = WECHAT_TOKEN
        self.access_token_api = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}' \
                                .format(self.appId, self.appSecret)

        self.post_tmplmsg_api = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}' \
                        .format(self.__get_access_token())

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())


    def __get_access_token(self):
        key = 'wechat_access_token_{0}'.format(self.appId)
        result = cache.get(key)
        if not result:
            res = urllib.urlopen(self.access_token_api)
            result = json.loads(res.read())
            if result.get('access_token'):
                cache.set(key, result, 3600)
        return result.get('access_token')

    def validate(self, data):
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        raw_signature = data.get('signature', '')
        string = ''.join(key for key in sorted([timestamp, nonce, echostr, self.token]))
        signature = hashlib.sha1(string).hexdigest()
        if raw_signature == signature:
            return True
        return False

    def oauth2_redirect_uri(self, url):
        return 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&redirect_uri={1}&response_type=code&scope=snsapi_base&state=123#wechat_redirect'\
                .format(WECHAT_APPID, urllib.quote(url))
                
    def oauth2_token(self, code):
        oauth2_token_api = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={2}&grant_type=authorization_code'\
                        .format(self.appId, self.appSecret, code)
        res = urllib.urlopen(oauth2_token_api)
        result = json.loads(res.read())
        return result

    def menu_create(self, menus):
        buttons = []
        for menu in menus:
            btn = {'name':menu.name, 'type':menu.type, 'key': menu.key, 'url':menu.url, 'media_id':menu.media_id}
            sub_button = []
            for sub_menu in menu.sub_menus:
                sub_btn = {'name':sub_menu.name, 'type':sub_menu.type, 'key': sub_menu.key, 'url':sub_menu.url, 'media_id':sub_menu.media_id}
                sub_button.append(sub_btn)
            if menu.sub_menus:
                btn.update({'sub_button':sub_button})
            buttons.append(btn)
        post_data = {'button':buttons}
        create_menu_api = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}' \
                        .format(self.__get_access_token())
        req = urllib2.Request(create_menu_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(post_data, ensure_ascii=False).encode('utf-8'))
        result = json.loads(response.read())
        return (result.get('errcode'), result.get('errmsg'))

    def menu_delete(self):
        delete_menu_api = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={0}' \
                            .format(self.__get_access_token())
        res = urllib.urlopen(delete_menu_api)
        result = json.loads(res.read())
        return (result.get('errcode'), result.get('errmsg'))

    def user_info(self, openid):
        get_userinfo_api_token = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN'
        res = urllib.urlopen(get_userinfo_api_token.format(self.__get_access_token(), openid))
        result = json.loads(res.read())
        if result.get('subscribe'):
            return (result.get('nickname'), result)
        return ('', result)

    def material_create(self, mta):
        data = {'type': mta.type, 'media':mta.media}
        if mta.type == 'video':
            data.update({'description': json.dumps({'title': mta.title, 'introduction': mta.introduction}, ensure_ascii=False)})

        register_openers()
        datagen, headers = multipart_encode(data)
        create_material_api = 'https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={0}' \
                                .format(self.__get_access_token())
        request = urllib2.Request(create_material_api, datagen, headers)
        result = urllib2.urlopen(request).read()
        print result
        result = json.loads(result)
        if 'errcode' in result.keys():
            return (0, result.get('errcode'), result.get('errmsg'))
        return (1, result.get('media_id'), result.get('url', ''))

    def material_delete(self, mta):
        data = {'media_id': mta.media_id}
        delete_material_api = 'https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={0}' \
                                .format(self.__get_access_token())
        req = urllib2.Request(delete_material_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
        result = json.loads(response.read())
        return (result.get('errcode'), result.get('errmsg'))

    def news_create(self, qs):
        articles = []
        for atl in qs:
            item = {
               "title": atl.title,
               "thumb_media_id": atl.thumb_media_id.media_id,
               "author": atl.author,
               "digest": atl.digest,
               "show_cover_pic": atl.show_cover_pic and 1 or 0,
               "content": atl.content,
               "content_source_url": atl.url
            }
            articles.append(item)
        data = {'articles':articles}
        create_news_api = 'https://api.weixin.qq.com/cgi-bin/material/add_news?access_token={0}' \
                            .format(self.__get_access_token())
        req = urllib2.Request(create_news_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
        result = json.loads(response.read())
        if 'errcode' in result.keys():
            return (result.get('errcode'), result.get('errmsg'))
        return (1, result.get('media_id'))

    def image_create(self, img):
        data = {'media':img.media}
        register_openers()
        datagen, headers = multipart_encode(data)
        create_image_api = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={0}' \
                            .format(self.__get_access_token())
        request = urllib2.Request(create_image_api, datagen, headers)
        result = urllib2.urlopen(request).read()
        result = json.loads(result)
        if 'errcode' in result.keys():
            return (0, '{0}-{1}'.format(result.get('errcode'), result.get('errmsg')))
        return (1, result.get('url'))

    def send(self, uid, msg):
        data = {
            "touser": uid.encode('utf-8'),
            "msgtype": "text",
            "text":{
                "content": msg.encode('utf-8')
            }
        }
        send_msg_api = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={0}' \
                                .format(self.__get_access_token())
        req = urllib2.Request(send_msg_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
        result = json.loads(response.read())
        debug('message-send', result)
        return result

    def post_paysuccess(self, order, domain):
#        OPENTM201285651
        data = {
                "touser":order.openid
                , "template_id":self.adv.pay_success_template_id
                , "url":"http://{0}/product/pay_success/?trade_no={1}".format(domain, order.orderid)
                , "topcolor":"#7B68EE"
                , "data":{
                   "first": {
                       "value":"您好，您的订单已支付成功！\n",
                       "color":"#000000"
                   },
                   "keyword1":{
                       "value":order.product.name,
                       "color":"#000000"
                   },
                   "keyword2": {
                       "value":order.orderid,
                       "color":"#000000"
                   },
                   "keyword3": {
                       "value":"{0}元".format(order.price),
                       "color":"#000000"
                   },
                   "remark":{
                       "value":"\n感谢您的光临~",
                       "color":"#000000"
                   }
                }
            }
        req = urllib2.Request(self.post_tmplmsg_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data))
        result = json.loads(response.read())
        debug('paysuccess-template', result)
        return (result.get('errcode'), result.get('errmsg'))

    def post_refund_success(self, order, domain):
#        OPENTM202723917
        data = {
                "touser":order.openid
                , "template_id":self.adv.refund_success_template_id
                , "url":"http://{0}/product/refund_success/?trade_no={1}".format(domain, order.orderid)
                , "topcolor":"#000000"
                , "data":{
                   "first": {
                       "value":"您好，您购买的{0}已退款成功！\n".format(order.product.name),
                       "color":"#000000"
                   },
                   "keyword1":{
                       "value":order.orderid,
                       "color":"#000000"
                   },
                   "keyword2": {
                       "value":"{0}元".format(order.price),
                       "color":"#000000"
                   },
                   "remark":{
                       "value":"\n感谢您的光临~",
                       "color":"#000000"
                   }
                }
            }
        req = urllib2.Request(self.post_tmplmsg_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data))
        result = json.loads(response.read())
        debug('refund-template', result)
        return (result.get('errcode'), result.get('errmsg'))

    def device_notice(self, openid, number, msg):
#        OPENTM401260554
        data = {
                "touser":openid
                , "template_id":self.adv.device_notice_template_id
                , "url":""
                , "topcolor":"#7B68EE"
                , "data":{
                   "first": {
                       "value":'让您久等啦！\n',
                       "color":"#000000"
                   },
                   "keyword1":{
                       "value":number,
                       "color":"#000000"
                   },
                   "keyword2": {
                       "value":msg,
                       "color":"#000000"
                   },
                   "remark":{
                       "value":"\n感谢您的光临~",
                       "color":"#000000"
                   }
                }
            }
        req = urllib2.Request(self.post_tmplmsg_api)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data))
        result = json.loads(response.read())
        debug('device-notice-template', result)
        code = result.get('errcode')
        if code != 0:
            self.send(openid, msg)
        return (code, result.get('errmsg'))

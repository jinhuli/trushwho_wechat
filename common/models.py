# coding: utf-8
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# #
# # Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# # into your database.
from __future__ import unicode_literals
# 
# from django.db import models
# 
# 
# class ArchiveTable(models.Model):
#     user_id = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     detail = models.CharField(max_length=255, blank=True, null=True)
#     publish_time = models.DateTimeField(blank=True, null=True)
#     repost_count = models.CharField(max_length=255, blank=True, null=True)
#     donate_count = models.CharField(max_length=255, blank=True, null=True)
#     comment_count = models.CharField(max_length=255, blank=True, null=True)
#     device = models.CharField(max_length=255, blank=True, null=True)
#     href = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'archive_table'
# 
# 
# class ArticleGubaEastmoney(models.Model):
#     uuid = models.CharField(primary_key=True, max_length=32)
#     user_id = models.CharField(max_length=64, blank=True, null=True)
#     user_name = models.CharField(max_length=128, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.CharField(max_length=64, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     readed_count = models.IntegerField(blank=True, null=True)
#     comment_count = models.IntegerField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.CharField(max_length=64, blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'article_guba_eastmoney'
# 
# 

# 
# class ArticleShixi(models.Model):
#     object_id = models.TextField(primary_key=True)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     target = models.CharField(max_length=45, blank=True, null=True)
#     status = models.IntegerField()
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     manual_summary = models.TextField(blank=True, null=True)
#     auto_summary = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_shixi'
# 
# 
# class ArticleSinaGuba(models.Model):
#     uuid = models.CharField(primary_key=True, max_length=64)
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     readed_count = models.FloatField(blank=True, null=True)
#     comment_count = models.FloatField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_sina_guba'
# 
# 
# class ArticleSinaZl(models.Model):
#     id = models.IntegerField(primary_key=True)
#     uuid = models.CharField(max_length=64)
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     readed_count = models.FloatField(blank=True, null=True)
#     comment_count = models.FloatField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_sina_zl'
# 
# 
# class ArticleSinaZlCopy(models.Model):
#     uuid = models.CharField(primary_key=True, max_length=64)
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     readed_count = models.FloatField(blank=True, null=True)
#     comment_count = models.FloatField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_sina_zl_copy'
# 
# 
# class ArticleTraining(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     href = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     publish_date = models.DateTimeField(blank=True, null=True)
#     v_id = models.CharField(max_length=36, blank=True, null=True)
#     source_id = models.CharField(max_length=36, blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
#     article_type = models.CharField(max_length=2, blank=True, null=True)
#     article_category = models.IntegerField(blank=True, null=True)
#     is_predictable = models.IntegerField(blank=True, null=True)
#     summary = models.TextField(blank=True, null=True)
#     list_of_object = models.CharField(max_length=36, blank=True, null=True)
#     list_of_v = models.CharField(max_length=255, blank=True, null=True)
#     object_keyword_title = models.CharField(max_length=255, blank=True, null=True)
#     object_keyword_content = models.CharField(max_length=255, blank=True, null=True)
#     other_keyword_title = models.CharField(max_length=255, blank=True, null=True)
#     other_keyword_content = models.CharField(max_length=255, blank=True, null=True)
#     organization_id = models.CharField(max_length=45, blank=True, null=True)
#     article_source = models.CharField(max_length=45, blank=True, null=True)
#     article_uuid = models.CharField(max_length=45, blank=True, null=True)
#     is_correct = models.IntegerField(blank=True, null=True)
#     emotion_level = models.IntegerField(blank=True, null=True)
#     period = models.IntegerField(blank=True, null=True)
#     article_status = models.IntegerField(blank=True, null=True)
#     comment = models.CharField(max_length=45, blank=True, null=True)
#     recommendation = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_training'
# 
# 
# class ArticleWeibo(models.Model):
#     uuid = models.CharField(primary_key=True, max_length=32)
#     user_id = models.CharField(max_length=64, blank=True, null=True)
#     user_name = models.CharField(max_length=128, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.CharField(max_length=64, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     content_original = models.TextField(blank=True, null=True)
#     readed_count = models.IntegerField(blank=True, null=True)
#     comment_count = models.IntegerField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.CharField(max_length=64, blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'article_weibo'
# 
# 
# class ArticleWeixin(models.Model):
#     uuid = models.TextField(blank=True, null=True)
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.TextField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_weixin'
# 
# 
# class ArticleWindBreakingnews(models.Model):
#     object_id = models.CharField(primary_key=True, max_length=36)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_breakingnews'
# 
# 
# class ArticleWindCompanynews(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_companynews'
# 
# 
# class ArticleWindEconomicindicators(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_economicindicators'
# 
# 
# class ArticleWindFinancialnews(models.Model):
#     object_id = models.CharField(primary_key=True, max_length=36)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_financialnews'
# 
# 
# class ArticleWindNews(models.Model):
#     newstype = models.CharField(max_length=12)
#     object_id = models.CharField(max_length=36)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_news'
# 
# 
# class ArticleWindNews2(models.Model):
#     newstype = models.CharField(max_length=12)
#     object_id = models.CharField(max_length=36)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_news2'
# 
# 
# class ArticleWindSrleaderremarks(models.Model):
#     object_id = models.CharField(primary_key=True, max_length=36)
#     publishdate = models.DateTimeField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     source = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     sections = models.TextField(blank=True, null=True)
#     areacodes = models.TextField(blank=True, null=True)
#     windcodes = models.TextField(blank=True, null=True)
#     industrycodes = models.TextField(blank=True, null=True)
#     sectercodes = models.TextField(blank=True, null=True)
#     keywords = models.TextField(blank=True, null=True)
#     opdate = models.DateTimeField(blank=True, null=True)
#     opmode = models.TextField(blank=True, null=True)
#     mktsentiments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_wind_srleaderremarks'
# 
# 
# class ArticleXueqiu(models.Model):
#     user_id = models.CharField(max_length=64, blank=True, null=True)
#     user_name = models.CharField(max_length=128, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     classify = models.CharField(max_length=64, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     readed_count = models.FloatField(blank=True, null=True)
#     comment_count = models.FloatField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     source = models.CharField(max_length=64, blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
#     uuid = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'article_xueqiu'
# 
# 
# class ArticlesModelMiddle(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     bigv_id = models.CharField(max_length=36, blank=True, null=True)
#     article_id = models.CharField(max_length=36, blank=True, null=True)
#     object_id = models.CharField(max_length=36, blank=True, null=True)
#     forecast_direction = models.CharField(max_length=2, blank=True, null=True)
#     forecast_date = models.DateTimeField(blank=True, null=True)
#     forecast_point = models.CharField(max_length=255, blank=True, null=True)
#     forecast_point_from = models.CharField(max_length=255, blank=True, null=True)
#     forecast_point_to = models.CharField(max_length=255, blank=True, null=True)
#     created_by = models.CharField(max_length=36, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     model_type = models.CharField(max_length=2, blank=True, null=True)
#     model_status = models.CharField(max_length=2, blank=True, null=True)
#     relative_object = models.CharField(max_length=36, blank=True, null=True)
#     forecast_text = models.TextField(blank=True, null=True)
#     model_direction = models.CharField(max_length=255, blank=True, null=True)
#     model_for = models.CharField(max_length=2, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'articles_model_middle'
# 
# 
# class Asharestockrating(models.Model):
#     object_id = models.CharField(db_column='OBJECT_ID', primary_key=True, max_length=255)  # Field name made lowercase.
#     s_info_windcode = models.CharField(db_column='S_INFO_WINDCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_institute = models.CharField(db_column='S_EST_INSTITUTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_ratinganalyst = models.CharField(db_column='S_EST_RATINGANALYST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_estnewtime_inst = models.CharField(db_column='S_EST_ESTNEWTIME_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_scorerating_inst = models.CharField(db_column='S_EST_SCORERATING_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_prescorerating_inst = models.CharField(db_column='S_EST_PRESCORERATING_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_lowprice_inst = models.CharField(db_column='S_EST_LOWPRICE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_highprice_inst = models.CharField(db_column='S_EST_HIGHPRICE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_prelowprice_inst = models.CharField(db_column='S_EST_PRELOWPRICE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_prehighprice_inst = models.CharField(db_column='S_EST_PREHIGHPRICE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opdate = models.CharField(db_column='OPDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opmode = models.CharField(db_column='OPMODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ann_dt = models.CharField(db_column='ANN_DT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_rating_inst = models.CharField(db_column='S_EST_RATING_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_prerating_inst = models.CharField(db_column='S_EST_PRERATING_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_report_title = models.CharField(db_column='S_EST_REPORT_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_report_type = models.CharField(db_column='S_EST_REPORT_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_est_ratinganalystid = models.CharField(db_column='S_EST_RATINGANALYSTID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_rating_change = models.CharField(db_column='S_RATING_CHANGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     s_rating_validenddt = models.CharField(db_column='S_RATING_VALIDENDDT', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'asharestockrating'
# 
# 
# class Attachment(models.Model):
#     objid = models.CharField(db_column='OBJID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DOCID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
#     contentsize = models.CharField(db_column='CONTENTSIZE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     digest = models.CharField(db_column='DIGEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     storetype = models.CharField(db_column='STORETYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     storepath = models.CharField(db_column='STOREPATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     convertstatus = models.CharField(db_column='CONVERTSTATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     createtimestamp = models.CharField(db_column='CREATETIMESTAMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatetimestamp = models.CharField(db_column='UPDATETIMESTAMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     clsid = models.CharField(db_column='CLSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sharemode = models.CharField(db_column='SHAREMODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     removetag = models.CharField(db_column='REMOVETAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     filetype = models.CharField(db_column='FILETYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sendflag = models.CharField(db_column='SENDFLAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'attachment'
# 
# 
# class AutherGubaEasymoney(models.Model):
#     user_id = models.CharField(primary_key=True, max_length=64)
#     user_name = models.CharField(max_length=128, blank=True, null=True)
#     fans_count = models.IntegerField(blank=True, null=True)
#     visit_count = models.IntegerField(blank=True, null=True)
#     article_count = models.IntegerField(blank=True, null=True)
#     comment_count = models.IntegerField(blank=True, null=True)
#     scrapy_date = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'auther_guba_easymoney'
# 
# 
# class BaselinkSinaGuba(models.Model):
#     uuid = models.TextField(primary_key=True)
#     title = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     type = models.TextField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#     is_bigv = models.IntegerField(blank=True, null=True)
#     page_view = models.BigIntegerField(blank=True, null=True)
#     reply_cnt = models.BigIntegerField(blank=True, null=True)
#     published_time = models.DateField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'baselink_sina_guba'
# 
# 
# class BigVTable(models.Model):
#     user_id = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     sex = models.CharField(max_length=255, blank=True, null=True)
#     area = models.CharField(max_length=255, blank=True, null=True)
#     stock_count = models.IntegerField(blank=True, null=True)
#     talk_count = models.IntegerField(blank=True, null=True)
#     fans_count = models.IntegerField(blank=True, null=True)
#     big_v_in_fans_count = models.IntegerField(blank=True, null=True)
#     follows_count = models.IntegerField(blank=True, null=True)
#     capacitys = models.CharField(max_length=255, blank=True, null=True)
#     summary = models.CharField(max_length=255, blank=True, null=True)
#     follow_search_time = models.CharField(max_length=255, blank=True, null=True)
#     fans_search_time = models.CharField(max_length=255, blank=True, null=True)
#     update_time = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'big_v_table'
# 
# 
# class BigVsAuth(models.Model):
#     v_id = models.CharField(max_length=36)
#     username = models.CharField(max_length=36)
# 
#     class Meta:
#         managed = False
#         db_table = 'big_vs_auth'
# 
# 
# 
# class BigvsBigvMiddle(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     da_v_type = models.IntegerField(blank=True, null=True)
#     belong_to = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'bigvs_bigv_middle'
# 
# 
# class ChnWords(models.Model):
#     name = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'chn_words'
# 
# 
# class Docgeneral(models.Model):
#     objid = models.CharField(db_column='OBJID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     clsid = models.CharField(db_column='CLSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     doctypeid = models.CharField(db_column='DOCTYPEID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     inputid = models.CharField(db_column='INPUTID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     originalauthor = models.CharField(db_column='ORIGINALAUTHOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     keyword = models.CharField(db_column='KEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     docversion = models.CharField(db_column='DOCVERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     accesscount = models.CharField(db_column='ACCESSCOUNT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     secret = models.CharField(db_column='SECRET', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     importance = models.CharField(db_column='IMPORTANCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attachmentflag = models.CharField(db_column='ATTACHMENTFLAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     commentflag = models.CharField(db_column='COMMENTFLAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sharemode = models.CharField(db_column='SHAREMODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     removetag = models.CharField(db_column='REMOVETAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     createtimestamp = models.CharField(db_column='CREATETIMESTAMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatetimestamp = models.CharField(db_column='UPDATETIMESTAMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mktcode = models.CharField(db_column='MKTCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'docgeneral'
# 
# 
# class Docreport(models.Model):
#     objid = models.CharField(db_column='OBJID', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     stkcode = models.CharField(db_column='STKCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.CharField(db_column='INDUSTRYCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     laststockprice = models.CharField(db_column='LASTSTOCKPRICE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastindustryprice = models.CharField(db_column='LASTINDUSTRYPRICE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastmarketprice = models.CharField(db_column='LASTMARKETPRICE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     isevaluate = models.CharField(db_column='ISEVALUATE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     industryrank = models.CharField(db_column='INDUSTRYRANK', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     industryrankorigin = models.CharField(db_column='INDUSTRYRANKORIGIN', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastindustryrank = models.CharField(db_column='LASTINDUSTRYRANK', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastindustryrankorigin = models.CharField(db_column='LASTINDUSTRYRANKORIGIN', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     investrank = models.CharField(db_column='INVESTRANK', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     investrankorigin = models.CharField(db_column='INVESTRANKORIGIN', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastinvestrank = models.CharField(db_column='LASTINVESTRANK', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     lastinvestrankorigin = models.CharField(db_column='LASTINVESTRANKORIGIN', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     targetprice = models.CharField(db_column='TARGETPRICE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     targetpricehigh = models.CharField(db_column='TARGETPRICEHIGH', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     isestimate = models.CharField(db_column='ISESTIMATE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     yeare = models.CharField(db_column='YEARE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netincomet = models.CharField(db_column='NETINCOMET', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netincomet1 = models.CharField(db_column='NETINCOMET1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netincomet2 = models.CharField(db_column='NETINCOMET2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     opcashflowt = models.CharField(db_column='OPCASHFLOWT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     opcashflowt1 = models.CharField(db_column='OPCASHFLOWT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     opcashflowt2 = models.CharField(db_column='OPCASHFLOWT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalequityt = models.CharField(db_column='TOTALEQUITYT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalequityt1 = models.CharField(db_column='TOTALEQUITYT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalequityt2 = models.CharField(db_column='TOTALEQUITYT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     cashdividentst = models.CharField(db_column='CASHDIVIDENTST', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     cashdividentst1 = models.CharField(db_column='CASHDIVIDENTST1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     cashdividentst2 = models.CharField(db_column='CASHDIVIDENTST2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netdebtt = models.CharField(db_column='NETDEBTT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netdebtt1 = models.CharField(db_column='NETDEBTT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     netdebtt2 = models.CharField(db_column='NETDEBTT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     ebitdat = models.CharField(db_column='EBITDAT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     ebitdat1 = models.CharField(db_column='EBITDAT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     ebitdat2 = models.CharField(db_column='EBITDAT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalsharest = models.CharField(db_column='TOTALSHAREST', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalsharest1 = models.CharField(db_column='TOTALSHAREST1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     totalsharest2 = models.CharField(db_column='TOTALSHAREST2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     salest = models.CharField(db_column='SALEST', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     salest1 = models.CharField(db_column='SALEST1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     salest2 = models.CharField(db_column='SALEST2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopprofitt = models.CharField(db_column='MAINOPPROFITT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopprofitt1 = models.CharField(db_column='MAINOPPROFITT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopprofitt2 = models.CharField(db_column='MAINOPPROFITT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopincomingt = models.CharField(db_column='MAINOPINCOMINGT', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopincomingt1 = models.CharField(db_column='MAINOPINCOMINGT1', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     mainopincomingt2 = models.CharField(db_column='MAINOPINCOMINGT2', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     brokerid = models.CharField(db_column='BROKERID', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     originaltitle = models.CharField(db_column='ORIGINALTITLE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     secondtitle = models.CharField(db_column='SECONDTITLE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     summary = models.TextField(db_column='SUMMARY', blank=True, null=True)  # Field name made lowercase.
#     writetime = models.CharField(db_column='WRITETIME', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     submittime = models.CharField(db_column='SUBMITTIME', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     approvetime = models.CharField(db_column='APPROVETIME', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     archivetime = models.CharField(db_column='ARCHIVETIME', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     approvestatus = models.CharField(db_column='APPROVESTATUS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     createtimestamp = models.CharField(db_column='CREATETIMESTAMP', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     updatetimestamp = models.CharField(db_column='UPDATETIMESTAMP', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     clsid = models.CharField(db_column='CLSID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     sharemode = models.CharField(db_column='SHAREMODE', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     removetag = models.CharField(db_column='REMOVETAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     isfieldsurvey = models.CharField(db_column='ISFIELDSURVEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     ipoprice = models.CharField(db_column='IPOPRICE', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     ipopricehigh = models.CharField(db_column='IPOPRICEHIGH', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     isadjuststkpool = models.CharField(db_column='ISADJUSTSTKPOOL', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     targetstkpool = models.CharField(db_column='TARGETSTKPOOL', max_length=26, blank=True, null=True)  # Field name made lowercase.
#     targetstkpoollevel = models.CharField(db_column='TARGETSTKPOOLLEVEL', max_length=26, blank=True, null=True)  # Field name made lowercase.
#     invest_rank = models.CharField(db_column='INVEST_RANK', max_length=26, blank=True, null=True)  # Field name made lowercase.
#     report_type = models.CharField(db_column='REPORT_TYPE', max_length=26, blank=True, null=True)  # Field name made lowercase.
#     warp_cause = models.CharField(db_column='WARP_CAUSE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     allocate_method = models.CharField(db_column='ALLOCATE_METHOD', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     fund_type = models.CharField(db_column='FUND_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     inquire_price_low = models.CharField(db_column='INQUIRE_PRICE_LOW', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     inquire_price_high = models.CharField(db_column='INQUIRE_PRICE_HIGH', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     future_price_low = models.CharField(db_column='FUTURE_PRICE_LOW', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     future_price_high = models.CharField(db_column='FUTURE_PRICE_HIGH', max_length=126, blank=True, null=True)  # Field name made lowercase.
#     eval_info = models.CharField(db_column='EVAL_INFO', max_length=512, blank=True, null=True)  # Field name made lowercase.
#     start_date = models.CharField(db_column='START_DATE', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     end_date = models.CharField(db_column='END_DATE', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     is_first_time = models.CharField(db_column='IS_FIRST_TIME', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     survey_target = models.CharField(db_column='SURVEY_TARGET', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     visit_place = models.CharField(db_column='VISIT_PLACE', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     style_pool = models.CharField(db_column='STYLE_POOL', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     currentstkpoollevel = models.CharField(db_column='CURRENTSTKPOOLLEVEL', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     current_style_pool = models.CharField(db_column='CURRENT_STYLE_POOL', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     industryprospect = models.CharField(db_column='INDUSTRYPROSPECT', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     businessrank = models.CharField(db_column='BUSINESSRANK', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     valuerank = models.CharField(db_column='VALUERANK', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     manageability = models.CharField(db_column='MANAGEABILITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     opcashability = models.CharField(db_column='OPCASHABILITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     mktcode = models.CharField(db_column='MKTCODE', max_length=25, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'docreport'
# 
# 
# class FansInBigVTable(models.Model):
#     user_id = models.CharField(max_length=255, blank=True, null=True)
#     fans_id = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'fans_in_big_v_table'
# 
# 
# class FinishedIds(models.Model):
#     user_id = models.CharField(max_length=64, blank=True, null=True)
#     finish_date = models.DateTimeField(blank=True, null=True)
#     source = models.CharField(max_length=64, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'finished_ids'
# 
# 
# class GubaEasymoney(models.Model):
#     linkmd5id = models.CharField(primary_key=True, max_length=32)
#     title = models.TextField(blank=True, null=True)
#     auther = models.TextField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     last_updated = models.DateTimeField(blank=True, null=True)
#     read_count = models.IntegerField(blank=True, null=True)
#     comment_count = models.IntegerField(blank=True, null=True)
#     board = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'guba_easymoney'
# 
# 
# class IpProxy(models.Model):
#     ip = models.TextField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
#     port = models.TextField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
#     addr = models.CharField(db_column='Addr', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     anonymous = models.TextField(db_column='Anonymous', blank=True, null=True)  # Field name made lowercase.
#     speed = models.FloatField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
#     source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
#     createtime = models.TextField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
#     updatetime = models.CharField(db_column='UpdateTime', max_length=45, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'ip_proxy'
# 
# 
# class Keywords(models.Model):
#     level1cate = models.TextField(blank=True, null=True)
#     level2cate = models.TextField(blank=True, null=True)
#     level3cate = models.TextField(blank=True, null=True)
#     keyword = models.TextField(blank=True, null=True)
#     synonym = models.TextField(blank=True, null=True)
#     object_min = models.IntegerField(blank=True, null=True)
#     object_max = models.IntegerField(blank=True, null=True)
#     object_unit = models.TextField(blank=True, null=True)
#     range_min = models.IntegerField(blank=True, null=True)
#     range_max = models.IntegerField(blank=True, null=True)
#     update_at = models.TextField(blank=True, null=True)
#     comment = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'keywords'
# 
# 
# class LicaishiViewpointTable(models.Model):
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     publish_time = models.TextField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     watch_count = models.BigIntegerField(blank=True, null=True)
#     repost_count = models.BigIntegerField(blank=True, null=True)
#     donate_count = models.BigIntegerField(blank=True, null=True)
#     comment_count = models.BigIntegerField(blank=True, null=True)
#     device = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'licaishi_viewpoint_table'
# 
# 
# class LogArticlePostedResults(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     article_id = models.CharField(max_length=36)
#     username = models.CharField(max_length=36)
#     ip = models.CharField(max_length=128, blank=True, null=True)
#     browser = models.CharField(max_length=36, blank=True, null=True)
#     update_time = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'log_article_posted_results'
# 
# 
# class ModelPostedResults(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     object_date = models.DateField(blank=True, null=True)
#     keywords = models.CharField(max_length=255, blank=True, null=True)
#     object_type = models.IntegerField(blank=True, null=True)
#     object_status = models.IntegerField(blank=True, null=True)
#     object_unit = models.CharField(max_length=255, blank=True, null=True)
#     object_min = models.FloatField(blank=True, null=True)
#     object_max = models.FloatField(blank=True, null=True)
#     range_min = models.FloatField(blank=True, null=True)
#     range_max = models.FloatField(blank=True, null=True)
#     weight = models.FloatField(blank=True, null=True)
#     comment = models.CharField(max_length=255, blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'model_posted_results'
# 
# 
# class ModelsObjectMiddle(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     keywords = models.CharField(max_length=255, blank=True, null=True)
#     object_type = models.IntegerField(blank=True, null=True)
#     object_status = models.IntegerField(blank=True, null=True)
#     object_unit = models.CharField(max_length=255, blank=True, null=True)
#     object_min = models.FloatField(blank=True, null=True)
#     object_max = models.FloatField(blank=True, null=True)
#     range_min = models.FloatField(blank=True, null=True)
#     range_max = models.FloatField(blank=True, null=True)
#     weight = models.FloatField(blank=True, null=True)
#     comment = models.CharField(max_length=255, blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'models_object_middle'
# 
# 
# class QtDailyquote(models.Model):
#     id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
#     innercode = models.CharField(db_column='InnerCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tradingday = models.CharField(db_column='TradingDay', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prevcloseprice = models.CharField(db_column='PrevClosePrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     openprice = models.CharField(db_column='OpenPrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     highprice = models.CharField(db_column='HighPrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lowprice = models.CharField(db_column='LowPrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     closeprice = models.CharField(db_column='ClosePrice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     turnovervolume = models.CharField(db_column='TurnoverVolume', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     turnovervalue = models.CharField(db_column='TurnoverValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     turnoverdeals = models.CharField(db_column='TurnoverDeals', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     xgrq = models.CharField(db_column='XGRQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jsid = models.CharField(db_column='JSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'qt_dailyquote'
# 
# 
# class RefObjectType(models.Model):
#     object_type = models.IntegerField(primary_key=True)
#     level2cate = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'ref_object_type'
# 
# 
# class RefObjectUnit(models.Model):
#     object_unit = models.IntegerField(primary_key=True)
#     unit = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'ref_object_unit'
# 
# 
# class Secumain(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     innercode = models.IntegerField(db_column='InnerCode')  # Field name made lowercase.
#     companycode = models.IntegerField(db_column='CompanyCode', blank=True, null=True)  # Field name made lowercase.
#     secucode = models.CharField(db_column='SecuCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     chiname = models.CharField(db_column='ChiName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     chinameabbr = models.CharField(db_column='ChiNameAbbr', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     engname = models.CharField(db_column='EngName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     engnameabbr = models.CharField(db_column='EngNameAbbr', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     secuabbr = models.CharField(db_column='SecuAbbr', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     chispelling = models.CharField(db_column='ChiSpelling', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     secumarket = models.IntegerField(db_column='SecuMarket', blank=True, null=True)  # Field name made lowercase.
#     secucategory = models.IntegerField(db_column='SecuCategory', blank=True, null=True)  # Field name made lowercase.
#     listeddate = models.DateTimeField(db_column='ListedDate', blank=True, null=True)  # Field name made lowercase.
#     listedsector = models.IntegerField(db_column='ListedSector', blank=True, null=True)  # Field name made lowercase.
#     listedstate = models.IntegerField(db_column='ListedState', blank=True, null=True)  # Field name made lowercase.
#     xgrq = models.DateTimeField(db_column='XGRQ', blank=True, null=True)  # Field name made lowercase.
#     jsid = models.BigIntegerField(db_column='JSID')  # Field name made lowercase.
#     isin = models.CharField(db_column='ISIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'secumain'
# 
# 
# class SinaFinanceTable(models.Model):
#     classify = models.CharField(max_length=32, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     released_time = models.DateTimeField(blank=True, null=True)
#     url = models.CharField(max_length=1024, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sina_finance_table'
# 
# 
# class SinaFinanceTableNews(models.Model):
#     classify = models.CharField(max_length=32, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     released_time = models.DateTimeField(blank=True, null=True)
#     url = models.CharField(max_length=1024, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sina_finance_table_news'
# 
# 
# class SinaNewsAll(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     classify = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     tags = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sina_news_all'
# 
# 
# class SinaNewsTable(models.Model):
#     classify = models.CharField(max_length=30, blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     released_time = models.DateTimeField(blank=True, null=True)
#     url = models.CharField(max_length=180, blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     tags = models.CharField(max_length=120, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sina_news_table'
# 
# 
# class SinaNewsTableTags(models.Model):
#     classify = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     time = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     tags = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sina_news_table_tags'
# 
# 
# class StockBasicAll(models.Model):
#     code = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     industry = models.TextField(blank=True, null=True)
#     area = models.TextField(blank=True, null=True)
#     timetomarket = models.BigIntegerField(db_column='timeToMarket', blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'stock_basic_all'
# 
# 
# class StockKlineAll(models.Model):
#     code = models.CharField(max_length=12, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     open = models.FloatField(blank=True, null=True)
#     high = models.FloatField(blank=True, null=True)
#     close = models.FloatField(blank=True, null=True)
#     low = models.FloatField(blank=True, null=True)
#     volume = models.FloatField(blank=True, null=True)
#     ma_12 = models.FloatField(blank=True, null=True)
#     ma_40 = models.FloatField(blank=True, null=True)
#     ema_12 = models.FloatField(blank=True, null=True)
#     ema_40 = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'stock_kline_all'
# 
# 
# class Stocks(models.Model):
#     code = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     industry = models.TextField(blank=True, null=True)
#     area = models.TextField(blank=True, null=True)
#     timetomarket = models.BigIntegerField(db_column='timeToMarket', blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'stocks'
# 
# 
# class Target(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=32)
#     keywords = models.TextField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     object_type = models.IntegerField(blank=True, null=True)
#     object_status = models.IntegerField(blank=True, null=True)
#     object_unit = models.CharField(max_length=32, blank=True, null=True)
#     object_min = models.FloatField(blank=True, null=True)
#     object_max = models.FloatField(blank=True, null=True)
#     range_min = models.FloatField(blank=True, null=True)
#     range_max = models.FloatField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     comment = models.TextField(blank=True, null=True)
#     object_category = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'target'
# 
# 
# class UnfinishArcticleTable(models.Model):
#     user_id = models.CharField(max_length=255, blank=True, null=True)
#     fail_time = models.CharField(max_length=255, blank=True, null=True)
#     fail_reason = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'unfinish_arcticle_table'
# 
# 
# class UnfinishBigVTable(models.Model):
#     user_id = models.CharField(max_length=255, blank=True, null=True)
#     fail_time = models.CharField(max_length=255, blank=True, null=True)
#     fail_reason = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'unfinish_big_v_table'
# 
# 
# class UnfinishSinaNewsTimeout(models.Model):
#     index = models.BigIntegerField(blank=True, null=True)
#     site = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     date_occur = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'unfinish_sina_news_timeout'
# 
# 
# class UnfinishSinaNewsTimeoutOld(models.Model):
#     index = models.AutoField()
#     site = models.TextField(blank=True, null=True)
#     date_occur = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'unfinish_sina_news_timeout_old'
# 
# 
# class User(models.Model):
#     username = models.CharField(max_length=200, blank=True, null=True)
#     password = models.CharField(max_length=200, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user'
# 
# 
# class WeiboArticleTable(models.Model):
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     publish_time = models.TextField(blank=True, null=True)
#     repost_count = models.TextField(blank=True, null=True)
#     donate_count = models.TextField(blank=True, null=True)
#     comment_count = models.TextField(blank=True, null=True)
#     repost_reason = models.TextField(blank=True, null=True)
#     is_repost = models.IntegerField(blank=True, null=True)
#     is_top = models.IntegerField(blank=True, null=True)
#     device = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'weibo_article_table'
# 
# 
# class WeixinArticleTable(models.Model):
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     publish_time = models.TextField(blank=True, null=True)
#     capture_time = models.TextField(blank=True, null=True)
#     device = models.TextField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'weixin_article_table'
# 
# 
# class XueqiuArticleTable(models.Model):
#     user_id = models.TextField(blank=True, null=True)
#     user_name = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     detail = models.TextField(blank=True, null=True)
#     publish_time = models.DateTimeField(blank=True, null=True)
#     repost_count = models.TextField(blank=True, null=True)
#     donate_count = models.TextField(blank=True, null=True)
#     comment_count = models.TextField(blank=True, null=True)
#     device = models.TextField(blank=True, null=True)
#     href = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'xueqiu_article_table'

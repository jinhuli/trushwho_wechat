# coding: utf-8
import logging

def debug(token, info, error=False):
    logger = logging.getLogger('trustwho')
    tag = '#' if error else '-'
    logger.info('{0}{1}{2}'.format(tag * 20, token, tag * 20))
    if error:
        logger.error(info)
    else:
        logger.info(info)
    logger.info('{0}{1}{2}'.format(tag * 20, token, tag * 20))

#!/usr/bin.env python

BROKER_URL = 'localhost'
CELERY_TASK_SERIALIZER='json'
# lots of   queues
#CELERY_RESULT_BACKEND = 'amqp'
#CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_EXCHANGE='dnscelerytask'
#CELERY_RESULT_EXCHANGE = 'dnscelery'
CELERY_TIMEZONE = 'Asia/Taipei'
CELERY_ENABLE_UTC = True
CELERY_SEND_EVENTS = True

CELERY_IMPORTS = "indexdns"

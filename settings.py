# -*- coding=utf-8 -*-

# Настройки доступа к очереди, которую будем периодически пуллить
XQUEUE_INTERFACE = {
    'url': 'http://192.168.4.78:18040/xqueue',
    'login': 'lms',
    'password': 'password',
    # 'queue': 'champ_demo',
    'queue': 'test-pull',
}

# Относительные адреса api
XQUEUE_URLS = {
    'login': '/login/',
    'get_len': '/get_queuelen/',
    'get_submission': '/get_submission/',
    'put_result': '/put_result/',
}
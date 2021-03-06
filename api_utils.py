# -*- coding=utf-8 -*-

import requests

from champ_ex import api
from champ_ex import settings


def xqueue_login():
    """
    Создаёт и возвращает авторизованную сессию.

    :return: авторизованная сессия
    """

    # Создаём сессию, поскольку доступ к серверу очередей получается через
    # авторизацию, работать предстоит исключительно с ней.
    session = requests.session()

    (success, message) = api.login(session,
                                   settings.XQUEUE_INTERFACE['login'],
                                   settings.XQUEUE_INTERFACE['password'])

    # Возвращаем авторизованную сессию
    return session

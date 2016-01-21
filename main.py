# -*- coding=utf-8 -*-

from champ_ex import settings, utils, api, api_utils, core
# from champ_ex import utils
# from champ_ex import api

import logging
import requests
import time


log = logging.getLogger(__name__)


def main():

    log.info("Start polling")
    while True:
        queue_len = 0

        # Получаем авторизованную сессию
        session = api_utils.xqueue_login()

        # Получаем количество элементов в очереди на данный момент
        (queue_len_result, queue_len) = api.get_queue_length(
            session,
            settings.XQUEUE_INTERFACE['queue']
        )

        # И все их обрабатываем по очереди, пока можем
        while queue_len_result and queue_len:

            # Получаем очередное решение из очереди
            (submission_result, submission) = api.get_submission(
                session,
                settings.XQUEUE_INTERFACE['queue']
            )

            # Если не удалось получить решение на проверку, заканчиваем
            if not submission_result:
                break

            submission = utils.parse_submission(submission)

            # Оцениваем решение пользователя
            (grade, message) = core.grade(
                submission['student_response'],
                submission['grader_payload']
            )

            pass

        # Закрываем сессию
        session.close()

        # Отдыхаем
        log.info("Empty queue, will now sleep, re-poll in 5s...")
        time.sleep(5)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

# -*- coding=utf-8 -*-


def grade(student_response, grader_payload):
    """
    Пример оценивающей функции. По общему дизайну и философии, единственное, о
    чём она может знать, это что ответил пользователь (без уточнения данных,
    позволяющих его каким-либо образом идентифицировать), а также полезную
    информацию для грэйдера (например, внутренний идентификатор задания в
    рамках оценивающей платформы).

    В качестве примера мы будет проверять, входит ли определённая подсторка в
    пользовательский ответ. Если да -- задание выполнено верно.

    :param student_response: Ответ пользователя (str)
    :param grader_payload: Нагрузка для оценивания (str)
    :return: tuple (оценка, сообщение)
    """

    student_response = student_response.strip()
    grader_payload = grader_payload.strip()

    if grader_payload not in student_response.decode('utf-8'):
        return 0, "Задание выполнено неверно"

    return 1, "Задание выполнено верно"


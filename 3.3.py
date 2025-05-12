from typing import Any, List, Union


def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    """
    Функция обрабатывает аргументы в зависимости от значений параметров `search` и `status`.

    Параметры:
    search (str): Указывает, какую часть аргументов обрабатывать. Возможные значения - "args" или "kwargs".
    status (bool): Флаг, который определяет, как обрабатывать аргументы. Если True, обрабатываются только числа в `args`, если False, все аргументы в `args` преобразуются в строку.
    *args (Any): Неограниченное количество дополнительных позиционных аргументов.
    **kwargs (Any): Неограниченное количество именованных аргументов.

    Возвращаемое значение:
    Union[List[int], str]: Если `search == "args"`, возвращает список целых чисел (если `status == True`), либо строку, которая является конкатенацией всех элементов в `args`. Если `search == "kwargs"`, возвращает строку, содержащую ключи и значения из `kwargs`.

    Исключения:
    ValueError: Если `search` не равен "args" или "kwargs", будет выброшена ошибка.
    """
    result: List[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
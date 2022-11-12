import os
import random



def gen_square_of_the_number():
    """
    Генерация последовательных чисел
    """

    for i in range(0,10000):
        yield i


async def gen_random_number():
    """
    Генерация рандомных чисел в промежутке [0, 100000)
    """

    yield random.randint(0, 100000)


async def get_html():
    """
    Получение html
    """

    with open(os.path.join("templates", "html_example.html"), mode="r", encoding="utf-8") as f:
                html = f.read()
    return html

def gen_random_list():
    """
    Генерация списка рандомных чисел
    """

    numbers = []

    for i in range(0, 6):
        numbers.append(random.randint(0, 10000))

    yield numbers


def gen_str():
    """
    Генерация 3-х буквенного слова
    """

    word = []
    latters = ["a", "b", "c", "d", "e", "f", "g"]

    for i in range(0, 3):
        word.append(random.choice(latters))
    word = ''.join(word)
    yield word
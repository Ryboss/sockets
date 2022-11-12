import os
import time
import logging

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from random import randint
from datetime import datetime

from sensor import gen_square_of_the_number, gen_random_number, get_html, gen_random_list, gen_str


app = FastAPI(title="Техническое задание")

log = logging.getLogger()


@app.get("/random_sum")
async def get_random_sum():
    """
    Получение html для выдачи нынешнего времени на вебе
    """

    with open(os.path.join("templates", "random_number.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/random_sum")
async def ws_random_sum(websocket: WebSocket):
    """
    Получение двух чисел с помощью random вывод их суммы
    """

    await websocket.accept()

    while True:
        try:
            first_number = randint(0, 10000)
            await websocket.send_text(data=f"First number {str(first_number)}")
            log.info(f"Первое число {first_number}")
            time.sleep(0.01)

            second_number = randint(0, 10000)
            await websocket.send_text(data=f"Second number {str(second_number)}")
            log.info(f"Второе число {second_number}")
            time.sleep(0.01)

            await websocket.send_text(data=f"Sum {str(first_number + second_number)}")
            log.info(f"Их сумма {first_number + second_number}")
            time.sleep(0.01)
        
        except Exception as e:
            log.exception(e, exc_info=True)
            await websocket.close()


@app.get("/time_now")
async def get_time_now():
    """
    Получение html для выдачи нынешнего времени на вебе
    """

    with open(os.path.join("templates", "time_now.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/time_now")
async def ws_time_now(websocket: WebSocket):
    """
    Получение нынешнего времени %h%m%s выборка только по секундам и вывод на вебе"""
    await websocket.accept()

    while True:
        try:
            time_now = datetime.utcnow()
            log.info(f"Нынешнее время {time_now}")
            await websocket.send_text(data=f"Time Now {str(time_now.second)}")
            
            time.sleep(1)

        except Exception as e:
            log.exception(e, exc_info=True)
            await websocket.close()


@app.get("/html_example")
async def get_html_example():
    """
    Получение html для выдачи того же str(html) на вебе
    """

    with open(os.path.join("templates", "html_example.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/html_example")
async def ws_html_example(websocket: WebSocket):
    """
    Получение html перевод его в строковый формат и выдача его на вебе
    """

    await websocket.accept()

    while True:
        try:
            html = await get_html()
            await websocket.send_text(data=f"{str(html)}")

            log.info(f"Html отправлена")

        except Exception as e:
            log.exception(e, exc_info=True)
            await websocket.close()


@app.get("/get_square_of_the_number")
async def get_square_of_the_number():
    """
    Получение html для выдачи квадрата генерируемых чисел на вебе
    """

    with open(os.path.join("templates", "get_square_of_the_number.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/get_square_of_the_number")
async def ws_square_number(websocket: WebSocket):
    """
    Возведение генерируемых чисел в квадрат
    """

    await websocket.accept()

    while True:
        try:
            for number in gen_square_of_the_number():
                number = number**2
                await websocket.send_text(data=str(number))

        except Exception as e:
            log.info(e, exc_info=True)
            await websocket.close()
    

@app.get("/max_number")
async def get_max_number():
    """
    Получение html для выдачи квадрата генерируемых чисел на вебе
    """

    with open(os.path.join("templates", "max_number.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/max_number")
async def ws_max_number(websocket: WebSocket):
    """
    Получение max из списка чисел
    """

    await websocket.accept()
    max_number: int = 0

    while True:
        try:
            for number in gen_random_list():
                max_number = max(number)
                print(max_number)
                log.info(f"Максимальное число {max_number} из списка чисел {number}")
            await websocket.send_text(data=str(max_number))

        except Exception as e:
            log.info(e, exc_info=True)
            await websocket.close()


@app.get("/min_number")
async def get_min_number():
    """
    Получение html для выдачи квадрата генерируемых чисел на вебе
    """

    with open(os.path.join("templates", "min_number.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/min_number")
async def ws_min_number(websocket: WebSocket):
    """
    Получение max из списка чисел
    """

    await websocket.accept()
    max_number: int = 0

    while True:
        try:
            for numbers in gen_random_list():
                min_number = min(numbers)
                log.info(f"Минимальное число {min_number} из списка чисел {numbers}")
            await websocket.send_text(data=str(max_number))

        except Exception as e:
            log.info(e, exc_info=True)
            await websocket.close()


@app.get("/random_str")
async def get_random_str():
    """
    Получение html для выдачи квадрата генерируемых чисел на вебе
    """

    with open(os.path.join("templates", "random_str.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/random_str")
async def ws_random_str(websocket: WebSocket):
    """
    Получение max из списка чисел
    """

    await websocket.accept()

    while True:
        try:
            for word in gen_str():
                log.info(f"Полученное слово {word}")
            await websocket.send_text(data=f"Полученное слово {str(word)}")  # type: ignore

        except Exception as e:
            log.info(e, exc_info=True)
            await websocket.close()


@app.get("/recieve_text")
async def get():
    with open(os.path.join("templates", "recieve_text.html"), mode="r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.websocket("/ws/recieve_text")
async def ws_smile(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data} :D")
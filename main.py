import telebot
from random import seed
import requests
from services.functions import generate_pass, roll_dice
from utils.config import API_TOKEN, BOT_USERNAME
from utils.logger import logging as logger
bot = telebot.TeleBot(API_TOKEN)
seed(1)

@bot.message_handler(content_types=['text'])
def test_message(message):
    cid = message.chat.id
    text = message.text.lower()
    logger.info(f'{cid} {text}')

    if text == "/help" or text == "/start" or text == f"/help{BOT_USERNAME}" or text == f"/start{BOT_USERNAME}":
        bot.send_message(cid, 
            """ 👾 Bot programado por @Belenitas99 👾\n
            Listado de funcionalidades:
            - /info
            - /code
            - /password
            - /roll
            - /cat
            """)
        
    elif text == "/info" or text == f"/info{BOT_USERNAME}":
        bot.send_message(cid, 
            """ ℹ️ INFO
            - /info → Ofrece información sobre qué hace cada funcionalidad
            - /code → Devuelve tu código de chat.
            - /password → Genera contrasñas aleatorias. Por defecto genera 16 caracteres, pero usando \"password x\", siendo x un número, para generar contraseñas de longitud x. Por ejemplo, \"password 12\".
            - /roll → Tira un dado y devuelve el resultado. Por defecto tira dados de 20 caras, pero usando \"roll xdy\" puedes lanzar tantos dados (x) de tantas caras (y) como quieras. Por ejemplo, \"roll 4d5\".
            - /cat → Devuelve una imagen aleatoria de un gato
            """)

    elif text == "/code" or text == f"/code{BOT_USERNAME}":
        bot.send_message(cid, f"Código: {cid}")

    elif "/password" in text:
        bot.send_message(cid, generate_pass(text))

    elif "/roll" in text:
        bot.send_message(cid, roll_dice(text))

    elif text == "/cat" or text == f"/cat{BOT_USERNAME}":
        resp = requests.get('https://api.thecatapi.com/v1/images/search')
        bot.send_photo(cid, resp.json()[0]['url'])

    else:
        bot.send_message(cid, "Lo siento, no te he entendido. Utiliza /help para ver los comandos disponibles")
        pass

if __name__ == "__main__":
    logger.info('Bot inicializado!')
    while True:
        try:
            bot.enable_save_next_step_handlers(delay=60)
            bot.polling()

        except KeyboardInterrupt:
            logger.error('Interrumpido por teclado')
            break

        except Exception as e:
            logger.error(f'¡Algo salió mal!\n{e}')
        
        
import requests
from datetime import datetime
import telebot
from auth_data import token


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello, write the 'price' to find out the cost of BTS")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTS Price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "something was wrong"
                )
        else:
            bot.send_message(message.chat.id, "check the command")

    bot.polling()



if __name__ == "__main__":
    telegram_bot(token)
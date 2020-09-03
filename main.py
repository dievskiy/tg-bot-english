from core.message_handler import MessageHandler
import os

token_unsplash = os.getenv('TOKEN_UNSPLASH')
token_telegram = os.getenv('TOKEN_TELEGRAM')
channel = os.getenv('CHANNEL')

if __name__ == '__main__':
    if not token_telegram or not token_unsplash or not channel:
        raise RuntimeError("Token or channel is not specified!")

    MessageHandler(token_unsplash, token_telegram, channel).send_post()

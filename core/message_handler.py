import telebot
import requests
from db.db import session as sess, close_sessions
from core.image_processing import ImageProcessor
import random
from crud.crud_posts import get_random_post
from io import BytesIO
from core.TextProcessor import TextProcessor


class MessageHandler:
    """
    Handles messaging the telegram bot
    """

    def __init__(self, token_unsplash, token_telegram, channel):
        """
        :param token_unsplash: API key for unsplash
        :param token_telegram: token for telegram bot
        :param channel: could be id or name of a channel
        """
        self.channel = channel
        self._tags = ['nature', 'books', 'tower', 'skyscraper', 'landscape', 'building']
        self._random_photo_url = "https://api.unsplash.com/photos/random/?client_id={}&orientation=landscape&query=".format(
            token_unsplash)
        self._image_processor = ImageProcessor()
        self.bot = telebot.TeleBot(token_telegram)

    def _get_photo_url(self):
        """
        get url for unsplash photo with random tag which is defined in tags list
        :return: complete url to get from
        """
        return self._random_photo_url + self._tags[random.randint(0, len(self._tags) - 1)]

    def send_post(self):
        """
        Sends images to the channel
        """
        try:
            db = sess()

            # fetch random regular-sized image url from unsplash
            image_url = requests.get(self._get_photo_url()).json()['urls']['regular']
            post = get_random_post(db)

            image_raw = requests.get(image_url).content
            image = BytesIO(image_raw)
            image_with_text = self._image_processor.process_photo(image, TextProcessor.process_english(post.english),
                                                                  post.russian,
                                                                  TextProcessor.process_example(post.example))
            self.bot.send_photo(self.channel, image_with_text)
        except RuntimeError as e:
            print(e)
        finally:
            close_sessions()

from PIL import Image, ImageFont, ImageDraw

import math
import textwrap
import io


class ImageProcessor():
    """
    Writes text on the image
    """
    def __init__(self):
        self.ENG_WORD_SIZE = 50
        self.ENG_FONT_SIZE = 35
        self.AUTHOR_FONT_SIZE = 35
        self.EXAMPLE_TEXT_BACKGROUND_SIZE = 45
        self.AUTHOR_WORD_SIZE = 55
        self._font_path = "./font/ttf/DejaVuSans.ttf"
        self._BASIC_TEXT_BACKGROUND_SIZE = 60
        self._COLOR_BLACK = 'black'
        self._COLOR_WHITE = 'white'
        self.font_idiom = ImageFont.truetype(self._font_path, self.ENG_WORD_SIZE)
        self.font_translation = ImageFont.truetype(self._font_path, self.ENG_WORD_SIZE)
        self.font_example = ImageFont.truetype(self._font_path, self.AUTHOR_FONT_SIZE)
        self.PADDING_BETWEEN_LINES = 10
        self.MINIMUM_WORDS_MARGIN = 25

    def _add_text_to_draw(self, draw, img, words, font, color_rect, color_text, padding_top=50, back_size=60):
        for line in words:
            w, h = draw.textsize(line, font=font)
            draw.rectangle(
                (((img.width - w) // 2) - 10, padding_top, (-img.width + w) / 2 + img.width + 10,
                 padding_top + back_size),
                fill=color_rect)
            draw.text(((img.width - w) // 2, padding_top), line, font=font, fill=color_text)
            padding_top += h + self.PADDING_BETWEEN_LINES
        return padding_top

    def _draw_text(self, draw, idiom_wrapped, translation_wrapped, example_wrapped, img):

        # add idiom's text
        idiom_height = self._add_text_to_draw(draw, img, idiom_wrapped, self.font_idiom, color_rect=self._COLOR_WHITE,
                                              color_text=self._COLOR_BLACK,
                                              back_size=self._BASIC_TEXT_BACKGROUND_SIZE)

        # add translation text
        translation_height = self._add_text_to_draw(draw, img, translation_wrapped, self.font_translation,
                                                    color_rect=self._COLOR_BLACK,
                                                    color_text=self._COLOR_WHITE,
                                                    back_size=self._BASIC_TEXT_BACKGROUND_SIZE,
                                                    padding_top=idiom_height + img.height // 8)

        show_example = True
        # be sure that example fits to the picture without overriding
        padding_example = img.height - img.height // 4
        if padding_example - translation_height < self.MINIMUM_WORDS_MARGIN:
            if padding_example - translation_height < 0:
                show_example = False
            else:
                padding_example += img.height // 10
                self.AUTHOR_FONT_SIZE = (self.AUTHOR_FONT_SIZE * 8) // 10
                self.EXAMPLE_TEXT_BACKGROUND_SIZE = 40

        # add example text
        if show_example:
            self._add_text_to_draw(draw, img, example_wrapped, self.font_example, color_rect=self._COLOR_WHITE,
                                   color_text=self._COLOR_BLACK,
                                   padding_top=padding_example, back_size=self.EXAMPLE_TEXT_BACKGROUND_SIZE)

        return draw

    def process_photo(self, raw_bytes, idiom, translation, example):
        idiom_wrapped = textwrap.wrap(idiom, width=self.ENG_FONT_SIZE)
        translation_wrapped = textwrap.wrap(translation, width=self.ENG_FONT_SIZE)
        example_wrapped = textwrap.wrap(example, self.AUTHOR_WORD_SIZE)

        img = Image.open(raw_bytes)
        draw = ImageDraw.Draw(img)
        self._draw_text(draw, idiom_wrapped, translation_wrapped, example_wrapped, img)

        # save image to bytes
        image_bytes = io.BytesIO()
        img.save(image_bytes, format=img.format)

        return image_bytes.getvalue()

class TextProcessor:
    @staticmethod
    def process_english(idiom):
        return idiom.replace("\n", "; ")

    @staticmethod
    def process_example(ex):
        return "Example: " + ex.replace('<', '').replace('>', '').replace('??', '?')

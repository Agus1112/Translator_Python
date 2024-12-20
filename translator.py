# Library to translate text.
from translate import Translator


# Main Function.
def main():

    # Languages.
    from_lang='en'
    to_lang='es'

    # English text.
    text_to_translate = "Learning new skills is a great way to improve yourself and achieve your goals."
    
    # Translator instance.
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(text_to_translate)

    print(translation)

# Main function execution.
if __name__ == '__main__':
    main()
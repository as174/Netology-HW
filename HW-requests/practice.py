#Путь к файлу с текстом;
#Путь к файлу с результатом;
#Язык с которого перевести;
#Язык на который перевести (по-умолчанию русский)

import requests

def translate_it(txt):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181203T174752Z.949933b6bd21e319.3735be4a82be1a600f791f625513c1a4ccdb7403'
    
    with open(txt, encoding='utf-8') as f:
        text = f.readlines()
        return(text)
        
    params = {
        'key': key,
        'lang': 'fr-ru',
        'text': text,
    }
       
    response = requests.get(url, params=params, timeout=30).json()
    with open('text-ru.txt', 'w') as f:
        f.write(' '.join(response.get('text', [])))
#    return ' '.join(response.get('text', []))
    
    
if __name__ == '__main__':
    
    translate_it('fr.txt')
    

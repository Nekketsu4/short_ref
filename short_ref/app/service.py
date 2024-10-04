import string
import random

from tld import get_tld


def convert_to_short_url(url):

    """
    Получаем url адрес и
    затем из него генерируем короткий адрес
    """

    get_url = get_tld(url, as_object=True)
    random_word = ''.join(
        (random.choice(string.ascii_letters) for i in range(7))
    )
    converted = (f'{get_url.parsed_url.scheme}://'
                 f'{get_url.parsed_url.netloc}/{random_word}')

    return converted

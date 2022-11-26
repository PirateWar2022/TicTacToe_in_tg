from typing import Final
from os import environ


class Tgtoken:
     TOKEN: Final = environ.get('token' ,'token')

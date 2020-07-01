from helpers import is_not_null, is_email
from datetime import datetime


class Author:
    """Modelo de Autores"""

    __attributes = ('_name', '_email', '_registration_time')

    def __init__(self, name: str, email: str) -> None:
        self.__set_name(name)
        self.__set_email(email)
        self._registration_time = datetime.now()

    def __str__(self) -> str:
        return f'\n---Autor Cadastrado---\nNome: {self.name} - E-mail: {self.email}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, self.name, self.email)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Author):
            return NotImplemented
        return self.email == other.email

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @is_not_null
    def __set_name(self, name: str) -> None:
        self._name = name

    @is_not_null
    @is_email
    def __set_email(self, email: str) -> None:
        self._email = email

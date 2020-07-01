from app.helpers.decorators import is_not_null

from datetime import datetime


class Category:
    """Modelo de Categoria"""

    __attributes = ('_name', '_registration_time')

    def __init__(self, name: str) -> None:
        self.__set_name_category(name)
        self._registration_time = datetime.now()

    def __str__(self) -> str:
        return f'\n---Categoria Cadastrada---\nNome da Categoria: {self.name_category}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r})'.format(class_name, self.name_category)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Category):
            return NotImplemented
        return self.name_category == other.name_category

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @property
    def name_category(self) -> str:
        return self._name

    @is_not_null
    def __set_name_category(self, name: str) -> None:
        self._name = name

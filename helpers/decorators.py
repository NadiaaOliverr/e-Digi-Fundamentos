from validate_email import validate_email


def is_not_null(function):
    """Valida campos em branco: '', se só possuem espaços: '  ' ou None"""

    def wrapper(self, field):
        if not field or field.split() == []:
            raise ValueError('Campo nulo ou em branco. Isso não é permitido.')
        return function(self, field)
    return wrapper


def is_email(function):
    """Valida se o campo digitado é um email"""

    def wrapper(self, email):
        if not validate_email(email):
            raise ValueError('E-mail inválido.')
        return function(self, email)
    return wrapper

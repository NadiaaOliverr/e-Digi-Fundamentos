from validate_email import validate_email as verification_email


def validate_field(function):
    """Valida campos em branco, none ou que só possuem espaços"""

    def wrapper(self, field):
        if not field or field.split() == []:
            raise Exception('Campo nulo ou em branco. Isso não é permitido.')
        return function(self, field)
    return wrapper


def validate_email(function):
    """Valida se o campo digitado é um email"""

    def wrapper(self, email):
        if not verification_email(email):
            raise Exception('E-mail inválido.')
        return function(self, email)
    return wrapper

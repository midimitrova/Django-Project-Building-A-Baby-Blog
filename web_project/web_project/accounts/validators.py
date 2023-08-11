from django.core import exceptions


def validate_only_alphabetical(value):
    first_ch = value[0]
    if not first_ch.isalpha():
        raise exceptions.ValidationError('Your name must start with a letter!')
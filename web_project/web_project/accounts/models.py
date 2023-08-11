from enum import Enum

from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models

from web_project.accounts.validators import validate_only_alphabetical


class ChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'


class BlogUser(auth_models.AbstractUser):
    MIN_FIRST_NAME_LEN = 2
    MAX_FIRST_NAME_LEN = 30
    MIN_LAST_NAME_LEN = 2
    MAX_LAST_NAME_LEN = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LEN),
            validate_only_alphabetical,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LEN),
            validate_only_alphabetical,
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),
        default=Gender.DO_NOT_SHOW.value,

    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None

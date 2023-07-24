from django.core import validators

from django.db import models


class Tag(models.Model):
    MAX_CAPTION_LEN = 20

    caption = models.CharField(
        max_length=MAX_CAPTION_LEN,
    )

    def __str__(self):
        return self.caption


class Author(models.Model):
    MAX_FIRST_NAME_LEN = 100
    MAX_LAST_NAME_LEN = 100

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
    )

    email = models.EmailField(

    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    MAX_TITLE_LEN = 150
    MAX_EXCERPT_LEN = 200
    MAX_IMAGE_NAME_LEN = 100
    MIN_CONTENT_LEN = 10

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    excerpt = models.CharField(
        max_length=MAX_EXCERPT_LEN,
    )

    image_name = models.CharField(
        max_length=MAX_IMAGE_NAME_LEN,
    )

    date = models.DateField(
        auto_now=True,
    )

    slug = models.SlugField(
        unique=True,
        db_index=True,
    )

    content = models.TextField(
        validators=(
            validators.MinLengthValidator(MIN_CONTENT_LEN),
        ),

    )

    author = models.ForeignKey(
        Author,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
    )

    tags = models.ManyToManyField(
        Tag,
    )
from django.contrib.auth import get_user_model
from django.core import validators

from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


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
    MAX_CONTENT_LEN = 1000

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    excerpt = models.CharField(
        max_length=MAX_EXCERPT_LEN,
    )

    image = models.URLField(

        null=False,
        blank=False,


    )

    date = models.DateField(
        # auto_now=True,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        # unique=True,
        # db_index=True,
        null=False,
        blank=True,
        # unique=True,
    )

    content = models.TextField(
        max_length=MAX_CONTENT_LEN,

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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}')

        return super().save(*args, **kwargs)


class Comment(models.Model):
    MAX_USERNAME_LEN = 120
    MAX_TEXT_LEN = 400

    user_name = models.CharField(
        max_length=MAX_USERNAME_LEN,
    )

    user_email = models.EmailField()
    text = models.TextField(
        max_length=MAX_TEXT_LEN,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    #
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.DO_NOTHING,
    # )

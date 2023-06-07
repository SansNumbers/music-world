from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CASCADE, CharField, EmailField


class User(AbstractUser):
    email = EmailField(
        verbose_name='email address',
        max_length=150,
        unique=True,
    )
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)

    reviews = ForeignKey(
        'review.Review',
        on_delete=CASCADE,
        null=True,
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

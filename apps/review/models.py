from django.db.models import Model, TextField, IntegerField, BooleanField, DateField, OneToOneField, CASCADE


class Review(Model):
    review = TextField()
    rating = IntegerField()
    status = BooleanField(default=False)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now_add=True)
    album = OneToOneField(
        'album.Album',
        on_delete=CASCADE,
        null=True
    )

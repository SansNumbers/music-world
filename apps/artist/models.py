from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, JSONField, ForeignKey, CASCADE


class Artist(Model):
    spotify_id = CharField(max_length=32, )
    name = CharField(max_length=32, )
    # photo = array of imageobject
    type = CharField(max_length=32, )
    genres = ArrayField(CharField(max_length=200), blank=True)
    uri = CharField(max_length=64, )
    external_urls = JSONField()
    albums = ForeignKey(
        'album.Album',
        on_delete=CASCADE,
        null=True,
    )

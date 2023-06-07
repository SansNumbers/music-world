from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, JSONField, IntegerField, DateField, ForeignKey, CASCADE


class Album(Model):
    spotify_id = CharField(max_length=32, )
    name = CharField(max_length=64, )
    total_tracks = IntegerField()
    release_date = DateField()
    # cover = array of imageobject
    type = CharField(max_length=32, )
    genres = ArrayField(CharField(max_length=200), blank=True)
    uri = CharField(max_length=64, )
    external_urls = JSONField()
    tracks = ForeignKey(
        'track.Track',
        on_delete=CASCADE,
        null=True,
    )

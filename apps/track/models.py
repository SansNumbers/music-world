from django.db.models import Model, CharField, JSONField


class Track(Model):
    spotify_id = CharField(max_length=32, )
    name = CharField(max_length=32, )
    type = CharField(max_length=32, )
    uri = CharField(max_length=64, )
    external_urls = JSONField()

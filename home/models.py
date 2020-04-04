import os

from django.db import models


class Changelog(models.Model):
    userid = models.IntegerField()
    file = models.FileField(upload_to='changelogs/')

    def filename(self):
        return os.path.basename(self.file.name)


class SoundDef(models.Model):
    userid = models.IntegerField()
    file = models.FileField(upload_to='sound_defs/')

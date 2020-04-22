import os

from django.db import models


def changelog_user_dir(instance, filename):
    return 'changelogs/user_{0}/{1}'.format(instance.username, filename)


def sounddefs_user_dir(instance, filename):
    return 'sound_defs/user_{0}/{1}'.format(instance.username, filename)


class Changelog(models.Model):
    username = models.CharField(max_length=30, unique=True)
    file = models.FileField(upload_to=changelog_user_dir)

    def filename(self):
        return os.path.basename(self.file.name)


class SoundDef(models.Model):
    username = models.CharField(max_length=30, unique=True)
    file = models.FileField(upload_to=sounddefs_user_dir)

    def filename(self):
        return os.path.basename(self.file.name)


class UserKey(models.Model):
    username = models.CharField(max_length=30, unique=True)
    token = models.CharField(max_length=32, unique=True)

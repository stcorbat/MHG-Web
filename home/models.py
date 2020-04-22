import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


def changelog_user_dir(instance, filename):
    return 'changelogs/user_{0}/{1}'.format(instance.username, filename)


def sounddefs_user_dir(instance, filename):
    return 'sound_defs/user_{0}/{1}'.format(instance.username, filename)


class Changelog(models.Model):
    username = models.CharField(max_length=30)
    file = models.FileField(upload_to=changelog_user_dir)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return str(self.username) + ': ' + str(self.file.name)


class SoundDef(models.Model):
    username = models.CharField(max_length=30)
    file = models.FileField(upload_to=sounddefs_user_dir)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return str(self.username) + ': ' + str(self.file.name)


class UserKey(models.Model):
    username = models.CharField(max_length=30, unique=True)
    token = models.CharField(max_length=255, unique=True)


@receiver(post_delete, sender=Changelog)
def changelog_delete(sender, instance, **kwargs):
    if instance.file and os.path.isfile(instance.file.path):
        os.remove(instance.file.path)


@receiver(post_delete, sender=SoundDef)
def sounddef_delete(sender, instance, **kwargs):
    if instance.file and os.path.isfile(instance.file.path):
        os.remove(instance.file.path)

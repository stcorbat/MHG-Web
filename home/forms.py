import os

from django.forms import Form, FileField, ValidationError


class TxtFileField(FileField):
    def validate(self, value):
        super().validate(value)

        file_extension = os.path.splitext(value.name)[1]
        if file_extension != '.txt':
            raise ValidationError(
                'Must be a .txt file!',
                code='invalid'
            )


class JsonFileField(FileField):
    def validate(self, value):
        super().validate(value)

        file_extension = os.path.splitext(value.name)[1]
        if file_extension != '.json':
            raise ValidationError(
                'Must be a .json file!',
                code='invalid'
            )


class ChangelogForm(Form):
    changelog_file_input = TxtFileField()


class SoundDefForm(Form):
    sounddef_file_input = JsonFileField()

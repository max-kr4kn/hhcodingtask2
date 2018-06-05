from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from .validators import clean_and_validate

class GenericModel(models.Model):
    _data = JSONField(null=True, blank=True)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = clean_and_validate(value, settings.SCHEME)

    def __str__(self):
        return '#{}'.format(self.id)

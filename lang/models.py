"""Models language identifier."""

from django.db import models


class Translate(models.Model):
    """Translate text."""
    title = models.CharField(max_length=50, blank=True, verbose_name='Name of translate')
    file_one = models.FileField(upload_to='', blank=True, verbose_name='File from translate')
    file_two = models.FileField(upload_to='', blank=True, verbose_name='File to translate')

    def __str__(self):
        """Text representation of translate."""
        return self.title

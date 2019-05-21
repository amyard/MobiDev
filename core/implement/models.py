from django.db import models
from model_utils.models import TimeStampedModel


class UrlModel(TimeStampedModel):

    full_url = models.URLField(max_length = 255)
    short_url = models.CharField(max_length = 255, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.full_url}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'URL'
        verbose_name_plural = 'URLS'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = '/'.join(self.full_url.split('/')[3:])
        super(UrlModel, self).save(*args, **kwargs)
from django.db import models
from model_utils.models import TimeStampedModel
from core.common.utils import get_short_url

from core.common.utils import crawling

class UrlModel(TimeStampedModel):

    full_url = models.URLField(max_length = 255)
    short_url = models.CharField(max_length = 255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.full_url}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'URL'
        verbose_name_plural = 'URLS'

    def save(self, *args, **kwargs):
        self.short_url = get_short_url(self.full_url)
        self.text = crawling(self.full_url)
        super(UrlModel, self).save(*args, **kwargs)
from django.db import models
from app.service import convert_to_short_url


class URL(models.Model):

    url = models.URLField(
        'Ссылка',
        max_length=200,
        blank=True
    )

    short_url = models.CharField(
        'Короткая ссылка',
        max_length=64,
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        convert = convert_to_short_url(self.url)
        URL.objects.filter(pk=self.pk).update(short_url=convert)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.short_url

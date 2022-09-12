from django.db import models

from staff.models import Department


class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Settings(SingletonBaseModel):
    main = models.ManyToManyField(Department, related_name='main', blank=True, verbose_name='Руководство (подразделения)')
    sidebar = models.ManyToManyField(Department, related_name='sidebar', blank=True, verbose_name='Сайдбар (подразделения)')

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return 'Настройки'

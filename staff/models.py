from django.db import models
from staff.querysets import StaffManager


class Department(models.Model):
    title = models.CharField('Название подразделения', max_length=254)
    numbers = models.JSONField('Номера', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True, verbose_name='Родительское подразделение')
    published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'
        ordering = ('parent__title', 'title')

    def __str__(self):
        return self.title


class PostType(models.Model):
    title = models.CharField('Тип должности', max_length=50)
    priority = models.PositiveIntegerField('Приоритет', default=1000)

    class Meta:
        verbose_name = 'тип должности'
        verbose_name_plural = 'типы должностей'
        ordering = ('-priority',)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('Название должности', max_length=50)
    priority = models.PositiveIntegerField('Приоритет', default=1000)
    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL,
                                  blank=True, null=True, verbose_name='Тип должности')

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'
        ordering = ('-post_type__priority', '-priority',)

    def __str__(self):
        return self.title


class Staff(models.Model):
    lname = models.CharField('Фамилия', max_length=50)
    fname = models.CharField('Имя', max_length=50)
    sname = models.CharField('Отчество', max_length=50, null=True, blank=True)
    number = models.IntegerField('Номер', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,
                             blank=True, null=True, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   blank=True, null=True, verbose_name='Подразделение')
    photo = models.ImageField('Фото', upload_to='staff/images', blank=True)
    priority = models.PositiveIntegerField('Приоритет', default=1000)
    published = models.BooleanField('Опубликовано', default=False)

    objects = StaffManager()

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        ordering = ('lname', 'fname', 'sname')

    @property
    def fullname(self):
        return self._fullname

    def __str__(self):
        return self._fullname


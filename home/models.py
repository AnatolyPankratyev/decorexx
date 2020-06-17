from django.db import models


class Project(models.Model):
    title = models.CharField('Название объекта', max_length=255)
    description = models.CharField('Короткое описание проекта', max_length=255)
    characteristic = models.TextField('Описание')
    picture = models.ImageField(default='default.png', upload_to='projects_img')
    pub_date = models.DateTimeField('Дата добавления')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Photo(models.Model):
    title = models.CharField('Название', max_length=255)
    picture = models.ImageField(default='default.png', upload_to='projects_img_nodis')
    pub_date = models.DateTimeField('Дата добавления')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объектов'
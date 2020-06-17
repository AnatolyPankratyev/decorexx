# Generated by Django 2.2.6 on 2019-10-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('picture', models.ImageField(default='default.png', upload_to='projects_img_nodis')),
                ('pub_date', models.DateTimeField(verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Фото объекта',
                'verbose_name_plural': 'Фото объектов',
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]

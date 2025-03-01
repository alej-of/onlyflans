# Generated by Django 3.2.4 on 2024-07-10 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='flan',
            name='image_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='flan',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='flan',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

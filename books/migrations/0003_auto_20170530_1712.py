# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170529_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-name']},
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='headshot',
            field=models.ImageField(upload_to='author_headshots', blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, default='No Name'),
        ),
        migrations.AddField(
            model_name='author',
            name='salutation',
            field=models.CharField(max_length=10, default='Hello'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]

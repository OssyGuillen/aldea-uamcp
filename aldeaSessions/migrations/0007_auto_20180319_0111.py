# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldeaSessions', '0006_auto_20180319_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='parrafo',
        ),
        migrations.AddField(
            model_name='noticia',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-21 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0010_auto_20200120_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winning_side',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='game',
            field=models.CharField(choices=[(b'Kabaddi', b'Kabaddi'), (b'Volleyball', b'Volleyball'), (b'Gully Cricket', b'Gully Cricket'), (b'Table Tennis', b'Table Tennis'), (b'Football', b'Football'), (b'Cricket', b'Cricket'), (b'Tug Of War', b'Tug Of War'), (b'Lan Gaming', b'Lan Gaming'), (b'Hand Ball', b'Hand Ball'), (b'Kho Kho', b'Kho Kho'), (b'Carrom', b'Carrom'), (b'Chess', b'Chess'), (b'Athletics', b'Athletics'), (b'Basketball', b'Basketball')], default=b'Kabaddi', max_length=15),
        ),
    ]

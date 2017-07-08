# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=30)),
                ('ucode', models.CharField(default=b'', max_length=10)),
                ('uphone', models.CharField(default=b'', max_length=15)),
                ('uman', models.CharField(default=b'', max_length=20)),
                ('uaddress', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]

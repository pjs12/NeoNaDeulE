# Generated by Django 3.1.3 on 2022-04-25 02:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Qna', '0003_auto_20220425_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qna_Posting',
            fields=[
                ('qna_idx', models.AutoField(primary_key=True,
                                             serialize=False)),
                ('title', models.CharField(max_length=255,
                                           null=True)),
                ('body', models.TextField(null=True)),
                ('pic', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('id',
                 models.ForeignKey(db_column='id',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Qna_Posting',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Qna_Chatting',
            fields=[
                ('qna_chatting_index', models.AutoField(primary_key=True,
                                                        serialize=False)),
                ('username', models.CharField(blank=True,
                                              max_length=150)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('chatting', models.TextField(null=True)),
                ('qna_idx',
                 models.ForeignKey(db_column='qna_idx',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='Qna.qna_posting')),
            ],
            options={
                'db_table': 'Qna_Chatting',
                'managed': True,
            },
        ),
    ]

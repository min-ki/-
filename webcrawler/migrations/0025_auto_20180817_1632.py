# Generated by Django 2.0.7 on 2018-08-17 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0024_news_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Notice',
        ),
    ]

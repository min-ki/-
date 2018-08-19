# Generated by Django 2.0.7 on 2018-08-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0021_auto_20180728_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='culture_type',
            field=models.CharField(blank=True, choices=[('언어영역', '언어영역'), ('영어영역', '영어영역'), ('SW영역', 'SW영역'), ('인문소양', '인문소양'), ('창업영역', '창업영역'), ('창의영역', '창의영역'), ('자유선택영역', '자유선택영역')], max_length=25, verbose_name='교양 유형'),
        ),
    ]

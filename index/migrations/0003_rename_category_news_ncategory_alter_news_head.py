# Generated by Django 5.1 on 2024-08-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_news_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='category',
            new_name='ncategory',
        ),
        migrations.AlterField(
            model_name='news',
            name='head',
            field=models.CharField(max_length=128),
        ),
    ]

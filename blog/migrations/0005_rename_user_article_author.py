# Generated by Django 3.2.6 on 2021-08-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='author',
        ),
    ]

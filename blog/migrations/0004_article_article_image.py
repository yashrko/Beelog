# Generated by Django 3.2.6 on 2021-08-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='articleDefault.jpg', upload_to='article_image'),
        ),
    ]
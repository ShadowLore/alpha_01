# Generated by Django 4.1.7 on 2023-04-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_description_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=290, verbose_name='Описание'),
        ),
    ]
# Generated by Django 3.2.16 on 2022-11-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_book_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_book_add_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='add_by',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

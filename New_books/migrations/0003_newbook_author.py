# Generated by Django 3.2.5 on 2021-08-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_books', '0002_newbook_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbook',
            name='Author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
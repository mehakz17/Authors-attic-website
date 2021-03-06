# Generated by Django 3.2.5 on 2021-08-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploads/AboutAuthors')),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Aboutme',
        ),
    ]

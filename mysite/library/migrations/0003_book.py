# Generated by Django 3.0.6 on 2020-05-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Pavadinimas')),
            ],
        ),
    ]

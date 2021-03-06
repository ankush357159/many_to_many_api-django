# Generated by Django 4.0 on 2021-12-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('publisher', models.CharField(max_length=400)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('biography', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('books', models.ManyToManyField(blank=True, related_name='authors', to='authors.Book')),
            ],
        ),
    ]

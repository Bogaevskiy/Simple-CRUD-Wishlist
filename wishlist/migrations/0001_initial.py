# Generated by Django 2.2.3 on 2019-07-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('price', models.CharField(blank=True, max_length=150)),
                ('link', models.URLField(blank=True)),
                ('note', models.TextField(blank=True, max_length=300)),
            ],
        ),
    ]
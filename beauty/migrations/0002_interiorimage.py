# Generated by Django 4.0.5 on 2022-06-21 22:52

import beauty.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteriorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=beauty.models.InteriorImage)),
            ],
        ),
    ]

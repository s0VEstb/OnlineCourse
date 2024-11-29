# Generated by Django 5.1.3 on 2024-11-27 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAndHomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos/')),
                ('homework', models.CharField(max_length=255)),
                ('mounth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='courses.mounth')),
            ],
        ),
    ]

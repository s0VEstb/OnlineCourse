# Generated by Django 5.1.3 on 2024-11-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_classandhomework_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='classandhomework',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
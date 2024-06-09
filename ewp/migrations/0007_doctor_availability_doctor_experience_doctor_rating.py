# Generated by Django 5.0.4 on 2024-05-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewp', '0006_remove_profile_doctor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='availability',
            field=models.CharField(default='Available', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]

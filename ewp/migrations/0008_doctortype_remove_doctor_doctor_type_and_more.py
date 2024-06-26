# Generated by Django 5.0.4 on 2024-06-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewp', '0007_doctor_availability_doctor_experience_doctor_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_type',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_types',
            field=models.ManyToManyField(blank=True, to='ewp.doctortype'),
        ),
    ]

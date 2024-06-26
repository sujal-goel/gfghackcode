# Generated by Django 5.0.4 on 2024-04-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'female')], default='m', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_profile_image',
            field=models.ImageField(blank=True, default='static/user_images/person.svg', upload_to='static/user_images'),
        ),
    ]

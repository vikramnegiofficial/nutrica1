# Generated by Django 4.0.4 on 2022-05-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter a valid email address', max_length=254, unique=True)),
                ('name', models.CharField(help_text='Optional', max_length=30)),
                ('mobile', models.IntegerField(unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('account', models.CharField(choices=[('patient', 'patient'), ('hospital staff', 'hospital staff')], max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=15)),
            ],
        ),
    ]

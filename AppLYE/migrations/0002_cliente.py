# Generated by Django 4.2.4 on 2023-09-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLYE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('producto', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
            ],
        ),
    ]

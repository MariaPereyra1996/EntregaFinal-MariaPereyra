# Generated by Django 4.2.3 on 2023-08-14 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]

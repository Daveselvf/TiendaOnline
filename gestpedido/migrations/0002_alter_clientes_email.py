# Generated by Django 4.1.7 on 2023-07-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestpedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

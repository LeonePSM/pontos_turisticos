# Generated by Django 4.0.5 on 2022-07-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0004_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ManyToManyField(to='enderecos.endereco'),
        ),
    ]
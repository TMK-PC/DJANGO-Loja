# Generated by Django 5.0.6 on 2024-06-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0005_itens_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]

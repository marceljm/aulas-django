# Generated by Django 3.0.3 on 2020-02-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aula5', '0003_carrinho_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='preco',
            new_name='valor',
        ),
    ]

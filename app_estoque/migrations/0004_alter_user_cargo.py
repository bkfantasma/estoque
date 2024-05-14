# Generated by Django 5.0.6 on 2024-05-14 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_estoque", "0003_cargo_permissao_alter_cargo_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="cargo",
            field=models.ForeignKey(
                auto_created=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuarios",
                to="app_estoque.cargo",
            ),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_estoque", "0005_alter_user_cargo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cargo",
            name="nome",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="produto",
            name="categoria",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="produto",
            name="nome",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="chave_acesso",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="user",
            name="nome",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="senha",
            field=models.TextField(),
        ),
    ]

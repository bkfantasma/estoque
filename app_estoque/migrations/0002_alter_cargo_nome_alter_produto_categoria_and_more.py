# Generated by Django 5.0.6 on 2024-07-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='nome',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='chave_acesso',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='senha',
            field=models.TextField(),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffs', '0005_cpu_xxxx'),
    ]

    operations = [
        migrations.DeleteModel(
            name='xxxx',
        ),
        migrations.AlterField(
            model_name='cpu',
            name='etc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='series',
            field=models.SmallIntegerField(),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_usermodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]

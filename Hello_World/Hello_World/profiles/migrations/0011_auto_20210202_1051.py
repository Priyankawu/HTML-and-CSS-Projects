# Generated by Django 3.1.5 on 2021-02-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210202_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prefix',
            field=models.CharField(choices=[('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Ms', 'Ms')], default='', max_length=10),
        ),
    ]
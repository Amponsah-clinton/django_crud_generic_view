# Generated by Django 4.1.4 on 2023-02-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0002_alter_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]

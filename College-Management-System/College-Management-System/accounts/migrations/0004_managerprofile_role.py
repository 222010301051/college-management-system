# Generated by Django 4.2.1 on 2023-05-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_managerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerprofile',
            name='role',
            field=models.CharField(default='Manager', max_length=100),
        ),
    ]

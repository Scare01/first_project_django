# Generated by Django 2.0.5 on 2018-05-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wensite', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
    ]

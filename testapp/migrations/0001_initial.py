# Generated by Django 2.2.17 on 2020-12-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_name', models.CharField(max_length=120)),
                ('vchr_address', models.CharField(max_length=200)),
                ('dat_dob', models.DateField()),
                ('vchr_gender', models.CharField(max_length=100)),
                ('vchr_email', models.EmailField(max_length=254)),
                ('vchr_languages', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'table_name',
                'managed': False,
            },
        ),
    ]

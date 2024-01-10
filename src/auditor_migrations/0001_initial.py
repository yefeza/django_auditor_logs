# Generated by Django 2.2.1 on 2023-02-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditarticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_model', models.IntegerField()),
                ('user_metadata', models.TextField(blank=True, null=True)),
                ('request_metadata', models.TextField(blank=True, null=True)),
                ('model_metadata', models.TextField(blank=True, null=True)),
                ('action', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auditauthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_model', models.IntegerField()),
                ('user_metadata', models.TextField(blank=True, null=True)),
                ('request_metadata', models.TextField(blank=True, null=True)),
                ('model_metadata', models.TextField(blank=True, null=True)),
                ('action', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

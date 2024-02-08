# Generated by Django 5.0.1 on 2024-02-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_education_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('button_text', models.CharField(blank=True, default='', max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('name',),
            },
        ),
    ]

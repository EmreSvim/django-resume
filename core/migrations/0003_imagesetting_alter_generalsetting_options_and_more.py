# Generated by Django 5.0.1 on 2024-02-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable pf the image.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254)),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image')),
            ],
        ),
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is variable pf the setting.', max_length=254, verbose_name='Name'),
        ),
    ]
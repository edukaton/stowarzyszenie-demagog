# Generated by Django 2.0.3 on 2018-03-19 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manipulationcategory',
            options={'verbose_name': 'Manipulation Category', 'verbose_name_plural': 'Manipulation Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='topiccategory',
            options={'verbose_name': 'Topic Category', 'verbose_name_plural': 'Topic Categories'},
        ),
    ]
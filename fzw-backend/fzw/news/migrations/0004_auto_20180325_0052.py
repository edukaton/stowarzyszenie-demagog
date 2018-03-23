# Generated by Django 2.0.3 on 2018-03-25 00:52

from django.db import migrations, models
import uuid


def fill_news_uuid(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    News = apps.get_model('news', 'News')
    for obj in News.objects.using(db_alias).all():
        obj.uuid = uuid.uuid4()
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180325_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(fill_news_uuid, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='news',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, unique=True),
        ),
        # this RemoveField operation is irreversible, because in order to
        # recreate it, the primary key constraint on the UUIDField would first
        # have to be dropped.
        migrations.RemoveField('news', 'id'),
        migrations.RenameField(
            model_name='news',
            old_name='uuid',
            new_name='id'
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True),
        ),
    ]
# Generated by Django 2.2 on 2020-08-09 23:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theVault', '0005_auto_20200810_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newnote',
            name='pershkrimi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2, null=True, verbose_name='Content'),
        ),
    ]
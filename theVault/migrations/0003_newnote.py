# Generated by Django 2.2 on 2020-06-03 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theVault', '0002_remove_newpassword_charnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('pershkrimi', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Content')),
                ('koha_posti', models.DateTimeField(default=django.utils.timezone.now)),
                ('vault_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

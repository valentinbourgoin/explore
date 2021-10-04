# Generated by Django 3.2.7 on 2021-09-29 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0004_auto_20210923_1221'),
        ('core', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('last_response', models.JSONField(blank=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_syncs', to='socialaccount.socialapp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_syncs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User sync',
                'unique_together': {('app', 'user')},
            },
        ),
    ]
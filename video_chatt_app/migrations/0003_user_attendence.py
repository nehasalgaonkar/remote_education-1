# Generated by Django 2.0.5 on 2020-07-05 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_chatt_app', '0002_userrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_chatt_app.UserMeeting')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

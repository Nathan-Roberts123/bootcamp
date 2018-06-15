# Generated by Django 2.0.3 on 2018-03-28 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=210, null=True)),
                ('verb', models.CharField(choices=[('L', 'Liked'), ('C', 'Commented'), ('F', 'Favorited'), ('A', 'Answered'), ('W', 'Accepted'), ('E', 'Edited'), ('K', 'Also commented'), ('I', 'Logged In'), ('O', 'Logged Out'), ('U', 'Up voted'), ('S', 'Shared')], max_length=1)),
                ('action_object_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('target_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action_object', to='contenttypes.ContentType')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
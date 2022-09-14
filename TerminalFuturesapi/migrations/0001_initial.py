# Generated by Django 4.1.1 on 2022-09-14 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('sceneText', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='SceneLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('challengeText', models.CharField(max_length=550)),
                ('challengeAnswer', models.CharField(max_length=100)),
                ('failScene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FailScene', to='TerminalFuturesapi.scene')),
                ('nextScene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NextScene', to='TerminalFuturesapi.scene')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SceneLinks', to='TerminalFuturesapi.scene')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('startScene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stories', to='TerminalFuturesapi.scene')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserScene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField()),
                ('sceneLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userScene', to='TerminalFuturesapi.scenelink')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoryTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TerminalFuturesapi.story')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TerminalFuturesapi.tag')),
            ],
        ),
        migrations.AddField(
            model_name='scene',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TerminalFuturesapi.story'),
        ),
    ]

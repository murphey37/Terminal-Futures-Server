# Generated by Django 4.1.1 on 2022-09-21 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TerminalFuturesapi', '0002_alter_scenelink_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='startScene',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Stories', to='TerminalFuturesapi.scene'),
        ),
    ]

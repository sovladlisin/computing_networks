# Generated by Django 3.0.3 on 2020-11-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='markup_person',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='markup_person_person', to='backend.Person'),
        ),
        migrations.AddField(
            model_name='markup_system',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='markup_system', to='backend.System'),
        ),
        migrations.AlterField(
            model_name='markup_person',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='markup_person_list', to='backend.List'),
        ),
    ]
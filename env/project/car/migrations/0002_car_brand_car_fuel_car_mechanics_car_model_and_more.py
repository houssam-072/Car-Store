# Generated by Django 4.2.10 on 2024-03-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('gasoline', 'gasoline'), ('deizel', 'deizel')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='mechanics',
            field=models.CharField(choices=[('New', 'New'), ('Perfect', 'Perfect'), ('Good', 'Good'), ('Medium', 'Medium'), ('Bad', 'Bad'), ('So Bad', ' So Bad')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='aircondition',
            field=models.CharField(choices=[('New', 'New'), ('Perfect', 'Perfect'), ('Good', 'Good'), ('Medium', 'Medium'), ('Bad', 'Bad'), ('So Bad', ' So Bad')], max_length=255),
        ),
    ]

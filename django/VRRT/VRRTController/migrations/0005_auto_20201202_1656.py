# Generated by Django 3.1.3 on 2020-12-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRRTController', '0004_auto_20201130_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyinstance',
            name='BPEndValue1',
            field=models.PositiveIntegerField(default=0, help_text='Blood Pressure value1 at the end of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='BPEndValue2',
            field=models.PositiveIntegerField(default=0, help_text='Blood Pressure value2 at the end of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='BPStartValue1',
            field=models.PositiveIntegerField(default=0, help_text='Blood Pressure value1 at the start of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='BPStartValue2',
            field=models.PositiveIntegerField(default=0, help_text='Blood Pressure value2 at the start of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='HeartRateEnd',
            field=models.PositiveIntegerField(default=0, help_text='Heart Rate at the end of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='HeartRateStart',
            field=models.PositiveIntegerField(default=0, help_text='Heart Rate at the start of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='O2SaturationEnd',
            field=models.PositiveIntegerField(default=0, help_text='Oxygen saturation level at the end of session'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='O2SaturationStart',
            field=models.PositiveIntegerField(default=0, help_text='Oxygen saturation level at start of session'),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='PainScoreEnd',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='PainScoreStart',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

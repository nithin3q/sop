# Generated by Django 4.1 on 2023-09-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effizient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=250)),
                ('age', models.PositiveIntegerField()),
                ('education', models.CharField(choices=[('Grade 12', 'Grade 12'), ('Diploma', 'Diploma'), ('Bachelors Degree', 'Bachelors Degree'), ('Masters Degree', 'Masters Degree'), ('PhD', 'PhD')], max_length=250)),
                ('institute_of_highest', models.CharField(max_length=250)),
                ('course_of_study', models.CharField(max_length=250)),
                ('work_experience', models.TextField()),
                ('institute_canada', models.CharField(max_length=250)),
                ('study_in_canada', models.CharField(max_length=250)),
                ('country_applying_from', models.CharField(max_length=250)),
                ('future_goals', models.CharField(max_length=250)),
                ('english_scores_listening', models.CharField(max_length=250)),
                ('english_scores_reading', models.CharField(max_length=250)),
                ('english_scores_speaking', models.CharField(max_length=250)),
                ('english_scores_writing', models.CharField(max_length=250)),
                ('first_year_tuition', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=250)),
                ('tuition_fee', models.CharField(max_length=250)),
                ('GIC', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=250)),
                ('cost_of_gic', models.CharField(max_length=250)),
            ],
        ),
    ]

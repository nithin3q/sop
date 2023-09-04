from django.db import models

# Create your models here.

class Effizient(models.Model):
    EDUCATION = (
        ('Grade 12', 'Grade 12'),
        ('Diploma', 'Diploma'),
        ('Bachelors Degree', 'Bachelors Degree'),
        ('Masters Degree', 'Masters Degree'),
        ('PhD', 'PhD')
    )

    OPTIONS = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    email = models.EmailField(max_length=254)
    full_name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=250, choices=EDUCATION)
    institute_of_highest = models.CharField(max_length=250)
    course_of_study = models.CharField(max_length=250)
    work_experience = models.TextField()
    institute_canada = models.CharField(max_length=250)
    study_in_canada = models.CharField(max_length=250)
    country_applying_from = models.CharField(max_length=250)
    future_goals = models.CharField(max_length=250)
    english_scores_listening = models.CharField(max_length=250)
    english_scores_reading = models.CharField(max_length=250)
    english_scores_speaking = models.CharField(max_length=250)
    english_scores_writing = models.CharField(max_length=250)
    first_year_tuition =models.CharField(max_length=250, choices=OPTIONS)
    tuition_fee = models.CharField(max_length=250)
    GIC = models.CharField(max_length=250, choices = OPTIONS)
    cost_of_gic = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.full_name} | {self.email}"
    

from django import forms
from .models import Effizient

class EffizientForm(forms.ModelForm):
    
    class Meta:
        model = Effizient
        fields = ('email', 'full_name', 'age', 'education', 'institute_of_highest', 'course_of_study',
                  'work_experience', 'institute_canada', 'study_in_canada', 'country_applying_from',
                  'future_goals', 'english_scores_listening', 'english_scores_reading','english_scores_speaking',
                  'english_scores_writing','first_year_tuition', 'tuition_fee', 'GIC', 'cost_of_gic')
        
        
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'age': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'education': forms.Select(attrs={'class':'form-control'}),
            'institute_of_highest': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'course_of_study': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'work_experience': forms.Textarea(attrs={'class':'form-control', 'rows':'2', 'placeholder':'Your answer'}),
            'institute_canada': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'study_in_canada': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'country_applying_from': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'future_goals': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'english_scores_listening': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'english_scores_reading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'english_scores_speaking': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'english_scores_writing': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'first_year_tuition': forms.Select(attrs={'class':'form-control'}),
            'tuition_fee': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),
            'GIC': forms.Select(attrs={'class':'form-control'}),
            'cost_of_gic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your answer'}),



        }
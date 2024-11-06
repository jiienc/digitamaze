from django import forms
from .models import Student, Teacher, Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'class_enrolled']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'class_assigned']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

from django import forms;
from .models import TaskCategoryModel;

class TaskCategoryForms(forms.ModelForm) :
    class Meta :
        model = TaskCategoryModel;
        fields = "__all__";
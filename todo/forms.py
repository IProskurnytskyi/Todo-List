from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

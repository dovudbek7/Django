from django import forms

from .models import Articles

class AddArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'
        exclude = {'slug', 'author','published','on_top','comments','views'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tag':forms.Select(attrs={'class':'form-select', 'multiple':''}),
            'category':forms.Select(attrs={'class':'form-select','multiple':''}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }
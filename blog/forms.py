from django import forms
from.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'To Email'}))
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Write your Comments'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your Comment'})
            # Add placeholders for other fields as needed
        }


class SearchForm(forms.Form):
    query = forms.CharField()

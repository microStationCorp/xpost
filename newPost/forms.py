from django.contrib.auth.forms import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class newPostForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title')
    post = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20}), label='Post')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'post',
            Submit('submit', 'Upload Post')
        )

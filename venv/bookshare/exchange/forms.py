from django import forms
from .models import Document
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,  Submit, Field,ButtonHolder
from crispy_forms.bootstrap import FormActions

class PostForm(forms.Form):
    bookname=forms.CharField()
    contactnumber = forms.CharField(widget=forms.TextInput(attrs={'type':'number',
                                                             'class': 'form-control',
                                                             'placeholder': '+977984xxxxxxx'}))

    email = forms.EmailField(max_length=64,
                             widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'example@example.com'}),
                             required=True)

    additionalinfo = forms.CharField(max_length=5000,
                                     widget=forms.Textarea(),
                                     help_text='Write your message here!',
                                     required=False)
    Genre = forms.ChoiceField(
        choices=(
            ('option_one', "Novel"),
            ('option_two', "Academic"),
            ('option_three', "Others")
        ),
        widget = forms.RadioSelect,
        initial = 'option_three',
    )
    book_pic = forms.ImageField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('bookname', css_class='input-xlarge'),
        Field('contactnumber', css_class='input-xlarge'),
        Field('price', css_class='input-xlarge'),
        Field('email', css_class='input-xlarge'),
        Field('book_pic'),
        Field('additionalinfo', rows="3", css_class='input-xlarge'),
        'radio_buttons',
    )

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )




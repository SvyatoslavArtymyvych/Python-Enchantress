from django import forms

from apps.newsletters.models import NewsLetter


class NewsLetterModelForm(forms.ModelForm):
    email = forms.EmailField(max_length=35, label='Email')

    class Meta:
        model = NewsLetter
        fields = ('email',)

    def save(self, commit=True):
        subscriber = NewsLetter(email=self.cleaned_data['email'])
        if commit:
            subscriber.save()
        return subscriber

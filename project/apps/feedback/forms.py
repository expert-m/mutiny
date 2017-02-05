from django import forms


class FeedbackForm(forms.Form):
    subject = forms.CharField(
        required=True,
        max_length=100,
    )
    name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        min_length=20,
        max_length=1000,
    )

    def is_spam(self):
        return False

    def clean(self):
        if self.is_spam():
            raise forms.ValidationError('Spam', code='spam')

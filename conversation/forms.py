from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your message...'}))

    class Meta:
        model = ConversationMessage
        fields = ['content']

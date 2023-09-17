from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields= {'MusicTitle', 'ArtistName', 'Country'}
        widgets = {
            'MusicTitle': forms.TextInput(),
            'ArtistName': forms.TextInput(),
            'Country': forms.TextInput(),
        }
        labels = {
            'MusicTitle':'曲名',
            'ArtistName':'アーティスト名',
            'Country':'国'
        }


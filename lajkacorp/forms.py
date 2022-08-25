from django import forms
from django.core.exceptions import ValidationError

from lajkacorp.models import User, MusicAlbum, Distribution, Income, ArtistIncomeSpliter, Storeroom, Message


class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class AddAlbumForm(forms.ModelForm):

    class Meta:
        model = MusicAlbum
        fields = '__all__'


class AddDistroForm(forms.ModelForm):

    class Meta:
        model = Distribution
        fields = '__all__'


class AddIncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = "__all__"


class AddArtistIncomeSpliterForm(forms.ModelForm):

    class Meta:
        model = ArtistIncomeSpliter
        fields = "__all__"


class AddStoreroomForm(forms.ModelForm):

    class Meta:
        model = Storeroom
        fields = "__all__"


class AddMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"


class AddIncomeSpliterForm(forms.ModelForm):

    class Meta:
        model = ArtistIncomeSpliter
        fields = '__all__'


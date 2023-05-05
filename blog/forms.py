from django import forms
from blog.models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = "__all__"

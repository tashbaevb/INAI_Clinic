from django.forms import ModelForm, TextInput
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment_text"]
        widgets = {
            "name": TextInput(
                attrs={"class": "name-control", "placeholder": "Your name"}
            ),
            "comment_text": TextInput(
                attrs={"class": "comment-control", "placeholder": "Your opinion"}
            ),
        }

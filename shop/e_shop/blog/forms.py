from django import forms
from blog import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = "__all__"
        exclude = ["add_time"]
        widgets = {
            "comment_article": forms.HiddenInput(),
            "comment_text": forms.Textarea(
                attrs={
                    "id": "message",
                    "class": "form-control"
                }
            )
        }

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data


        #доделать форму и виджеты и написать волидацию
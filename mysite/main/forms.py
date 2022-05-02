from django import forms


# define attributes and fields in form
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check box, is optional since required is false
    check = forms.BooleanField(required=False)


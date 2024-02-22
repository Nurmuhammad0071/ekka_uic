from django import forms

from product.models import Comment
class ProductForm(forms.ModelForm):
    class Meta:
        model =
        fields = '__all__'
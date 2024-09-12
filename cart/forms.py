from django import forms

PAINTING_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddPaintingForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PAINTING_QUANTITY_CHOICES,
        coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

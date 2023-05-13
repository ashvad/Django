from django import forms
from Book.models import Books
from customer.models import Orders


# class BookForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     amount=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     copies=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         amount=cleaned_data.get("amount")
#         copies=cleaned_data.get("copies")
#         if amount<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if copies<0:
#             msg="inavlid copies"
#             self.add_error("copies",msg)

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})

        }


class OrderEditForm(forms.ModelForm):
    options = (
        ("order_placed", "order_placed"),
        ("dispatch", "dispatch"),
        ("in_transit", "in_transit"),
        ("delivered", "delivered")
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-control"}))

    class Meta:
        model = Orders
        fields = ["expected_delivery_date", "status"]
        widgets = {
            "expected_delivery_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"})
        }

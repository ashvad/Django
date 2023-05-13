from django import forms


class OperationForm(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        num1 = cleaned_data.get("num1")
        num2 = cleaned_data.get("num2")
        if int(num1) < 0:
            msg = ("please provide a valid number")
            self.add_error("num1", msg)
        if int(num2) < 0:
            msg = ("please provide a valid number")
            self.add_error("num2", msg)

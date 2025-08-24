from django import forms

class ApproachForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mobile_no = forms.CharField(
        label="Mobile No",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    therapy_days = forms.ChoiceField(
        choices=[("1", "1 Day"), ("3", "3 Days"), ("7", "7 Days")],
        label="Therapy Days",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    family_count = forms.IntegerField(
        label="Family Count",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )
    time_availability = forms.ChoiceField(
        choices=[("morning", "Morning"), ("afternoon", "Afternoon"), ("evening", "Evening")],
        label="Time Availability",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    current_city = forms.CharField(
        label="Current City",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


# -----------------------
# Contact Form
# -----------------------
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile No'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-Mail'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 4})
    )


# -----------------------
# Payment Form
# -----------------------
PAYMENT_CHOICES = [
    ("card", "Debit/ Credit Card"),
    ("gpay", "Google Pay"),
    ("phonepe", "Phone Pay"),
    ("paytm", "Paytm"),
    ("amazon", "Amazon Pay"),
    ("whatsapp", "WhatsApp"),
]

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )

from django import forms
class ContactForm(forms.Form):
    name= forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    interest = forms.ChoiceField( choices=[
        ("bridal","Bridal Set (Sirbandi / Naugedi)"),
        ("necklaces", "Necklaces & Chains"),
        ("rings", "Rings"),
        ("bangle", "Bangles"),
        ("earrings", "Earrings"),
        ("custom", "Custom Design / Old Gold Exachange"),

    ])
    message = forms.CharField(widget=forms.Textarea)

class FeedbackForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices =[('1','1 Stars'),('2', '2 Stars'),('3','3 Stars')])
    yes_no = forms.ChoiceField(choices =[('yes', 'Yes'), ('no', 'Np')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

class LoginForm(forms.Form):

    username = forms.CharField( widget=forms.TextInput(attrs={"placeholder": "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput( attrs={"placeholder": "••••••••"}))
    signin = forms.BooleanField(required=False)


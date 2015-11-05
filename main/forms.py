from main.models import Cereal, Manufacturer
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions


class CerealForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'


class CerealForm2(forms.Form):
    choices = (('choice1', 'Choice1'), ('choice2', 'Choice2'))

    choices2 = [choice for choice in Manufacturer.objects.all().values_list('pk', 'name')]

    # choices3 = []

    # for choice in Manufacturer.objects.all().values_list('pk', 'name')
    #     print choice
    #     choices3.append(choice)

    name = forms.CharField(max_length=255, label='Name of Cereal')
    manufacturer = forms.ChoiceField(choices=choices2, label='Maker')
    calories = forms.IntegerField(label='Calories')
    protein = forms.IntegerField(label='Protein')
    fat = forms.IntegerField(label='Fat')
    sodium = forms.IntegerField(label='Salt')
    dietary_fiber = forms.FloatField(label='Fiber')
    carbs = forms.FloatField(label='Carbs')
    sugars = forms.IntegerField(label='Sugar')
    display_shelf = forms.IntegerField(label='Display')
    potassium = forms.IntegerField(label='Potassium')
    vitamins_and_minerals = forms.IntegerField(label='Vitamins and Minerals')
    serving_size_weight = forms.FloatField(label='Servings')
    cups_per_serving = forms.FloatField(label='Serving Amount')


# class CerealModelUpdateForm(forms.Form):

#     title = forms.CharField(required=False)

#     info = forms.CharField(required=False, widget=forms.Textarea)

#     image = forms.ImageField(required=False)


# #class UserSignUp(forms.Form):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput(), required=True)

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/concat_view/'
        self.helper.layout = Layout(
                Div('name', 'email', 'phone', css_class='col-md-6'),
                Div('message', css_class='col-md-6')
            )
        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary")
               )
            )



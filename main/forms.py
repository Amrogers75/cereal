from main.models import Cereal, Manufacturer 
from django import forms


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


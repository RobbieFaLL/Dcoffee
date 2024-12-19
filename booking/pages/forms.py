from django import forms
from .models import CoffeeOrder

class CoffeeOrderForm(forms.ModelForm):
    # Coffee Selection (Include all available coffee options)
    coffee = forms.ChoiceField(choices=[
        ('Espresso', 'Espresso'),
        ('Americano', 'Americano'),
        ('Latte', 'Latte'),
        ('Cappuccino', 'Cappuccino'),
        ('Flat White', 'Flat White'),
        ('Macchiato', 'Macchiato'),
        ('Mocha', 'Mocha'),
        ('Hot Chocolate', 'Hot Chocolate'),
    ])
    
    # Espresso Shot Options (Only visible if Espresso is selected)
    shot = forms.ChoiceField(choices=[
        ('Single', 'Single Shot'),
        ('Double', 'Double Shot'),
        ('Triple', 'Triple Shot'),
    ], required=False)
    
    # Milk Selection (Include all available milk options)
    milk = forms.ChoiceField(choices=[
        ('Whole Milk', 'Whole Milk'),
        ('Semi-skimmed Milk', 'Semi-skimmed Milk'),
        ('Skimmed Milk', 'Skimmed Milk'),
        ('Almond Milk', 'Almond Milk'),
        ('Oat Milk', 'Oat Milk'),
        ('Cashew Milk', 'Cashew Milk'),
        ('Soya Milk', 'Soya Milk'),
        ('Goat Milk', 'Goat Milk'),
        ('Yak Milk', 'Yak Milk'),
        ('Nettle Milk', 'Nettle Milk'),
        ('Half and Half', 'Half and Half'),
    ])
    
    # Half and Half Milk Options (Only visible if 'Half and Half' is selected)
    milk_option1 = forms.ChoiceField(choices=[
        ('Whole Milk', 'Whole Milk'),
        ('Semi-skimmed Milk', 'Semi-skimmed Milk'),
        ('Skimmed Milk', 'Skimmed Milk'),
        ('Almond Milk', 'Almond Milk'),
        ('Oat Milk', 'Oat Milk'),
        ('Cashew Milk', 'Cashew Milk'),
        ('Soya Milk', 'Soya Milk'),
        ('Goat Milk', 'Goat Milk'),
        ('Yak Milk', 'Yak Milk'),
        ('Nettle Milk', 'Nettle Milk'),
    ], required=False)
    
    milk_option2 = forms.ChoiceField(choices=[
        ('Whole Milk', 'Whole Milk'),
        ('Semi-skimmed Milk', 'Semi-skimmed Milk'),
        ('Skimmed Milk', 'Skimmed Milk'),
        ('Almond Milk', 'Almond Milk'),
        ('Oat Milk', 'Oat Milk'),
        ('Cashew Milk', 'Cashew Milk'),
        ('Soya Milk', 'Soya Milk'),
        ('Goat Milk', 'Goat Milk'),
        ('Yak Milk', 'Yak Milk'),
        ('Nettle Milk', 'Nettle Milk'),
    ], required=False)
    
    # Flavouring Selection (Max 3 flavours)
    flavours = forms.MultipleChoiceField(choices=[
        ('Vanilla', 'Vanilla'),
        ('Caramel', 'Caramel'),
        ('Hazelnut', 'Hazelnut'),
        ('Chocolate', 'Chocolate'),
        ('Cinnamon', 'Cinnamon'),
        ('Mint', 'Mint'),
        ('Almond', 'Almond'),
    ], widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = CoffeeOrder
        fields = ['coffee', 'shot', 'milk', 'milk_option1', 'milk_option2', 'flavours']
        
    def clean_flavours(self):
        flavours = self.cleaned_data.get('flavours')
        if len(flavours) > 3:
            raise forms.ValidationError("You can select a maximum of 3 flavours.")
        return flavours

from django.db import models

class CoffeeOrder(models.Model):
    # Coffee choices
    COFFEE_CHOICES = [
        ('Espresso', 'Espresso'),
        ('Americano', 'Americano'),
        ('Latte', 'Latte'),
        ('Cappuccino', 'Cappuccino'),
        ('Flat White', 'Flat White'),
        ('Macchiato', 'Macchiato'),
        ('Mocha', 'Mocha'),
        ('Hot Chocolate', 'Hot Chocolate'),
    ]

    # Milk choices
    MILK_CHOICES = [
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
    ]

    # Shot choices for espresso
    SHOT_CHOICES = [
        ('Single', 'Single Shot'),
        ('Double', 'Double Shot'),
        ('Triple', 'Triple Shot'),
    ]

    # Flavouring choices
    FLAVOUR_CHOICES = [
        ('Hazelnut', 'Hazelnut'),
        ('Caramel', 'Caramel'),
        ('Chocolate', 'Chocolate'),
        ('Cinnamon', 'Cinnamon'),
        ('Peppermint', 'Peppermint'),
        ('Vanilla', 'Vanilla'),
        ('Salted Caramel', 'Salted Caramel'),
        ('5 Spice', '5 Spice'),
        ('Truffle', 'Truffle'),
        ('Paprika', 'Paprika'),
        ('Turmeric', 'Turmeric'),
        ("Lion's Mane", "Lion's Mane"),
    ]

    # Model fields
    coffee = models.CharField(max_length=50, choices=COFFEE_CHOICES)
    shot = models.CharField(max_length=50, choices=SHOT_CHOICES, blank=True, null=True)
    milk = models.CharField(max_length=50, choices=MILK_CHOICES)
    milk_option1 = models.CharField(max_length=50, choices=MILK_CHOICES, blank=True, null=True)
    milk_option2 = models.CharField(max_length=50, choices=MILK_CHOICES, blank=True, null=True)
    flavours = models.JSONField(default=list)  # To store up to 3 selected flavours

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This method provides a string representation for each order, including coffee type, milk choice, and selected flavours.
        return f"{self.coffee} - {self.milk} ({', '.join(self.flavours) if self.flavours else 'No Flavours'})"

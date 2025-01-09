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

    # Pastry choices
    PASTRY_CHOICES = [
        ('Croissant', 'Croissant'),
        ('Cinnamon Swirl', 'Cinnamon Swirl'),
        ('Chocolate Chip', 'Chocolate Chip'),
        ('Cinnamon Bun', 'Cinnamon Bun'),
        ('Apple Turnover', 'Apple Turnover'),
        ('Cheese Twist', 'Cheese Twist'),
        ('Raspberry Tart','Raspberry Tart'),
        ('Pain aux raisin','Pain aux raisin')
    ]

    # Model fields
    coffee = models.CharField(max_length=50, choices=COFFEE_CHOICES)
    shot = models.CharField(max_length=50, choices=SHOT_CHOICES, blank=True, null=True)
    milk = models.CharField(max_length=50, choices=MILK_CHOICES)
    milk_option1 = models.CharField(max_length=50, choices=MILK_CHOICES, blank=True, null=True)
    milk_option2 = models.CharField(max_length=50, choices=MILK_CHOICES, blank=True, null=True)
    flavours = models.JSONField(default=list)  # To store up to 3 selected flavours
    pastries = models.JSONField(default=list)  # To store selected pastries

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation for the order
        pastries_display = ', '.join(self.pastries) if self.pastries else 'No Pastries'
        flavours_display = ', '.join(self.flavours) if self.flavours else 'No Flavours'
        return f"{self.coffee} - {self.milk} (Flavours: {flavours_display}, Pastries: {pastries_display})"

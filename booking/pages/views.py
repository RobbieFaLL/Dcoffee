from django.shortcuts import render, get_object_or_404, redirect
from .forms import CoffeeOrderForm
from .models import CoffeeOrder

# Index page view
def index(request):
    return render(request, 'index.html')

# Order form view
def order_view(request):
    if request.method == "POST":
        form = CoffeeOrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the order to the database
            return redirect('success')  # Redirect to a success page or confirmation message
    else:
        form = CoffeeOrderForm()

    return render(request, 'order.html', {'form': form})

# Success page view after an order is placed
def success_view(request):
    coffee_order = CoffeeOrder.objects.last()

    if not coffee_order:
        return render(request, 'success.html', {
            'coffee_order': None,
            'total_price': 0,
            'coffee_price': 0,
            'milk_price': 0,
            'shot_price': 0,
            'flavours_price': 0,
            'pastries_price': 0,
            'all_orders': CoffeeOrder.objects.all(),
        })

    # Predefined prices for items
    prices = {
        'Espresso': 1.50,
        'Americano': 2.00,
        'Latte': 2.50,
        'Cappuccino': 2.50,
        'Flat White': 2.50,
        'Macchiato': 2.00,
        'Mocha': 3.00,
        'Hot Chocolate': 3.00,
        'Milk': 2.00,
        'Syrup': 0.75,
        'Pastry': 1.50,
        'Shot': {'Double': 1.50, 'Triple': 3.00}  # Prices for shot types
    }

    # Calculate prices for coffee, milk, shot, flavours, and pastries
    coffee_price = prices.get(coffee_order.coffee, 0)  # Use the string directly
    milk_price = prices['Milk'] if coffee_order.milk else 0
    shot_price = prices['Shot'].get(coffee_order.shot, 0) if coffee_order.shot else 0
    flavours_price = len(coffee_order.flavours) * prices['Syrup'] if coffee_order.flavours else 0
    pastries_price = len(coffee_order.pastries) * prices['Pastry'] if coffee_order.pastries else 0

    # Calculate total price
    total_price = coffee_price + milk_price + shot_price + flavours_price + pastries_price

    all_orders = CoffeeOrder.objects.all()

    # Pass all necessary information to the template
    return render(request, 'success.html', {
        'coffee_order': coffee_order,
        'total_price': total_price,
        'coffee_price': coffee_price,
        'milk_price': milk_price,
        'shot_price': shot_price,
        'flavours_price': flavours_price,
        'pastries_price': pastries_price,
        'all_orders': all_orders,
    })


# View page for a specific order selected by the user
def view_order(request):
    order_id = request.GET.get('order_select')  # Get the selected order ID
    if order_id:
        coffee_order = get_object_or_404(CoffeeOrder, id=order_id)

        # Predefined prices for items
        prices = {
            'Espresso': 1.50,
            'Americano': 2.00,
            'Latte': 2.50,
            'Cappuccino': 2.50,
            'Flat White': 2.50,
            'Macchiato': 2.00,
            'Mocha': 3.00,
            'Hot Chocolate': 3.00,
            'Milk': 2.00,
            'Syrup': 0.75,
            'Pastry': 1.50,
            'Shot': {'Double': 1.50, 'Triple': 3.00}  # Prices for shot types
        }

        # Calculate prices for coffee, milk, shot, flavours, and pastries
        coffee_price = prices.get(coffee_order.coffee, 0)
        milk_price = prices['Milk'] if coffee_order.milk else 0
        shot_price = prices['Shot'].get(coffee_order.shot, 0) if coffee_order.shot else 0
        flavours_price = len(coffee_order.flavours) * prices['Syrup'] if coffee_order.flavours else 0
        pastries_price = len(coffee_order.pastries) * prices['Pastry'] if coffee_order.pastries else 0

        # Calculate total price
        total_price = coffee_price + milk_price + shot_price + flavours_price + pastries_price

        # Pass prices to the template
        return render(request, 'order_details.html', {
            'coffee_order': coffee_order,
            'coffee_price': coffee_price,
            'milk_price': milk_price,
            'shot_price': shot_price,
            'flavours_price': flavours_price,
            'pastries_price': pastries_price,
            'total_price': total_price,
        })
    else:
        return redirect('index')  # Redirect to home if no order selected
    
def terms_view(request):
    return render(request, 'terms.html')

def privacy_view(request):
    return render(request, 'privacy.html')

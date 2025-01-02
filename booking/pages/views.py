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
    # Get the last order or set to None if no orders exist
    coffee_order = CoffeeOrder.objects.last()
    
    # Handle the case where no orders exist
    if not coffee_order:
        # Pass empty data to the template
        return render(request, 'success.html', {
            'coffee_order': None,
            'total_price': 0,
            'flavours_json': None,
            'all_orders': CoffeeOrder.objects.all(),
        })
    
    # Price calculation logic
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
        'Syrup': 0.75
    }
    
    total_price = prices.get(coffee_order.coffee, 0)
    if coffee_order.shot:
        if coffee_order.shot == 'Double':
            total_price += 0.50
        elif coffee_order.shot == 'Triple':
            total_price += 1.00
    
    if coffee_order.milk == 'Half and Half':
        total_price += prices['Milk'] * 2
    else:
        total_price += prices['Milk']
    
    if coffee_order.flavours:
        total_price += len(coffee_order.flavours) * prices['Syrup']
    
    # Get all previous orders to display in the dropdown
    all_orders = CoffeeOrder.objects.all()

    return render(request, 'success.html', {
        'coffee_order': coffee_order,
        'total_price': total_price,
        'flavours_json': coffee_order.flavours,
        'all_orders': all_orders,  # Pass all previous orders to the template
    })


# View page for a specific order selected by the user
def view_order(request):
    order_id = request.GET.get('order_select')  # Get the selected order ID
    if order_id:
        coffee_order = get_object_or_404(CoffeeOrder, id=order_id)
        return render(request, 'order_details.html', {'coffee_order': coffee_order})  # Render the details of the selected order
    else:
        return redirect('index')  # Redirect to home if no order selected

def terms_view(request):
    return render(request, 'terms.html')

def privacy_view(request):
    return render(request, 'privacy.html')
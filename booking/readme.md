# Coffee Order System

## Project Overview
The Coffee Order System is a Django-based web application that allows users to place coffee orders, view their order details, and calculate the total price of the order based on coffee type, milk choice, shot size, and additional flavours.

---

## Features
1. **Index Page:** The homepage with basic navigation.
2. **Order Form:** A form to place a coffee order with customizable options.
3. **Order Success Page:** Displays details of the last order, calculates the total price, and lists previous orders for selection.
4. **Order Details Page:** Displays detailed information about a selected previous order.
5. **Static Pages:** Includes `Terms of Service` and `Privacy Policy` pages.

---

## Technologies Used
- **Django Framework**: For backend development and template rendering.
- **HTML**: For structure and layout.
- **CSS (if applicable)**: For styling.
- **Python**: For backend logic and price calculation.

---

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- A virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coffee-order-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd coffee-order-system
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at:
   ```
   http://127.0.0.1:8000/
   ```

---

## Usage

### Placing an Order
1. Navigate to the order page.
2. Fill out the coffee order form with options like coffee type, milk type, shot size, and flavours.
3. Submit the form to view the success page with order details and the total price.

### Viewing Previous Orders
1. On the success page, use the dropdown to select a previous order.
2. View detailed information about the selected order.

---

## Project Structure
```
coffee_order_system/
├── coffee_order/       # App for managing coffee orders
│   ├── migrations/     # Database migrations
│   ├── models.py       # Database models for coffee orders
│   ├── forms.py        # Forms for order input
│   ├── views.py        # Views for handling requests
│   ├── templates/      # HTML templates
│       ├── base.html   # Base template
│       ├── index.html  # Home page template
│       ├── order.html  # Order form template
│       ├── success.html # Order success page template
│       ├── order_details.html # Order details template
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---

## Models
### CoffeeOrder
- **Fields:**
  - `coffee`: Type of coffee (e.g., Espresso, Latte).
  - `milk`: Type of milk (e.g., Skimmed, Oat).
  - `shot`: Number of espresso shots (Single, Double, Triple).
  - `flavours`: Optional flavours (e.g., Vanilla, Caramel).
  - `created_at`: Timestamp for when the order was created.

---

## Templates
- **Base Template:** Common structure for all pages.
- **Success Template:** Displays order details and total price.
- **Order Details Template:** Shows details of a selected previous order.

---

## Future Enhancements
- Add user authentication for personalized order history.
- Allow users to edit or delete previous orders.
- Enhance UI with Bootstrap or Tailwind CSS.
- Add API endpoints for mobile app integration.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or feedback, reach out to [your-email@example.com](mailto:your-email@example.com).

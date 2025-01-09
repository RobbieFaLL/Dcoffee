document.addEventListener('DOMContentLoaded', function () {
    // Show or hide espresso and half-and-half options based on selections
    const coffeeSelect = document.getElementById('id_coffee');
    const espressoShots = document.getElementById('espresso-shots');
    const milkSelect = document.getElementById('id_milk');
    const halfAndHalfOptions = document.getElementById('half-and-half-options');

    coffeeSelect.addEventListener('change', () => {
        espressoShots.style.display = coffeeSelect.value === 'Espresso' ? 'block' : 'none';
    });

    milkSelect.addEventListener('change', () => {
        halfAndHalfOptions.style.display = milkSelect.value === 'Half and Half' ? 'block' : 'none';
    });

    // Get the modal and close button elements
    const modal = document.getElementById("flavour-warning-modal");
    const closeModalButton = document.getElementById("close-modal");

    // Restrict flavouring selection to a maximum of 3
    const maxFlavours = 3;

    // Function to update the number of selected flavours
    const updateFlavourLimit = () => {
        const selected = document.querySelectorAll('.flavour-checkbox:checked');
        if (selected.length > maxFlavours) {
            // Show the modal if more than 3 flavours are selected
            modal.style.display = 'block';
            // Uncheck the last selected checkbox if over the limit
            selected[selected.length - 1].checked = false;
        }
    };

    // Add event listener to each flavour checkbox
    const flavourCheckboxes = document.querySelectorAll('.flavour-checkbox');
    flavourCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', updateFlavourLimit);
    });

    // Ensure the limit is applied on page load (in case of pre-selected flavours)
    updateFlavourLimit();

    // Close the modal when the user clicks the close button
    closeModalButton.addEventListener("click", function() {
        modal.style.display = "none";
    });

    // Close the modal if the user clicks anywhere outside of the modal content
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    // Prevent form submission if more than 3 flavours are selected
    const form = document.getElementById('order-form');
    form.addEventListener('submit', (event) => {
        const selectedFlavours = document.querySelectorAll('.flavour-checkbox:checked');
        if (selectedFlavours.length > maxFlavours) {
            // Show the modal if more than 3 flavours are selected
            modal.style.display = 'block';
            event.preventDefault();  // Prevent form submission
        }
    });

    // Adjust price based on item selections
    const priceElement = document.getElementById('total-price'); // Assuming this displays the total price
    const basePrices = {
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
        'Pastry': 1.50, // Assuming each pastry costs £1.50
        'Shot': 1.50 // Each additional shot adds £1.50
    };

    const updatePrice = () => {
        const coffeeType = coffeeSelect.value;
        let totalPrice = basePrices[coffeeType] || 0;

        // Add price for shot if selected
        const shotSelect = document.getElementById('id_shot');
        const shotType = shotSelect ? shotSelect.value : null;
        const shotPrice = shotType === 'Double' ? 1.50 : shotType === 'Triple' ? 3.00 : 0;
        totalPrice += shotPrice;

        // Add price for milk if selected
        const milkType = milkSelect.value;
        if (milkType === 'Half and Half') {
            totalPrice += basePrices['Milk'] * 2;
        } else {
            totalPrice += basePrices['Milk'];
        }

        // Add price for flavours if selected
        const selectedFlavours = document.querySelectorAll('.flavour-checkbox:checked');
        totalPrice += selectedFlavours.length * basePrices['Syrup'];

        // Add price for selected pastries
        const selectedPastries = document.querySelectorAll('.pastry-checkbox:checked');
        totalPrice += selectedPastries.length * basePrices['Pastry'];

        // Update the price element
        priceElement.textContent = `£${totalPrice.toFixed(2)}`;
    };

    // Attach event listeners to form elements
    coffeeSelect.addEventListener('change', updatePrice);
    shotSelect.addEventListener('change', updatePrice);
    milkSelect.addEventListener('change', updatePrice);
    flavourCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', updatePrice);
    });
    const pastryCheckboxes = document.querySelectorAll('.pastry-checkbox');
    pastryCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', updatePrice);
    });

    // Update price on page load in case of pre-selected items
    updatePrice();
});

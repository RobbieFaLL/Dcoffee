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
});
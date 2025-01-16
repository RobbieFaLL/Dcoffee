document.addEventListener('DOMContentLoaded', () => {
    const products = document.querySelectorAll('.product');

    products.forEach(product => {
        product.addEventListener('click', () => {
            // Only toggle on smaller screens
            if (window.innerWidth <= 768) {
                product.classList.toggle('clicked');
            }
        });
    });
});


    // Handles the increment/decrement functionality on the add to cart buttons
    let increment = document.querySelector('.increment-qty');
    increment.addEventListener('click', add);
    let decrement = document.querySelector('.decrement-qty');
    decrement.addEventListener('click', subtract);
    let quantity = document.querySelector('.qty_input');

    function add(e) {
        e.preventDefault();
        if (quantity.valueAsNumber < 10) {
            quantity.valueAsNumber++
        }
    }

    function subtract(e) {
        e.preventDefault();
        if (quantity.valueAsNumber > 1) {
            quantity.valueAsNumber--
        }
    }
// Получаем элемент формы
const form = document.getElementById('order-form');

// Добавляем обработчик события отправки формы
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем перезагрузку страницы

    // Получаем данные из формы
    const currency = form.querySelector('[name="currency"]').value;

    // Получаем строку из страницы
    const totalPrice = document.querySelector('.total-price').innerText;

    // Получить товары
    const dataCart = [];
    const cartItems = document.querySelectorAll('.cart-item')
    cartItems.forEach((item) => {
        const cartItem = {
            id: item.getAttribute('data-id'),
            count: item.querySelector('.items__current').innerText
        }
        dataCart.push(cartItem)
    })

    // Вызываем функцию с данными из формы и строкой
    myFunction(totalPrice, currency, dataCart);
});

function myFunction(totalPrice, currency, dataCart) {
    const res = fetch('https://kharisov.space/olive/api/payment', {
        method: 'POST',
        redirect: 'follow',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        'price': totalPrice,
        'currency': currency,
        'description': 'string',
        'data_cart': dataCart
        })
    })
    .then((response) => response.json())
    .then((data) => {
        window.location.href = data.url;
    })
}
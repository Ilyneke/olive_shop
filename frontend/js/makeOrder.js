// Получаем элемент формы
const form = document.getElementById('order-form');

// Добавляем обработчик события отправки формы
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем перезагрузку страницы

    // Получаем данные из формы
//    const name = form.querySelector('[name="name"]').value;
//    const age = form.querySelector('[name="age"]').value;
//    const terms = form.querySelector('[name="terms"]').checked;
    const currency = form.querySelector('[name="currency"]').value;

    // Получаем строку из страницы
    const totalPrice = document.querySelector('.total-price').innerText;

    // Вызываем функцию с данными из формы и строкой
    myFunction(totalPrice, currency);
});

function myFunction(totalPrice, currency) {
    fetch('https://kharisov.space/olive/api/payment', {
        method: 'POST',
        redirect: 'follow',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        'price': totalPrice,
        'currency': currency,
        'description': 'string'
        })
    });
}
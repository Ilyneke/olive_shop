const productsContainer = document.querySelector('#products-container');

// Запускаем getProducts
getProducts();

// Асинхронная функция получения данных из файла products.json
async function getProducts() {
	// Получаем данные из products.json
    const response = await fetch('https://kharisov.space/olive/api/products', {
      headers: {
        'accept': 'application/json'
      }
    });
    // Парсим данные из JSON формата в JS
    const productsArray = await response.json();
    // Запускаем ф-ю рендера (отображения товаров)
	renderProducts(productsArray);
}

function renderProducts(productsArray) {
    let price = null;
    productsArray.forEach(function (item) {
        if (item.discount === 0) {
            price = `<div class="price__currency">${item.price} $</div>`;
        } else {
            price = `<span class="price__old">${item.price} $</span>
                    <span class="sale-badge">${item.discount}% OFF</span>
                    <div class="price__currency">${item.discounted_price} $</div>`;
        };

        const productHTML = `<div class="col-md-6">
						<div class="card mb-4" data-id="${item.id}">
							<img class="product-img" src="${item.image}" alt="">
							<div class="card-body text-center">
								<h4 class="item-title">${item.name}</h4>
								<p><small data-items-in-box class="text-muted">${item.description}</small></p>

								<div class="details-wrapper">

									<!-- Счетчик -->
									<div class="items counter-wrapper">
										<div class="items__control" data-action="minus">-</div>
										<div class="items__current" data-counter>1</div>
										<div class="items__control" data-action="plus">+</div>
									</div>
									<!-- // Счетчик -->

									<div class="price">${price}</div>
								</div>

								<button data-cart type="button" class="btn btn-block btn-outline-warning">
									+ to cart
								</button>

							</div>
						</div>
					</div>`;
        productsContainer.insertAdjacentHTML('beforeend', productHTML);
    });
}
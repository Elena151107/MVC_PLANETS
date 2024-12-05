document.addEventListener('DOMContentLoaded', ()=> {
fetch('/api/menu')
    .then(response => response.json())
    .then(menu => {
        const menuContainer = document.getElementById('menu');
        menu.forEach(dish => {
            const dishElement = document.createElement('div');
            dishElement.className = 'menu-item';
            dishElement.innerHTML = `<h3>${dish.name}</h3>
                 <p>${dish.description}</p>
                 <p>Price: $${dish.price}</p>
                 <button>Add to Cart</button>`;
            menuContainer.appendChild(dishElement);
        });
    })
    .catch(error => {
    console.error('Failed to load menu', error)
    });
});
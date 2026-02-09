const themeSelector = document.getElementById('themeSelector');
const itemInput = document.getElementById('itemInput');
const addBtn = document.getElementById('addBtn');
const itemList = document.getElementById('itemList');

let items = JSON.parse(localStorage.getItem('myList')) || [];

window.addEventListener('load', () => {
    // 1. Carregar i aplicar tema
    const savedTheme = localStorage.getItem('theme') || 'light';
    themeSelector.value = savedTheme;
    applyTheme(savedTheme);

    // 2. Renderitza la llista
    renderList();
});

themeSelector.addEventListener('change', () => {
    const selectedTheme = themeSelector.value;
    localStorage.setItem('theme', selectedTheme);
    applyTheme(selectedTheme);
});

// Funció que "encén/apaga" el mode fosc al CSS
function applyTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}

// Lògica de la llista
addBtn.addEventListener('click', () => {
    const text = itemInput.value.trim();
    if (text !== "") {
        items.push(text);
        localStorage.setItem('myList', JSON.stringify(items));
        itemInput.value = "";
        renderList();
    }
});

function renderList() {
    itemList.innerHTML = "";
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        itemList.appendChild(li);
    });
}
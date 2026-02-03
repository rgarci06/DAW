const themeSelector = document.getElementById('themeSelector');
const itemInput = document.getElementById('itemInput');
const addBtn = document.getElementById('addBtn');
const itemList = document.getElementById('itemList');

let items = JSON.parse(localStorage.getItem('myList')) || [];

// Al cargar la página
window.addEventListener('load', () => {
    // 1. Cargar y aplicar tema
    const savedTheme = localStorage.getItem('theme') || 'light';
    themeSelector.value = savedTheme;
    applyTheme(savedTheme);

    // 2. Renderizar lista
    renderList();
});

// Al cambiar el selector
themeSelector.addEventListener('change', () => {
    const selectedTheme = themeSelector.value;
    localStorage.setItem('theme', selectedTheme);
    applyTheme(selectedTheme);
});

// Función que "enciende/apaga" el modo oscuro en el CSS
function applyTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}

// Lógica de la lista
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
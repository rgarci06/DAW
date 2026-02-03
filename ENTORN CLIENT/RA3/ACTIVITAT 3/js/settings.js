window.addEventListener('load', () => {
    // APLICAR TEMA (Esto hace que funcione el modo oscuro aquí también)
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') document.body.classList.add('dark-mode');

    // Resto del código de settings...
    const configDiv = document.getElementById('currentConfig');
    const clearBtn = document.getElementById('clearBtn');
    const items = JSON.parse(localStorage.getItem('myList')) || [];

    configDiv.innerHTML = `
        <p><strong>Tema actual:</strong> ${savedTheme === 'dark' ? 'Oscuro' : 'Claro'}</p>
        <p><strong>Elementos:</strong> ${items.length}</p>
    `;

    clearBtn.addEventListener('click', () => {
        if(confirm("¿Borrar todo?")) {
            localStorage.clear();
            window.location.href = "index.html";
        }
    });
});
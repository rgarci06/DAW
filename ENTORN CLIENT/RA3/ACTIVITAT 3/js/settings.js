// Quan la pàgina està carregada, executo tot el codi
window.addEventListener('load', () => {
    
    // Miro si tinc guardat el tema de color al navegador
    const savedTheme = localStorage.getItem('theme');
    // Si veig que és el mode fosc, li dono la classe 'dark-mode' al body
    if (savedTheme === 'dark') document.body.classList.add('dark-mode');

    // Aquí agafo els elements de l'HTML que m'interessen per ID
    const configDiv = document.getElementById('currentConfig');
    const clearBtn = document.getElementById('clearBtn');
    
    // Intento carregar la meva llista; si no n'hi ha cap, em faig un array buit per no tindre errors
    const items = JSON.parse(localStorage.getItem('myList')) || [];

    // Actualitzo el contingut del div per mostrar el tema que tinc i quants ítems hi ha
    configDiv.innerHTML = `
        <p><strong>Tema actual:</strong> ${savedTheme === 'dark' ? 'Fosc' : 'Clar'}</p>
        <p><strong>Elements:</strong> ${items.length}</p>
    `;
    // Faig un esdeveniment per quan es premi el botó d'esborrar i avisar a l'usuari
    clearBtn.addEventListener('click', () => {
        if(confirm("¿Esborrar tot?")) {
            localStorage.clear();
            window.location.href = "index.html";
        }
    });
});
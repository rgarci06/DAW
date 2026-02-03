window.addEventListener('load', () => {
    // APLICAR TEMA
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') document.body.classList.add('dark-mode');

    // Resto del código de summary...
    const summaryContent = document.getElementById('summaryContent');
    const items = JSON.parse(localStorage.getItem('myList')) || [];

    summaryContent.innerHTML = `
        <ul>
            <li>Modo visual: <b>${savedTheme || 'Claro'}</b></li>
            <li>Total elementos: <b>${items.length}</b></li>
        </ul>
    `;
});
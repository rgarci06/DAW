window.addEventListener('load', () => {
    // Miro si tinc el tema guardat i, si és el fosc, l'activo
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') document.body.classList.add('dark-mode');

    const summaryContent = document.getElementById('summaryContent');
    
    // Recupero la llista del storage: la passo de text a array
    const items = JSON.parse(localStorage.getItem('myList')) || [];

    summaryContent.innerHTML = `
        <ul>
            <li>Mode visual: <b>${savedTheme || 'Clar'}</b></li>
            <li>Total elements: <b>${items.length}</b></li>
        </ul>
    `;
});
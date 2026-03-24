// busquem els elements per ID
const boton = document.getElementById('btnCarregar');
const tabla = document.getElementById('cosTaula');

// Esdeveniment al clicar el botó
boton.addEventListener('click', () => {
    
    fetch('productes.json')
        .then(res => res.json())
        .then(datos => {
            tabla.innerHTML = "";
            
            datos.forEach(p => {

                tabla.innerHTML += `
                    <tr>
                        <td>${p.id}</td>
                        <td>${p.nom}</td>
                        <td>${p.preu}€</td>
                    </tr>
                `;
            });
        })
        .catch(err => console.error("Error cargando el JSON", err));
});
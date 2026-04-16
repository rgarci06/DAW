const boto = document.getElementById('btnProductes');
const llista = document.getElementById('llistaProductes');

boto.addEventListener('click', () => {
  fetch('productes.json')
    .then(res => res.json())
    .then(dades => {
      llista.innerHTML = ""; 
      
      dades.forEach(p => {
        llista.innerHTML += `<li>${p.nom} - <strong>${p.preu}€</strong></li>`;
      });
    })
    .catch(err => console.error("Error carregant el JSON de productes", err));
});
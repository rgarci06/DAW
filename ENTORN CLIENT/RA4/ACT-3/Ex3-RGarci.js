const boto = document.getElementById('btnAlumnes');
const llista = document.getElementById('llistaAlumnes');

boto.addEventListener('click', () => {
  fetch('alumnes.json')
    .then(res => res.json())
    .then(dades => {
      llista.innerHTML = ""; // Netegem la llista
      
      dades.forEach(alumne => {
        llista.innerHTML += `<li>${alumne.nom}</li>`;
      });
    })
    .catch(err => console.error("Error carregant el JSON d'alumnes", err));
});
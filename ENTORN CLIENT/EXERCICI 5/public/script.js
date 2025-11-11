document.getElementById('registre').addEventListener('submit', function(event) {
  const nom       = document.getElementById('usuari').value.trim();
  const cognom1   = document.getElementById('cognom1').value.trim();
  const cognom2   = document.getElementById('cognom2').value.trim();
  const email     = document.getElementById('email').value.trim();
  const telefon   = document.getElementById('telefon').value.trim();
  const data      = document.getElementById('data').value.trim();
  const tarjeta   = document.getElementById('tarjeta').value.trim();
  const password  = document.getElementById('password').value;
  const password2 = document.getElementById('password2').value;
  const termes    = document.getElementById('termes').checked;

  // Validació: nom i cognoms amb majúscula inicial
  const regexNom = /^[A-Z][a-z]+$/;
  if (!nom.match(regexNom) || !cognom1.match(regexNom) || !cognom2.match(regexNom)) {
    event.preventDefault();
    alert('Omple el nom i cognoms amb majúscula inicial.');
    return;
  }

  // Correu electrònic simple
  if (!email.match(/^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$/)) {
    event.preventDefault();
    alert('Escriu un correu vàlid.');
    return;
  }

  // Telèfon: 9 xifres, comença per 6-9
  if (!telefon.match(/^[6-9]\d{2}[\s-]?\d{3}[\s-]?\d{3}$/)) {
    event.preventDefault();
    alert('Telèfon: 9 xifres començant per 6, 7, 8 o 9.');
    return;
  }

  // Data de naixement: dd/mm/aaaa
  if (!data.match(/^\d{2}\/\d{2}\/\d{4}$/)) {
    event.preventDefault();
    alert('Format data: dd/mm/aaaa');
    return;
  }

  // Targeta de crèdit: 16 xifres, accepta espai o guió
  if (!tarjeta.match(/^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$/)) {
    event.preventDefault();
    alert('Targeta: 16 xifres. Format correcta!');
    return;
  }

  // Contrasenya mínima: 8 caràcters
  if (password.length < 8) {
    event.preventDefault();
    alert('La contrasenya ha de tenir 8 caràcters.');
    return;
  }
  if (password !== password2) {
    event.preventDefault();
    alert('Les contrasenyes no coincideixen.');
    return;
  }

  // Accepta termes
  if (!termes) {
    event.preventDefault();
    alert('Accepta els termes per continuar.');
    return;
  }
});

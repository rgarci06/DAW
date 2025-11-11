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

  const regexNom = /^[A-Z][a-zàèéíòóúçñü']+$/;

  if (!nom.match(regexNom)) {
    event.preventDefault();
    alert('El nom ha de començar amb majúscula i només pot contenir lletres.');
    return;
  }
  if (!cognom1.match(regexNom)) {
    event.preventDefault();
    alert('El primer cognom ha de començar amb majúscula i només pot contenir lletres.');
    return;
  }
  if (!cognom2.match(regexNom)) {
    event.preventDefault();
    alert('El segon cognom ha de començar amb majúscula i només pot contenir lletres.');
    return;
  }

  if (!email.match(/^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$/)) {
    event.preventDefault();
    alert('Introdueix un correu electrònic vàlid (nom@domini.extensió).');
    return;
  }

  if (!telefon.match(/^[6-9]\d{2}[\s-]?\d{3}[\s-]?\d{3}$/)) {
    event.preventDefault();
    alert('El número de telèfon ha de tenir 9 dígits, començar per 6, 7, 8 o 9. Pots utilitzar espais o guions.');
    return;
  }

  if (!data.match(/^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/)) {
    event.preventDefault();
    alert('La data de naixement ha de tenir el format dd/mm/aaaa, dia entre 01 i 31, mes entre 01 i 12, any de 4 xifres.');
    return;
  }

  if (!tarjeta.match(/^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$/)) {
    event.preventDefault();
    alert('La targeta de crèdit ha de tenir el format XXXX-XXXX-XXXX-XXXX o XXXX XXXX XXXX XXXX.');
    return;
  }

  if (!password.match(/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/)) {
    event.preventDefault();
    alert('La contrasenya ha de tenir mínim 8 caràcters, una majúscula, una minúscula, un número i un caràcter especial.');
    return;
  }

  if (password !== password2) {
    event.preventDefault();
    alert('Les contrasenyes no coincideixen.');
    return;
  }

  if (!termes) {
    event.preventDefault();
    alert('Has d\'acceptar els termes i condicions per registrar-te.');
    return;
  }
});

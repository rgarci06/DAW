const form = document.getElementById('registre');
const username = document.getElementById('usuari');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const termes = document.getElementById('termes');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  if (username.value.trim() === '') {
    alert("El nom d'usuari no pot estar buit.");
    return;
  }
  if (!validateEmail(email.value.trim())) {
    alert("El correu electrònic no té un format vàlid.");
    return;
  }
  if (password.value.length < 8) {
    alert("La contrasenya ha de tenir almenys 8 caràcters.");
    return;
  }
  if (password.value !== password2.value) {
    alert("Les contrasenyes no coincideixen.");
    return;
  }
  if (!termes.checked) {
    alert("Has d'acceptar els termes i condicions.");
    return;
  }

  // Si arriba aquí, es pot enviar el formulari
  alert("Registre correcte!");
  form.submit();
});

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(email).toLowerCase());
}

  const form = document.getElementById('registro');
  const usernameInput = document.getElementById('usuari');
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');

  document.getElementById('registro').addEventListener('submit', function(event) {
    // Previene el envío del formulario por defecto
    event.preventDefault();

    // Obtiene el valor del input y elimina los espacios en blanco
    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    // Valida si el campo está vacío
    if (username === '') {
      alert('El nombre de usuario no puede estar vacío.');
    } else if (email === '') {
      alert('El email no puede estar vacío.');
    } else if (password === '') {
      alert('La contraseña no puede estar vacía.');
    } else {
      // Si no está vacío, puedes enviar el formulario
      alert('¡Nombre de usuario válido!');
      form.submit(); // O cualquier otra lógica que necesites
    }
  });

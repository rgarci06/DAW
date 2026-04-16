const boto = document.getElementById("btnError");
const resultat = document.getElementById("resultat");

boto.addEventListener("click", function () {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "inexistent.txt", true);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        resultat.innerHTML = "<p style='color: green;'>La resposta és correcta. S'ha trobat el fitxer.</p>";
      } else if (xhr.status === 404) {
        resultat.innerHTML = "<p style='color: red;'>Error 404: El fitxer sol·licitat no existeix.</p>";
      } else {
        resultat.innerHTML = `<p style='color: orange;'>S'ha produït un altre error. Codi d'estat: ${xhr.status}</p>`;
      }
    }
  };

  xhr.send();
});
const xhr = new XMLHttpRequest();
xhr.open("POST", "usuari.php", true);
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

xhr.onreadystatechange = function () {
	if (xhr.readyState === 4) {
		if (xhr.status === 200) {
			console.log("Resposta del servidor:", xhr.responseText);
		} else {
			console.error("Error en la petició:", xhr.status, xhr.statusText);
		}
	}
};

const nom = "Joan";
const edat = 25;
const dades = `nom=${encodeURIComponent(nom)}&edat=${encodeURIComponent(edat)}`;

xhr.send(dades);

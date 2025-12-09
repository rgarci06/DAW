// =======================
// CADENES DE TEXT
// =======================

// ACT 1
// Donada la cadena: let frase = "Aprendre JavaScript és útil";
// 1) Mostra la longitud de la cadena.
// 2) Converteix tota la frase a minúscules.
// 3) Extreu la paraula "JavaScript" mitjançant substring().
// 4) Comprova si la frase inclou la paraula "útil".

let frase = "Aprendre JavaScript és útil";

console.log(frase.length);           // 1
console.log(frase.toLowerCase());    // 2
console.log(frase.substring(9, 19)); // 3
console.log(frase.includes("útil")); // 4

// ACT 2
// Demana a l’usuari una frase amb prompt() i:
// 1) Mostra el primer caràcter.
// 2) Mostra els 5 primers caràcters.
// 3) Indica si la frase comença per "Hola".

let txt = prompt("Escriu una frase");

console.log(txt[0]);                 // 1
console.log(txt.substring(0, 5));    // 2
console.log(txt.startsWith("Hola")); // 3

// ACT 3
// Converteix la frase "Programació Web" en un array de paraules.

let paraules = "Programació Web".split(" ");
console.log(paraules);

// ACT 4
// Utilitza repeat() per mostrar la paraula "Hola" cinc vegades.

console.log("Hola".repeat(5));


// =======================
// NOMBRES
// =======================

// ACT 1
// Demana dos números a l’usuari i mostra el resultat de la seva divisió.
// Controla amb isNaN() si els valors són numèrics.

let a = Number(prompt("Primer número"));
let b = Number(prompt("Segon número"));

if (isNaN(a) || isNaN(b)) {
  console.log("Error: no són números");
} else {
  console.log(a / b);
}

// ACT 2
// Calcula el resultat de 10/0 i -10/0 i explica què succeeix.

console.log(10 / 0);
console.log(-10 / 0);
// A la consola veuràs Infinity i -Infinity.

// ACT 3
// Donat el número 1234.56789, mostra’l:
// 1) Amb un decimal.
// 2) Sense decimals.
// 3) Amb 3 decimals.

let n = 1234.56789;

console.log(n.toFixed(1));  // 1
console.log(n.toFixed(0));  // 2
console.log(n.toFixed(3));  // 3

// ACT 4
// Demana un valor numèric i mostra’l amb format de dos decimals utilitzant toFixed().

let num = Number(prompt("Número"));
console.log(num.toFixed(2));


// =======================
// DIÀLEGS I TEMPORITZACIÓ
// =======================

// ACT 1
// Mostra un missatge amb alert() quan carregui la pàgina.

window.onload = function () {
  alert("Pàgina carregada");
};

// ACT 2
// Fes un confirm() que pregunti a l’usuari si vol continuar.
// Si diu que sí, mostra un alert() amb "Has acceptat".
// Si diu que no, mostra "Has cancel·lat".

let ok = confirm("Vols continuar?");
if (ok) {
  alert("Has acceptat");
} else {
  alert("Has cancel·lat");
}

// ACT 3
// Demana el nom amb prompt() i mostra un missatge personalitzat.

let nom = prompt("Nom?");
alert("Hola " + nom);

// ACT 4
// Fes que aparegui un missatge "Hola!" als 3 segons d’entrar a la pàgina utilitzant setTimeout().

setTimeout(function () {
  alert("Hola!");
}, 3000);

// ACT 5
// Mostra l’hora actual cada segon amb setInterval().

setInterval(function () {
  console.log(new Date().toLocaleTimeString());
}, 1000);

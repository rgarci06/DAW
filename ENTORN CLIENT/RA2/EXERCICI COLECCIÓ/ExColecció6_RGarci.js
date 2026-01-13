// MAP D’ESTOC - RGarci

// Objecte que fa de "map"
let estocPerNom = {};

// Omple l'objecte a partir de l'array
function actualitzarMapDesDeArray() {
  estocPerNom = {};
  for (let i = 0; i < inventari.length; i++) {
    estocPerNom[inventari[i].nom] = inventari[i].stock;
  }
}

// Omple l'array a partir de l'objecte
function actualitzarArrayDesDeMap() {
  for (let i = 0; i < inventari.length; i++) {
    const nom = inventari[i].nom;
    if (estocPerNom[nom] !== undefined) {
      inventari[i].stock = estocPerNom[nom];
    }
  }
}

// Execució
actualitzarMapDesDeArray();
console.log(estocPerNom);
estocPerNom["Teclat"] = 99;
actualitzarArrayDesDeMap();
console.log(inventari);
// PRODUCTES SENSE ESTOC - RGarci

// Retorna un array de productes amb stock 0
function senseEstoc() {
  const resultat = [];
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].stock === 0) {
      resultat.push(inventari[i]);
    }
  }
  return resultat;
}

// Torna true si hi ha algun producte sense estoc
function hiHaSenseEstoc() {
  return senseEstoc().length > 0;
}

// Execució
console.log(senseEstoc());
console.log("Hi ha sense estoc?", hiHaSenseEstoc());

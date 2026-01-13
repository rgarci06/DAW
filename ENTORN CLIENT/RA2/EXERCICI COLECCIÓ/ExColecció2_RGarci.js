// ALTA I BAIXA DE PRODUCTES - RGarci

// Busca un producte pel nom
function cercarProducte(nom) {
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].nom === nom) {
      return inventari[i];
    }
  }
  return null;
}

// Afegeix un producte nou
function altaProducte(nom, stock) {
  if (cercarProducte(nom)) {
    console.log("Ja existeix");
    return;
  }
  inventari.push({ nom: nom, stock: stock, venuts: 0 });
  console.log("Afegit");
}

// Dona de baixa un producte
function baixaProducte(nom) {
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].nom === nom) {
      inventari.splice(i, 1);
      console.log("Eliminat");
      return;
    }
  }
  console.log("No trobat");
}

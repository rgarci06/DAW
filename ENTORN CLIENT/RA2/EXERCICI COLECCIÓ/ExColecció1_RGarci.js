// INVENTARI BÀSIC - RGarci

// Mostra tots els productes
function llistarProductes() {
  for (let i = 0; i < inventari.length; i++) {
    const p = inventari[i];
    console.log(p.nom, "stock:", p.stock, "venuts:", p.venuts);
  }
}

// Busca un producte pel nom
function cercarProducte(nom) {
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].nom === nom) {
      return inventari[i];
    }
  }
  return null;
}

// Compra unitats si hi ha estoc
function comprar(nom, unitats) {
  const p = cercarProducte(nom);
  if (!p) {
    console.log("Producte no trobat");
    return;
  }
  if (unitats > p.stock) {
    console.log("No hi ha prou estoc");
    return;
  }
  p.stock = p.stock - unitats;
  p.venuts = p.venuts + unitats;
  console.log("Compra feta");
}

// Proves
llistarProductes();
comprar("Teclat", 2);
llistarProductes();

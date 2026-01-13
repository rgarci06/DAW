// CATEGORIES ÚNIQUES - RGarci

let inventari = [
  { nom: "Teclat", stock: 10, venuts: 0, categoria: "Perifèrics" },
  { nom: "Ratolí", stock: 5, venuts: 0, categoria: "Perifèrics" },
  { nom: "Monitor", stock: 3, venuts: 0, categoria: "Pantalles" },
  { nom: "Portàtil", stock: 7, venuts: 0, categoria: "Ordinadors" },
  { nom: "Impressora", stock: 0, venuts: 0, categoria: "Impressió" }
];

// Retorna categories sense repetir
function categoriesUniques() {
  const cats = [];

  for (let i = 0; i < inventari.length; i++) {
    const c = inventari[i].categoria; // ara sí existeix
    let trobat = false;
    for (let j = 0; j < cats.length; j++) {
      if (cats[j] === c) {
        trobat = true;
      }
    }
    if (!trobat) {
      cats.push(c);
    }
  }

  cats.sort();
  console.log("Categories:", cats);
  return cats;
}

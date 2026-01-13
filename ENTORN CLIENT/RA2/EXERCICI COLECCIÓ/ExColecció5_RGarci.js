// ESTADÍSTIQUES DE L'INVENTARI - RGarci

// Calcula totals i màxims/mínims de stock
function estadistiquesInventari() {
  let totalStock = 0;
  let totalVenuts = 0;
  let max = null;
  let min = null;

  for (let i = 0; i < inventari.length; i++) {
    const p = inventari[i];
    totalStock += p.stock;
    totalVenuts += p.venuts;

    if (!max || p.stock > max.stock) max = p;
    if (!min || p.stock < min.stock) min = p;
  }

  console.log("Total stock:", totalStock);
  console.log("Total venuts:", totalVenuts);
  console.log("Més estoc:", max.nom, max.stock);
  console.log("Menys estoc:", min.nom, min.stock);
}

// Execució
estadistiquesInventari();

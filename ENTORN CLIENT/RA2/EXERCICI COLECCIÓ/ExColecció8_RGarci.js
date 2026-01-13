// MENÚ DE GESTIÓ PER CONSOLA (AMB prompt) - Navegador

// --- Funcions bàsiques (ex8) ---

// Llista productes de l'ex8
function llistarProductes8() {
  console.log("Llista de productes (ex8):");
  for (let i = 0; i < inventari.length; i++) {
    const p = inventari[i];
    console.log(p.nom, "stock:", p.stock, "venuts:", p.venuts);
  }
}

// Cerca producte pel nom en inventari
function cercarProducte8(nom) {
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].nom === nom) {
      return inventari[i];
    }
  }
  return null;
}

// Compra producte en inventari
function comprar8(nom, unitats) {
  const p = cercarProducte8(nom);
  if (!p) {
    console.log("Producte no trobat");
    return;
  }
  if (unitats > p.stock) {
    console.log("No hi ha prou estoc");
    return;
  }
  p.stock -= unitats;
  p.venuts += unitats;
  console.log("Compra feta");
}

// Alta de producte en inventari
function altaProducte8(nom, stock) {
  if (cercarProducte8(nom)) {
    console.log("Ja existeix");
    return;
  }
  inventari.push({ nom: nom, stock: stock, venuts: 0 });
  console.log("Afegit");
}

// Baixa de producte en inventari
function baixaProducte8(nom) {
  for (let i = 0; i < inventari.length; i++) {
    if (inventari[i].nom === nom) {
      inventari.splice(i, 1);
      console.log("Eliminat");
      return;
    }
  }
  console.log("No trobat");
}

// Rànquing més venuts sobre inventari
function rankingMesVenuts8() {
  let c1 = null, c2 = null, c3 = null;

  for (let i = 0; i < inventari.length; i++) {
    const p = inventari[i];

    if (!c1 || p.venuts > c1.venuts) {
      c3 = c2;
      c2 = c1;
      c1 = p;
    } else if (!c2 || p.venuts > c2.venuts) {
      c3 = c2;
      c2 = p;
    } else if (!c3 || p.venuts > c3.venuts) {
      c3 = p;
    }
  }

  console.log("Rànquing més venuts:");
  if (c1) console.log("1)", c1.nom, c1.venuts);
  if (c2) console.log("2)", c2.nom, c2.venuts);
  if (c3) console.log("3)", c3.nom, c3.venuts);
}

// --- MENÚ AMB PROMPT ---

function mostrarMenu8() {
  console.log("\n=== MENÚ INVENTARI ===");
  console.log("1) Llistar productes");
  console.log("2) Comprar producte");
  console.log("3) Alta producte");
  console.log("4) Baixa producte");
  console.log("5) Rànquing més venuts");
  console.log("0) Sortir");
}

// Aquesta funció es diu EXACTAMENT "menu"
function menu() {
  let opcio;
  do {
    mostrarMenu8();
    const resposta = prompt("Opcio (0-5):");
    if (resposta === null) {
      console.log("Sortint...");
      break;
    }

    opcio = Number(resposta);

    if (opcio === 1) {
      console.clear();
      llistarProductes8();
    } else if (opcio === 2) {
      const nom = prompt("Nom del producte:");
      const unitats = Number(prompt("Unitats:"));
      comprar8(nom, unitats);
    } else if (opcio === 3) {
      const nom = prompt("Nom nou producte:");
      const stock = Number(prompt("Stock inicial:"));
      altaProducte8(nom, stock);
    } else if (opcio === 4) {
      const nom = prompt("Nom producte a eliminar:");
      baixaProducte8(nom);
    } else if (opcio === 5) {
      console.clear();
      rankingMesVenuts8();
    } else if (opcio === 0) {
      console.log("Sortint...");
    } else {
      console.log("Opcio no valida");
    }
  } while (opcio !== 0);
}

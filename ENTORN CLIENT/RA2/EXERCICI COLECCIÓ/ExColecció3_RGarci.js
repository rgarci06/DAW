// RÀNQUING DE PRODUCTES MÉS VENUTS - RGarci

// Mostra el top 3 més venuts (sense tocar l'array original)
function rankingMesVenuts() {
  const copia = [];
  for (let i = 0; i < inventari.length; i++) {
    copia.push(inventari[i]);
  }

  // Ordenació molt simple (bubble sort)
  for (let i = 0; i < copia.length - 1; i++) {
    for (let j = 0; j < copia.length - 1; j++) {
      if (copia[j].venuts < copia[j + 1].venuts) {
        const tmp = copia[j];
        copia[j] = copia[j + 1];
        copia[j + 1] = tmp;
      }
    }
  }

  for (let i = 0; i < 3 && i < copia.length; i++) {
    console.log((i + 1) + ")", copia[i].nom, "-", copia[i].venuts, "venuts");
  }
}

// Execució
rankingMesVenuts();

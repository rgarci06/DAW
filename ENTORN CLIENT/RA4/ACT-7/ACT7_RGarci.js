/* Preguntes 1 i 2: Completa el codi per comprovar si la resposta és correcta utilitzant response.ok. Afegeix la instrucció necessària per convertir la resposta a JSON. */

fetch("productes.json")
  .then(response => {
    if (!response.ok) {
      throw new Error("Error de xarxa: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.log("Error:", error);
  });


/* Pregunta 3: Explica per què response.json() retorna una promesa. */

/* Resposta: response.json() retorna una promesa perquè el procés de llegir tot el flux de dades de la resposta i convertir-lo a JSON triga un temps. Així no bloquejem la resta del programa mentre esperem. */


/* Pregunta 4: Reescriu el codi utilitzant async/await. */

async function obtenirProductes() {
  try {
    const response = await fetch("productes.json");
    if (!response.ok) {
      throw new Error("Error de xarxa: " + response.status);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log("Error:", error);
  }
}

obtenirProductes();


/* Pregunta 5: Indica un avantatge de fetch() respecte a XMLHttpRequest. */

/* Resposta: L'avantatge principal és que fetch() està basat nativament en Promeses. Això permet tenir un codi més net, directe i fàcil d'encadenar, evitant l'estructura complexa i els callbacks imbricats que solia requerir XMLHttpRequest. */
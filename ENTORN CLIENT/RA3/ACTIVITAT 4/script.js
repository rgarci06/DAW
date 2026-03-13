// Inventari inicial
let productesDisponibles = [
    { id: 1, nom: "Tornavís", preu: 5.50, stock: 10 },
    { id: 2, nom: "Martell", preu: 12.00, stock: 5 },
    { id: 3, nom: "Trepant", preu: 45.00, stock: 3 },
    { id: 4, nom: "Claus (caixa)", preu: 3.20, stock: 20 }
];

let carret = [];

// 1. RECUPERAR DADES EN CARREGAR LA PÀGINA
document.addEventListener('DOMContentLoaded', () => {
    let dadesCarret = localStorage.getItem('carretGuardat');
    let dadesStock = localStorage.getItem('stockGuardat');

    // Si hi ha dades guardades d'abans, les carreguem
    if (dadesCarret) {
        carret = JSON.parse(dadesCarret);
    }
    if (dadesStock) {
        productesDisponibles = JSON.parse(dadesStock);
    }

    pintarProductes();
    pintarCarret();
});

// Funció per mostrar els productes per pantalla
function pintarProductes() {
    let contenidor = document.getElementById('contenedor-productos');
    contenidor.innerHTML = '';

    for (let i = 0; i < productesDisponibles.length; i++) {
        let prod = productesDisponibles[i];
        let div = document.createElement('div');
        div.className = 'producto-card';

        let botoDesactivat = "";
        let textBoto = "Afegir al carretó";

        if (prod.stock === 0) {
            botoDesactivat = "disabled";
            textBoto = "Esgotat";
        }

        div.innerHTML = `
            <h3>${prod.nom}</h3>
            <p>Preu: ${prod.preu}€</p>
            <p>Stock: ${prod.stock}</p>
            <button class="btn-agregar" onclick="afegirAlCarret(${prod.id})" ${botoDesactivat}>
                ${textBoto}
            </button>
        `;
        contenidor.appendChild(div);
    }
}

// 2. AFEGIR AL CARRETÓ I RESTAR STOCK
function afegirAlCarret(id) {
    // Busquem el producte a l'array de disponibles
    let producte = productesDisponibles.find(p => p.id === id);

    if (producte.stock > 0) {
        producte.stock--; // Restem 1 a l'stock de la botiga

        // Busquem si el producte ja està posat al carretó
        let itemAlCarret = carret.find(item => item.id === id);

        if (itemAlCarret) {
            itemAlCarret.quantitat++; // Si ja hi és, sumem 1 a la quantitat
        } else {
            // Si no hi és, el creem de nou al carretó
            carret.push({
                id: producte.id,
                nom: producte.nom,
                preu: producte.preu,
                quantitat: 1
            });
        }

        guardarDades();
        pintarProductes();
        pintarCarret();
    }
}

// 3. ELIMINAR DEL CARRETÓ I RETORNAR STOCK
function eliminarDelCarret(id) {
    let itemAlCarret = carret.find(item => item.id === id);
    let producte = productesDisponibles.find(p => p.id === id);

    if (itemAlCarret) {
        itemAlCarret.quantitat--; // Treiem 1 del carretó
        producte.stock++; // Li tornem 1 a l'stock de la botiga

        // Si la quantitat arriba a 0, traiem el producte del carretó
        if (itemAlCarret.quantitat === 0) {
            carret = carret.filter(item => item.id !== id);
        }

        guardarDades();
        pintarProductes();
        pintarCarret();
    }
}

// Funció per mostrar el carretó i el preu total
function pintarCarret() {
    let llista = document.getElementById('lista-carrito');
    let spanTotal = document.getElementById('total');

    llista.innerHTML = '';
    let total = 0;

    for (let i = 0; i < carret.length; i++) {
        let item = carret[i];
        let subtotal = item.preu * item.quantitat;
        total = total + subtotal;

        let li = document.createElement('li');
        li.className = 'item-carrito';
        li.innerHTML = `
            <span>${item.nom} (x${item.quantitat})</span>
            <span>${subtotal.toFixed(2)}€</span>
            <button class="btn-eliminar" onclick="eliminarDelCarret(${item.id})">X</button>
        `;
        llista.appendChild(li);
    }

    spanTotal.innerText = total.toFixed(2);
}

// 4. GUARDAR AL LOCALSTORAGE
function guardarDades() {
    localStorage.setItem('carretGuardat', JSON.stringify(carret));
    localStorage.setItem('stockGuardat', JSON.stringify(productesDisponibles));
}

// 5. BUIDAR CARRETÓ I COMPRAR
document.getElementById('btn-vaciar').addEventListener('click', () => {
    localStorage.clear(); // Esborrem la memòria
    location.reload(); // Recarreguem la pàgina per tornar a l'inventari original
});

document.getElementById('btn-comprar').addEventListener('click', () => {
    if (carret.length > 0) {
        alert("Compra finalitzada!");
        localStorage.removeItem('carretGuardat'); // Esborro només el carretó
        location.reload();
    } else {
        alert("El carretó està buit");
    }
});
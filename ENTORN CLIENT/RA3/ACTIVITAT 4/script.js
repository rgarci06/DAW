// Inventario inicial
let productosDisponibles = [
    { id: 1, nombre: "Destornillador", precio: 5.50, stock: 10 },
    { id: 2, nombre: "Martillo", precio: 12.00, stock: 5 },
    { id: 3, nombre: "Taladro", precio: 45.00, stock: 3 },
    { id: 4, nombre: "Clavos (caja)", precio: 3.20, stock: 20 }
];

let carrito = [];

// 1. RECUPERAR DATOS AL CARGAR LA PÁGINA
document.addEventListener('DOMContentLoaded', () => {
    let datosCarrito = localStorage.getItem('carritoGuardado');
    let datosStock = localStorage.getItem('stockGuardado');

    // Si hay datos guardados de antes, los cargamos
    if (datosCarrito) {
        carrito = JSON.parse(datosCarrito);
    }
    if (datosStock) {
        productosDisponibles = JSON.parse(datosStock);
    }

    pintarProductos();
    pintarCarrito();
});

// Función para mostrar los productos en pantalla
function pintarProductos() {
    let contenedor = document.getElementById('contenedor-productos');
    contenedor.innerHTML = '';

    for (let i = 0; i < productosDisponibles.length; i++) {
        let prod = productosDisponibles[i];
        let div = document.createElement('div');
        div.className = 'producto-card';

        let botonDesactivado = "";
        let textoBoton = "Añadir al carrito";

        if (prod.stock === 0) {
            botonDesactivado = "disabled";
            textoBoton = "Agotado";
        }

        div.innerHTML = `
            <h3>${prod.nombre}</h3>
            <p>Precio: ${prod.precio}€</p>
            <p>Stock: ${prod.stock}</p>
            <button class="btn-agregar" onclick="agregarAlCarrito(${prod.id})" ${botonDesactivado}>
                ${textoBoton}
            </button>
        `;
        contenedor.appendChild(div);
    }
}

// 2. AÑADIR AL CARRITO Y RESTAR STOCK
function agregarAlCarrito(id) {
    // Buscamos el producto en el array de disponibles
    let producto = productosDisponibles.find(p => p.id === id);

    if (producto.stock > 0) {
        producto.stock--; // Restamos 1 al stock de la tienda

        // Buscamos si el producto ya está metido en el carrito
        let itemEnCarrito = carrito.find(item => item.id === id);

        if (itemEnCarrito) {
            itemEnCarrito.cantidad++; // Si ya está, sumamos 1 a la cantidad
        } else {
            // Si no está, lo creamos nuevo en el carrito
            carrito.push({
                id: producto.id,
                nombre: producto.nombre,
                precio: producto.precio,
                cantidad: 1
            });
        }

        guardarDatos();
        pintarProductos();
        pintarCarrito();
    }
}

// 3. ELIMINAR DEL CARRITO Y DEVOLVER STOCK
function eliminarDelCarrito(id) {
    let itemEnCarrito = carrito.find(item => item.id === id);
    let producto = productosDisponibles.find(p => p.id === id);

    if (itemEnCarrito) {
        itemEnCarrito.cantidad--; // Quitamos 1 del carrito
        producto.stock++; // Le devolvemos 1 al stock de la tienda

        // Si la cantidad llega a 0, sacamos el producto del carrito
        if (itemEnCarrito.cantidad === 0) {
            carrito = carrito.filter(item => item.id !== id);
        }

        guardarDatos();
        pintarProductos();
        pintarCarrito();
    }
}

// Función para mostrar el carrito y el precio total
function pintarCarrito() {
    let lista = document.getElementById('lista-carrito');
    let spanTotal = document.getElementById('total');

    lista.innerHTML = '';
    let total = 0;

    for (let i = 0; i < carrito.length; i++) {
        let item = carrito[i];
        let subtotal = item.precio * item.cantidad;
        total = total + subtotal;

        let li = document.createElement('li');
        li.className = 'item-carrito';
        li.innerHTML = `
            <span>${item.nombre} (x${item.cantidad})</span>
            <span>${subtotal.toFixed(2)}€</span>
            <button class="btn-eliminar" onclick="eliminarDelCarrito(${item.id})">X</button>
        `;
        lista.appendChild(li);
    }

    spanTotal.innerText = total.toFixed(2);
}

// 4. GUARDAR EN LOCALSTORAGE
function guardarDatos() {
    localStorage.setItem('carritoGuardado', JSON.stringify(carrito));
    localStorage.setItem('stockGuardado', JSON.stringify(productosDisponibles));
}

// 5. VACIAR CARRITO Y COMPRAR (Botones)
document.getElementById('btn-vaciar').addEventListener('click', () => {
    localStorage.clear(); // Borramos la memoria
    location.reload(); // Recargamos la página para volver al inventario original
});

document.getElementById('btn-comprar').addEventListener('click', () => {
    if (carrito.length > 0) {
        alert("¡Compra finalizada!");
        localStorage.removeItem('carritoGuardado'); // Borramos solo el carrito
        location.reload(); // Recargamos la página (el stock se queda guardado)
    } else {
        alert("El carrito está vacío");
    }
});
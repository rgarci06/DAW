// ---------------------------------------------------------
// 1. MODELO DE DATOS (POO)
// ---------------------------------------------------------

// Creo la clase Libro con las propiedades que me piden
class Libro {
    constructor(titulo, autor, isbn, anio, prestamos = 0) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.anio = Number(anio); // Me aseguro de guardarlo como número
        this.prestamos = prestamos;
    }

    // Método para sumar un préstamo
    prestar() {
        this.prestamos++;
    }
}

// Inicializo mi aplicación con 4 libros de prueba en un array
let biblioteca = [
    new Libro("El Quijote", "Cervantes", "111-1-1111111", 1605, 5),
    new Libro("1984", "Orwell", "222-2-2222222", 1949, 10),
    new Libro("Dune", "Herbert", "333-3-3333333", 1965, 2),
    new Libro("Fundación", "Asimov", "444-4-4444444", 1951, 8)
];

// ---------------------------------------------------------
// 2. REFERENCIAS AL DOM (Selecciono los elementos del HTML)
// ---------------------------------------------------------
const formLibro = document.getElementById("formLibro");
const listaLibros = document.getElementById("listaLibros");
const inputBusqueda = document.getElementById("busqueda");
const divStats = document.getElementById("stats");

const btnRanking = document.getElementById("btnRanking");
const btnGuardar = document.getElementById("btnGuardar");
const btnCargar = document.getElementById("btnCargar");
const btnFetch = document.getElementById("btnFetch");

// ---------------------------------------------------------
// 3. LÓGICA PRINCIPAL Y MÉTODOS DE ARRAY
// ---------------------------------------------------------

// Función para pintar los libros en el HTML (Uso de forEach)
const listarLibros = (arrayLibros = biblioteca) => {
    listaLibros.innerHTML = ""; // Limpio la lista antes de volver a pintar

    arrayLibros.forEach(libro => {
        // Creo el elemento de la lista para cada libro usando Template Literals
        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${libro.titulo}</strong> - ${libro.autor} (ISBN: ${libro.isbn}) | Año: ${libro.anio} | Préstamos: ${libro.prestamos}
            <button class="btn-prestar" data-isbn="${libro.isbn}">Prestar</button>
            <button class="btn-eliminar" data-isbn="${libro.isbn}">Eliminar</button>
        `;
        listaLibros.appendChild(li);
    });

    // Actualizo las estadísticas cada vez que pinto la lista
    estadisticas();
};

// Función para buscar un libro exacto por título (Uso de find)
const buscarLibro = (titulo) => {
    return biblioteca.find(libro => libro.titulo === titulo);
};

// Función para borrar un libro por su ISBN (Uso de findIndex)
const eliminarLibro = (isbn) => {
    // Busco en qué posición del array está el libro
    const index = biblioteca.findIndex(libro => libro.isbn === isbn);
    if (index !== -1) {
        biblioteca.splice(index, 1); // Lo borro del array
        listarLibros(); // Vuelvo a pintar la lista para que desaparezca
    }
};

// Función para filtrar mientras escribo (Uso de filter e includes)
const filtrarLibros = (texto) => {
    const textoMinusculas = texto.toLowerCase();
    // Me quedo solo con los que coinciden en título o autor
    const filtrados = biblioteca.filter(libro => 
        libro.titulo.toLowerCase().includes(textoMinusculas) || 
        libro.autor.toLowerCase().includes(textoMinusculas)
    );
    listarLibros(filtrados); // Pinto solo los filtrados
};

// Función para ordenar por préstamos (Uso de sort)
const rankingPrestamos = () => {
    // Hago una copia del array con spread operator (...) para no modificar el original
    const copiaBiblioteca = [...biblioteca];
    copiaBiblioteca.sort((a, b) => b.prestamos - a.prestamos);
    listarLibros(copiaBiblioteca);
};

// Función para calcular estadísticas (Uso de reduce y map)
const estadisticas = () => {
    const totalLibros = biblioteca.length;
    
    // Sumo todos los préstamos
    const sumaPrestamos = biblioteca.reduce((acumulador, libro) => acumulador + libro.prestamos, 0);
    
    // Saco solo los años con map, y luego busco el mayor y el menor
    const anios = biblioteca.map(libro => libro.anio);
    const anioMasAntiguo = anios.length > 0 ? Math.min(...anios) : "N/A";
    const anioMasReciente = anios.length > 0 ? Math.max(...anios) : "N/A";

    // Lo pinto en la pantalla
    divStats.innerHTML = `
        <p>Total Llibres: ${totalLibros} | Total Préstecs: ${sumaPrestamos} | Més antic: ${anioMasAntiguo} | Més nou: ${anioMasReciente}</p>
    `;
};

// ---------------------------------------------------------
// 4. EVENTOS Y VALIDACIONES
// ---------------------------------------------------------

// Evento para añadir un libro nuevo
formLibro.addEventListener("submit", (e) => {
    e.preventDefault(); // Evito que la página recargue al enviar el form

    // Recojo los valores del formulario
    const titulo = document.getElementById("titulo").value.trim();
    const autor = document.getElementById("autor").value.trim();
    const isbn = document.getElementById("isbn").value.trim();
    const anio = document.getElementById("anio").value.trim();

    // Validaciones
    if (!titulo || !autor) {
        alert("El título y el autor son obligatorios.");
        return;
    }
    
    if (isNaN(anio) || anio === "") {
        alert("El año debe ser un valor numérico.");
        return;
    }

    // Expresión regular para el ISBN
    const patronISBN = /^[0-9]{3}-[0-9]{1,5}-[0-9]{1,7}$/;
    if (!patronISBN.test(isbn)) {
        alert("El formato del ISBN es incorrecto. Debe ser, por ejemplo, 000-0-000.");
        return;
    }

    // Si todo está bien, creo el libro, lo meto en el array y limpio el form
    const nuevoLibro = new Libro(titulo, autor, isbn, anio);
    biblioteca.push(nuevoLibro);
    listarLibros();
    formLibro.reset();
});

// Evento dinámico para los botones de "Prestar" y "Eliminar" de la lista
listaLibros.addEventListener("click", (e) => {
    // Si he hecho clic en un botón de eliminar...
    if (e.target.classList.contains("btn-eliminar")) {
        const isbn = e.target.getAttribute("data-isbn");
        eliminarLibro(isbn);
    }
    
    // Si he hecho clic en un botón de prestar...
    if (e.target.classList.contains("btn-prestar")) {
        const isbn = e.target.getAttribute("data-isbn");
        // Busco el libro por ISBN en vez de por título para ser más exacto
        const libro = biblioteca.find(l => l.isbn === isbn);
        if (libro) {
            libro.prestar();
            listarLibros(); // Repinto para actualizar el número de préstamos
        }
    }
});

// Evento para el buscador en tiempo real
inputBusqueda.addEventListener("input", (e) => {
    filtrarLibros(e.target.value);
});

// Evento para ver el ranking
btnRanking.addEventListener("click", rankingPrestamos);

// ---------------------------------------------------------
// 5. LOCALSTORAGE Y FETCH API (Persistencia y Asincronía)
// ---------------------------------------------------------

// Guardar en LocalStorage
btnGuardar.addEventListener("click", () => {
    // Convierto mi array de objetos a texto JSON y lo guardo
    localStorage.setItem("bibliotecaLocal", JSON.stringify(biblioteca));
    alert("Datos guardados en LocalStorage.");
});

// Recuperar de LocalStorage
btnCargar.addEventListener("click", () => {
    const datosGuardados = localStorage.getItem("bibliotecaLocal");
    if (datosGuardados) {
        // Los parseo y los vuelvo a convertir en instancias de la clase Libro
        // para no perder el método prestar()
        const datosParseados = JSON.parse(datosGuardados);
        biblioteca = datosParseados.map(obj => new Libro(obj.titulo, obj.autor, obj.isbn, obj.anio, obj.prestamos));
        listarLibros();
        alert("Datos recuperados correctamente.");
    } else {
        alert("No hay datos guardados.");
    }
});

// Importar desde JSON externo con Fetch
const cargarLibrosExternos = async () => {
    try {
        // Hago la petición al archivo json
        const respuesta = await fetch("libros.json");
        
        // Compruebo si la respuesta ha ido bien (propiedad ok)
        if (!respuesta.ok) {
            throw new Error("No se ha podido cargar el archivo JSON");
        }
        
        const librosNuevos = await respuesta.json();
        
        // Convierto los datos importados en instancias de mi clase Libro
        librosNuevos.forEach(obj => {
            const nuevoLibroFetch = new Libro(obj.titulo, obj.autor, obj.isbn, obj.anio, obj.prestamos);
            biblioteca.push(nuevoLibroFetch);
        });
        
        listarLibros();
        alert("Libros importados con éxito.");

    } catch (error) {
        // Si hay algún fallo, lo capturo aquí
        console.error("Error al importar:", error);
        alert("Hubo un error al intentar importar los libros.");
    }
};

btnFetch.addEventListener("click", cargarLibrosExternos);

// ---------------------------------------------------------
// INICIO DE LA APP
// ---------------------------------------------------------
// Pinto la lista por primera vez al cargar la página
listarLibros();
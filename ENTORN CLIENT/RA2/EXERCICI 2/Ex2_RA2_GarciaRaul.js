// 1. Declaració de funcions
// 1.1 saludar() que retorni "Hola, món!".
function saludar() {
  return "Hola, món!";
}

// 1.2 Funció que rep dos números i retorna el producte.
function producte(a, b) {
  return a * b;
}

// 1.3 Assignar una funció a una variable.
const f = function (x) {
  return x * 2;
};

// 2. Àmbit de variables i funcions
// 2.1 Diferències bàsiques entre var, let i const.
var x = 1;
let y = 2;
const z = 3;

if (true) {
  var a = 10;
  let b = 20;
  const c = 30;
}
console.log(a);

// 2.2 Exemple amb var i let.
for (var i = 0; i < 3; i++) {
}
console.log(i);

for (let j = 0; j < 3; j++) {
}
console.log(j);

// 3. Invocacions
// 3.1 Funció normal, mètode, call i apply.
function suma(a, b) {
  return a + b;
}

suma(2, 3);

const obj = {
  a: 2,
  b: 3,
  suma: function () {
    return this.a + this.b;
  }
};

obj.suma();
suma.call(null, 2, 3);
suma.apply(null, [2, 3]);

// 3.2 this i call().
function mostrarNom() {
  console.log(this.nom);
}

const persona = { nom: "Anna" };
mostrarNom.call(persona);

// 4. Memorització
// 4.1 esPrimer(n) amb memòria interna.
function esPrimer() {
  const cache = {};

  return function (n) {
    if (cache[n] !== undefined) return cache[n];

    if (n < 2) {
      cache[n] = false;
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        cache[n] = false;
        return false;
      }
    }
    cache[n] = true;
    return true;
  };
}

const comprovarPrimer = esPrimer();

// 5. Sobrecàrrega de funcions
// 5.1 calcul() segons arguments.length.
function calcul() {
  if (arguments.length === 1) {
    return arguments[0] * 2;
  } else if (arguments.length === 2) {
    return arguments[0] + arguments[1];
  } else {
    return null;
  }
}

// 5.2 afegirMetode().
function afegirMetode(obj2, nom, funcio) {
  obj2[nom] = funcio;
}

const calculadora = {};
afegirMetode(calculadora, "sumar", function (a, b) {
  return a + b;
});
afegirMetode(calculadora, "multiplicar", function (a, b) {
  return a * b;
});

calculadora.sumar(2, 3);
calculadora.multiplicar(2, 3);

// 6. Clausures
// 6.1 contador().
function contador() {
  let n = 0;
  return function () {
    n++;
    return n;
  };
}

const incrementar = contador();
incrementar();
incrementar();

// 7. Funcions sense nom
// 7.1 Tres exemples senzills.
setTimeout(function () {
  console.log("Hola");
}, 1000);

const f1 = function () {
  return 42;
};

(function () {
  console.log("IIFE");
})();

// 8. Funcions de fletxa
// 8.1 Converteix a fletxa.
function doble(x) {
  return x * 2;
}
const dobleFletxa = (x) => x * 2;

const obj2 = {
  x: 10,
  getX: function () {
    return this.x;
  }
};

const getXFletxa = () => obj2.x;

// 8.2 this en funcions de fletxa.
const obj3 = {
  x: 5,
  normal: function () {
    return this.x;
  },
  fletxa: () => {
    return this.x;
  }
};

// 9. Funcions immediates
// 9.1 IIFE bàsica.
(function () {
  console.log("Sóc una IIFE");
})();

// 9.2 IIFE amb n privat.
const modulContador = (function () {
  let n = 0;
  return {
    incrementa() {
      n++;
      return n;
    },
    valor() {
      return n;
    }
  };
})();

modulContador.incrementa();
modulContador.valor();

// 10. Altres maneres de crear funcions
// 10.1 Funció dins un objecte.
const usuari = {
  nom: "Joan",
  saluda() {
    console.log("Hola " + this.nom);
  }
};

usuari.saluda();

// 10.2 Funció que retorna una altra funció.
function crearSalutacio(prefix) {
  return function (nom) {
    return prefix + " " + nom;
  };
}

const hola = crearSalutacio("Hola");
hola("Maria");

// 11. Desestructuració
// 11.1 Objecte.
const persona2 = { nom: "Anna", edat: 25, ciutat: "Barcelona" };
const { nom, edat } = persona2;

// 11.2 Array.
const coords = [10, 20, 30];
const [x1, y1, z1] = coords;

// 12. Propagació i retorn múltiple
// 12.1 Retorn múltiple + desestructuració.
function calcularPosicio() {
  return [10, 20, 30];
}

const [x2, y2, z2] = calcularPosicio();

// 12.2 Spread i rest + 12.3 suma indefinida.
const nums = [1, 2, 3];
Math.max(...nums);

function restaExemple(primer, ...rest) {
  return rest;
}

restaExemple(1, 2, 3, 4);

function sumaIndefinida(...nums2) {
  return nums2.reduce((acc, n) => acc + n, 0);
}

sumaIndefinida(1, 2, 3, 4);

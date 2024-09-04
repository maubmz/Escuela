
let genericVariable = "Dame tu ";
let datos = [" edad", " peso", " estatura", " nombre", " masa corporal", " cuenta de github"];
let arregloDatos = [];
let lista;
let li

function pedir() {
    if (arregloDatos.length != 0) {
        arregloDatos = [];
    }
    for (let i = 0; i < 6; i++) {
        arregloDatos.push(prompt(genericVariable + datos[i]));
    }
    console.log(arregloDatos)

    // Insertar los datos en el HTML
    lista = document.getElementById("datos-lista");
    arregloDatos.forEach(function(dato) {
        li = document.createElement("li");
        li.textContent = dato;
        lista.appendChild(li);
    });

}

function borrarDatos() {
    lista = document.getElementById("datos-lista");
    lista.innerHTML = ""; // Eliminará todos los elementos <li> dentro de <ul>
}
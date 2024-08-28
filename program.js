
genericVariable = "Dame tu ";
let datos = [" edad", " peso", " estatura", " nombre", " masa corporal", " cuenta de github"];
let arregloDatos = [];


for (var i = 0; i < 6; i++) {
    arregloDatos.push(prompt(genericVariable + datos[i]));
}
console.log(arregloDatos)

// Insertar los datos en el HTML
let lista = document.getElementById("datos-lista");
arregloDatos.forEach(function(dato) {
    let li = document.createElement("li");
    li.textContent = dato;
    lista.appendChild(li);
});

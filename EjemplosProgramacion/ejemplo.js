

const arregloX = ['x', 'x', 'x', 'x'];

// Imprime la columna de 4 "X"
function columnaX() {
    let columna = "";
    arregloX.forEach((elemento) => columna += elemento+"\n");
    console.log(columna)
}

// Imprime la fila de 4 "X"
function filaX() {
    let var1 = "";
    arregloX.forEach((elemento) => var1 += elemento)
    console.log(var1)
}

// Imprime la fila y columna de una valor que da el usuario
function filaColumnaX() {
    let valorN = parseInt(prompt("Cuanto quieres la fila/columna X? "));
    let fila = "";
    let columna = "";
    for(let i = 0; i < valorN; i++) {
        fila += "x";
        columna += "x\n";
    }
    console.log(fila)
    console.log(columna)
}

function tablaX() {
    variableX = "x";
    varTabla = "";
    for(let i = 0; i < 4; i++) {
        for(let j = 0; j < 4; j++) {
            varTabla += variableX;
        }
        varTabla += "\n";
    }
    console.log(varTabla);
}

function tablasMultiplicar() {
    let tablaMultiplicar = "";
    for(let  i = 1; i <= 10; i ++) {
        for(let j = 1; j <= 10; j++) {
            tablaMultiplicar += `${i} x ${j} = ${(i*j)} \n`
        }
        console.log(tablaMultiplicar);
        tablaMultiplicar = "";
    }
}


console.log("Columna de x");
columnaX();
console.log("Fila de x");
filaX();
console.log("Fila/Columna de X");
filaColumnaX();
console.log("Tabla de 'X'");
tablaX();
console.log("Tablas de multiplicar del 1 al 10");
tablasMultiplicar();
console.log("Termino")

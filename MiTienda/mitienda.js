// Arreglo para almacenar los productos en el carrito
let carrito = [];

// Productos disponibles
let camisa = { nombre: "Camisa", precio: 300 };
let pantalon = { nombre: "Pantalón", precio: 500 };
let zapatos = { nombre: "Zapatos", precio: 800 };
let sombrero = { nombre: "Sombrero", precio: 200 };

// Función que agrega productos al carrito
function agregarCarrito() {
    let continuar = true; // Bandera para continuar o salir del bucle
    
    while (continuar) {
        // Mostrar el mensaje del prompt
        let respuesta = prompt(`Seleccione un producto para agregar al carrito:
            1. ${camisa.nombre} - $${camisa.precio}
            2. ${pantalon.nombre} - $${pantalon.precio}
            3. ${zapatos.nombre} - $${zapatos.precio}
            4. ${sombrero.nombre} - $${sombrero.precio}
            5. Ver Carrito y Total
            6. Salir`);

        let respuestaNum = parseInt(respuesta);
        switch (respuestaNum) {
            case 1:
                carrito.push(camisa);
                console.log("Agregaste una Camisa al carrito.");
                break;
            case 2:
                carrito.push(pantalon);
                console.log("Agregaste un Pantalón al carrito.");
                break;
            case 3:
                carrito.push(zapatos);
                console.log("Agregaste unos Zapatos al carrito.");
                break;
            case 4:
                carrito.push(sombrero);
                console.log("Agregaste un Sombrero al carrito.");
                break;
            case 5:
                mostrarCarrito();
                break;
            case 6:
                console.log("Saliendo del programa...");
                continuar = false; // Cambiar la bandera para romper el bucle
                break;
            default:
                console.log("Opción no válida, por favor intenta de nuevo.");
        }
    }
}

// Función para mostrar el carrito
function mostrarCarrito() {
    if (carrito.length === 0) {
        console.log("El carrito está vacío.");
    } else {
        console.log("Productos en el carrito:");
        carrito.forEach(producto => {
            console.log(`${producto.nombre} - $${producto.precio}`);
        });
    }
}

// Llamar a la función para comenzar el proceso
agregarCarrito();

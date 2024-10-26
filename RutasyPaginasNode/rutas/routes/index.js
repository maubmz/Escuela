const express = require("express");
const path = require("path"); // Asegúrate de requerir 'path' para usarlo en las rutas
const app = express();
const port = 3099;

// Middleware para servir archivos estáticos (CSS, JS, imágenes, etc.)
app.use(express.static(path.join(__dirname, '../../paginas'))); // Cambia la ruta según tu estructura de carpetas

// Definición de las rutas y los manejadores
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/index.html')); 
});

app.get("/quien-soy", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/about/index.html')); 
});

app.get("/contacto", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/contact/index.html')); 
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor en escucha desde http://localhost:${port}`);
});

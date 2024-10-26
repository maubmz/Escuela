const express = require("express");
const path = require("path"); // Asegúrate de requerir 'path' para usarlo en las rutas
const app = express();
const port = 3099;

// Definición de las rutas y los manejadores
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/index.html')); // Envía welcome.html
});

app.get("/quien-soy", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/about.html')); // Envía about.html
});

app.get("/contacto", (req, res) => {
    res.sendFile(path.join(__dirname, '../../paginas/contact.html')); // Envía contact.html
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor en escucha desde http://localhost:${port}`);
});

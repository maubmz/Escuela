const express = require("express");
const path = require("path");
const app = express();
const port = 3100;

// Servir archivos estáticos
app.use(express.static(path.join(__dirname, '../../Paginas')));

// Definición de las rutas y los manejadores
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '../../Paginas/index.html')); 
});

app.get("/qr", (req, res) => {
    res.sendFile(path.join(__dirname, '../../Paginas/qr/index.html')); 
});

app.get("/calculadora", (req, res) => {
    res.sendFile(path.join(__dirname, '../../Paginas/calculadora/index.html')); 
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor en escucha desde http://localhost:${port}`);
});

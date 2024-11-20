const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const { hostname } = require('os');

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));

// Configuración para servir archivos estáticos (CSS, JS, imágenes)
app.use(express.static('public'));  // Esto hará que los archivos en 'public' sean accesibles

// Motor de plantillas para HTML de forma dinámica
app.set('view engine', 'ejs');

// Credenciales para DB
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'M1x_2021',
    database: 'node_crud',
    port: '3306'
});

// Conexión a la DB
db.connect(err => {
    if (err) {
        console.log(`Error al momento de hacer conexión: ${err}`);
    } else {
        console.log('Conexión realizada correctamente');
    }
});

/* Puerto */
const port = 3036;
const hostName = '192.168.1.75';
// Server inicio
app.listen(port, hostName, () => {
    console.log(`El servidor está escuchando en http://${hostName}:${port}`);
});

// Mostrar lista de usuarios
app.get('/', (req, res) => {
    const query = 'SELECT * FROM users';
    db.query(query, (err, results) => {
        if (err) {
            console.error(`Error al recuperar datos: ${err}`);
            res.send('Error al recuperar datos');
        } else {
            res.render('index', { users: results });
        }
    });
});

// Ruta para mostrar formulario de creación
app.get('/crear', (req, res) => {
    res.render('crear'); // Renderiza el archivo crear.ejs
});

// Agregar usuario
app.post('/add', (req, res) => {
    console.log('Contenido de req.body:', req.body); // Depuración

    const { nombre, email } = req.body;

    if (!nombre || !email) {
        console.error('Nombre o correo faltan en el cuerpo de la solicitud.');
        return res.send('Nombre y correo son obligatorios');
    }

    const query = 'INSERT INTO users (nombre, email) VALUES (?, ?)';
    db.query(query, [nombre, email], (err) => {
        if (err) {
            console.error(`Error al insertar usuarios: ${err}`);
            res.send('Error al insertar usuario');
        } else {
            res.redirect('/');
        }
    });
});

// Actualizar usuario Editar usuario
app.get('/edit/:id', (req, res) => {
    const { id } = req.params; // Obtener el ID del usuario desde la URL
    const query = 'SELECT * FROM users WHERE id = ?'; // Query para obtener los datos del usuario
    db.query(query, [id], (err, results) => {
        if (err) {
            console.error('Error al recuperar datos del usuario para editar:', err);
            res.send('Error en la base de datos');
        } else {
            // Renderiza el formulario de edición con los datos del usuario
            res.render('edit', { user: results[0] });
        }
    });
});

// Actualizar usuario
app.post('/update/:id', (req, res) => {
    const { id } = req.params; // Obtiene el ID desde la URL
    const { nombre, email } = req.body; // Obtiene los datos del formulario

    // Verificar si los datos requeridos están presentes
    if (!nombre || !email) {
        return res.send('Nombre y correo son obligatorios');
    }

    const query = 'UPDATE users SET nombre = ?, email = ? WHERE id = ?';
    db.query(query, [nombre, email, id], (err) => {
        if (err) {
            console.error('Error al actualizar usuario:', err);
            res.send('Error al actualizar usuario');
        } else {
            res.redirect('/');
        }
    });
});

// Eliminar usuario
app.get('/delete/:id', (req, res) => {
    const { id } = req.params;
    const query = 'DELETE FROM users WHERE id = ?';
    db.query(query, [id], (err) => {
        if (err) {
            console.error('Error al eliminar usuario');
            res.send('Error al eliminar usuario');
        } else {
            res.redirect('/');
        }
    });
});

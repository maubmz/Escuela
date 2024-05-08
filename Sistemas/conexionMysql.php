<?php
// Conectarse a la base de datos MySQL
$username = "root";
$password = "";
$host = "localhost";

// Crear conexión
$connection = mysqli_connect($host, $username, $password);

$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];

if(!$connection) {
    echo "No se pudo establecer la conexion";
} else {
    echo "<b><h3>Hemos conectado al servidor</h3></b>";
}
// Nombre base de datos
$database = "cadena_tiendas";
// Indicamos seleccionar a la base de datos
$db = mysqli_select_db($connection, $database);

if(!$database) {
    echo "No se ha podido encontrar la Tabla";
} else {
    echo "<h3>Tabla Seleccionada</h3>";
}
// Buscamos los datos de los registros por medio de nombre y apellido
$query_sql = "SELECT t.NombreTienda, t.PaisTienda, c.nombre, c.apellidos
    FROM tienda t, cliente c, tienda_cliente a
    WHERE a.id_tienda1 = t.id_tienda
    AND a.id_cliente1 = c.id_cliente
    AND c.nombre = '$nombre'
    AND c.apellidos = '$apellido';";

$resultado = mysqli_query($connection, $query_sql);
if(!$resultado) {
    echo "No se pudo realizar la consulta";
} else {
    echo "<style>
        /* Estilos para la tabla */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
            font-size: 18px;
        }

        /* Estilos para los encabezados */
        h1, h2, h3 {
            font-family: Arial, sans-serif;
            color: #333;
        }

        h1 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        h2 {
            font-size: 20px;
            margin-bottom: 5px;
        }

        h3 {
            font-size: 18px;
            margin-bottom: 5px;
        }

        /* Estilos para los enlaces */
        a {
            color: blue;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>";

    echo "<table>";
    echo "<tr>";
    echo "<th><h1>Nombre Tienda</h1></th>";
    echo "<th><h1>Pais Tienda</h1></th>";
    // echo "<th><h1>Nombre</h1></th>";
    // echo "<th><h1>Apellidos</h1></th>";
    echo "</tr>";
}


while ($colum = mysqli_fetch_array($resultado)) {
    echo "<tr>";
    echo "<td><h2>" .$colum['NombreTienda'].  "</h2></td>";
    echo "<td><h2>" .$colum['PaisTienda']. "</h2></td>";
    // echo "<td><h2>" .$colum['nombre']. "</h2></td>";
    // echo "<td><h2>" .$colum['apellidos']. "</h2></td>";
    echo "</tr>";
}
echo "</table>";


mysqli_close( $connection);

echo '<a href="index.html">Volver Atras</a>';
?>

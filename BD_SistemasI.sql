CREATE DATABASE cadena_tiendas;

USE cadena_tiendas;

CREATE TABLE cliente(
	id_cliente INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Nombre VARCHAR(20) NOT NULL,
	Apellidos VARCHAR(20) NOT NULL
);

CREATE TABLE tienda(
	id_tienda INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	NombreTienda VARCHAR(20) NOT NULL,
	PaisTienda VARCHAR(20) NOT NULL
);

CREATE TABLE tienda_cliente(
	id_tienda1 INTEGER NOT NULL,
	id_cliente1 INTEGER NOT NULL,
	
	FOREIGN KEY (id_tienda1) REFERENCES tienda(id_tienda),
	FOREIGN KEY (id_cliente1) REFERENCES cliente(id_cliente)
);


INSERT INTO cliente(Nombre, Apellidos) VALUES ("Mauricio", "Baeza");
INSERT INTO cliente(Nombre, Apellidos) VALUES ("Brau", "Dominguez");
INSERT INTO cliente(Nombre, Apellidos) VALUES ("Tyson", "Ngo");

INSERT INTO tienda(NombreTienda, PaisTienda) VALUES ("Nike NY", "US, New York");
INSERT INTO tienda(NombreTienda, PaisTienda) VALUES ("Nike N", "Mexico, CDMX");

INSERT INTO tienda_cliente(id_tienda1, id_cliente1) VALUES (1, 1);
INSERT INTO tienda_cliente(id_tienda1, id_cliente1) VALUES (1, 3);
INSERT INTO tienda_cliente(id_tienda1, id_cliente1) VALUES (2, 1);
INSERT INTO tienda_cliente(id_tienda1, id_cliente1) VALUES (2, 2);

SELECT * FROM cliente;
SELECT * FROM tienda;
SELECT * FROM tienda_cliente;

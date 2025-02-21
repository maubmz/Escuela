package mx.unam.aragon.modelo.bd;

import mx.unam.aragon.modelo.Conexion;

public class MariaDB implements Conexion {
    @Override
    public void consultar(String consulta) {
        System.out.println("Consulta a MariaDB");
    }

    @Override
    public void conectar(String bd) {
        System.out.println("Conexion a MariaDB");
    }
}

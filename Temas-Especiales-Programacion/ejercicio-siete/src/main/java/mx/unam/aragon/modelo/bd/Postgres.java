package mx.unam.aragon.modelo.bd;

import mx.unam.aragon.modelo.Conexion;

public class Postgres implements Conexion {
    @Override
    public void conectar(String bd) {
        System.out.println("Conexion a Postgres");
    }

    @Override
    public void consultar(String consulta) {
        System.out.println("Consula a Postgres");
    }
}

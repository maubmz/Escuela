package mx.unam.aragon.modelo.bd;

import mx.unam.aragon.modelo.Conexion;

public class Oracle implements Conexion {
    @Override
    public void conectar(String bd) {
        System.out.println("Conexion a Oracle");
    }

    @Override
    public void consultar(String consulta) {
        System.out.println("Consulta a Oracle");
    }
}

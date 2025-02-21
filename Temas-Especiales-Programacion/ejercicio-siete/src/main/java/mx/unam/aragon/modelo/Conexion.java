package mx.unam.aragon.modelo;

public interface Conexion {
    public void conectar(String nombreBd);
    public void consultar(String consulta);
}

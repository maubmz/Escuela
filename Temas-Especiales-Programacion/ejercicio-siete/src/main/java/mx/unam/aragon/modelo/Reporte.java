package mx.unam.aragon.modelo;


import java.util.Collection;

public class Reporte {
    private Conexion conexion;
    private Formato formato;
    private Collection<DatoReporte> datosReporte;

    public Formato getFormato() {
        return formato;
    }

    public void setFormato(Formato formato) {
        this.formato = formato;
    }

    public Conexion getConexion() {
        return conexion;
    }

    public void setConexion(Conexion conexion) {
        this.conexion = conexion;
    }

    public Collection<DatoReporte> getDatosReporte() {
        return datosReporte;
    }

    public void setDatosReporte(Collection<DatoReporte> datosReporte) {
        this.datosReporte = datosReporte;
    }

    @Override
    public String toString() {
        return "Reporte[ " +
                "conexion a: " + this.getConexion() +
                ", formato: " + this.getFormato() + "]";
    }
}

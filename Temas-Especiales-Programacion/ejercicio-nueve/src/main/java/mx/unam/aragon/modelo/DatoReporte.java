package mx.unam.aragon.modelo;

public class DatoReporte {
    private String idVenta;
    private String fechaVenta;

    public DatoReporte(String idVenta, String fechaVenta) {
        this.idVenta = idVenta;
        this.fechaVenta = fechaVenta;
    }

    @Override
    public String toString() {
        return "DatoReporte [" +
                "idVenta: " + idVenta +
                ", fechaVenta: " + fechaVenta + "]";
    }
}

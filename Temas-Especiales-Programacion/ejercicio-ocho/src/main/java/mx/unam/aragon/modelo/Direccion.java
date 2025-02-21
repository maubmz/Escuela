package mx.unam.aragon.modelo;

public class Direccion {
    private String calle;
    private String numero;

    public Direccion() {
    }

    public String getCalle() {
        return calle;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    @Override
    public String toString() {
        return "Direccion { " +
                "calle = " + calle +
                ", numero = " + numero +
                " } ";
    }
}

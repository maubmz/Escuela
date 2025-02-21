package mx.unam.aragon.modelo;

public class Persona {
    private String nombre;
    private Integer edad;
    private Direccion direccion;

    public Persona() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public Direccion getDireccion() {
        return direccion;
    }

    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }

    @Override
    public String toString() {
        return "Persona { " +
                "nombre : " + nombre +
                "edad : " + edad +
                "direccion : " + direccion.toString();
    }
}

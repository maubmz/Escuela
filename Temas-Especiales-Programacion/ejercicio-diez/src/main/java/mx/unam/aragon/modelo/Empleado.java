package mx.unam.aragon.modelo;

public class Empleado {
    private String nombre;
    private Integer edad;
    private Actividades actividad;


    public Empleado(String nombre, Integer edad, Actividades actividad) {
        this.nombre = nombre;
        this.edad = edad;
        this.actividad = actividad;
    }

    public Actividades getActividad() {
        return actividad;
    }

    public void setActividad(Actividades actividades) {
        this.actividad = actividad;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Empleado [nombre=" + nombre + ", edad=" + edad + " ]";
    }
}

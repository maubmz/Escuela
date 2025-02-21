package mx.unam.aragon.modelo;
public class Estudiante {
    private String nombre;
    private Integer edad;
    private Actividades actividad;
    public Estudiante() {
    }
    public Estudiante(Actividades actividad) {
        this.actividad = actividad;
    }
    public Estudiante(String nombre) {
        this.nombre = nombre;
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
    @Override
    public String toString() {
        return "Empleado [nombre=" + nombre + ", edad=" + edad + "]";
    }
}
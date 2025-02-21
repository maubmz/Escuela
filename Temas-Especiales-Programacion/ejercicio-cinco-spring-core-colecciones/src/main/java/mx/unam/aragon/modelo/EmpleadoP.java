package mx.unam.aragon.modelo;

import java.util.Properties;

public class EmpleadoP {
    private String nombre;
    private Integer edad;
    private Properties actividad;
    public EmpleadoP() {
    }
    public EmpleadoP(String nombre) {
        super();
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
    public Properties getActividad() {
        return actividad;
    }
    public void setActividad(Properties actividad) {
        this.actividad = actividad;
    }
    @Override
    public String toString() {
        return "Empleado [nombre=" + nombre + ", edad=" + edad + "]";
    }
}

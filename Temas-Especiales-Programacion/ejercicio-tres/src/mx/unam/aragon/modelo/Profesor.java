package mx.unam.aragon.modelo;

import java.util.ArrayList;

public class Profesor {

    private String nombre;
    private ArrayList<Responsabilidades> responsabilidad = new ArrayList<>();

    public Profesor() {
    }

    public ArrayList<Responsabilidades> getResponsabilidad() {
        return responsabilidad;
    }

    public void setResponsabilidad(ArrayList<Responsabilidades> responsabilidad) {
        this.responsabilidad = responsabilidad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}

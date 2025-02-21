package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.Profesor;
import mx.unam.aragon.modelo.Responsabilidades;

public class MetodoUno {
    public static void main(String[] args) {

        Profesor profesor = new Profesor();
        Responsabilidades resp = new Responsabilidades();

        profesor.setNombre("Jorge");
        profesor.setResponsabilidad(resp);


    }
}

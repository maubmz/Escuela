package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.*;

public class MetodoTres {
    public static void main(String[] args) {
        Profesor profesor = new Profesor();
        profesor.setNombre("Pedro");
        ExplicarClases exp = new ExplicarClases();
        Calificar cal = new Calificar();
        Reportes rep = new Reportes();

        profesor.getResponsabilidad().add(exp);
        profesor.getResponsabilidad().add(cal);
        profesor.getResponsabilidad().add(rep);

        System.out.println(profesor.getNombre());
        for (Responsabilidades resp : profesor.getResponsabilidad()) {
            System.out.println("---");
            resp.realizar();
        }

    }
}

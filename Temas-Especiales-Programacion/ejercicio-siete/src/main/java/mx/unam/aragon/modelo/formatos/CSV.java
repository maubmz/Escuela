package mx.unam.aragon.modelo.formatos;

import mx.unam.aragon.modelo.DatoReporte;
import mx.unam.aragon.modelo.Formato;

import java.util.Collection;

public class CSV implements Formato {

    @Override
    public void generarReporte(Collection<DatoReporte> datos) {
        for (DatoReporte dato : datos) {
            System.out.println(dato);
        }
    }
}

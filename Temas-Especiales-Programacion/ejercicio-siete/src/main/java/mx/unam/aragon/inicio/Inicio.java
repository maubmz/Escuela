package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.DatoReporte;
import mx.unam.aragon.modelo.Reporte;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class Inicio {
    public static void main(String[] args) {
        ApplicationContext contexto = new ClassPathXmlApplicationContext(
                new String[] {"bean-configuration.xml"});
        Reporte reporte = (Reporte) contexto.getBean("reporte");
        System.out.println(reporte.toString());
        for (DatoReporte dato : reporte.getDatosReporte()) {
            System.out.println(dato.toString());;
        }

    }
}

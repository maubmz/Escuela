package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.Reporte;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class Inicio {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                new String[] {"bean-configuration.xml"});
        // Obtener dos instancias de Reporte
        Reporte reporte1 = context.getBean("reporte", Reporte.class);
        Reporte reporte2 = context.getBean("reporte", Reporte.class);

        System.out.println("HashCode de reporte1: " + reporte1.hashCode());
        System.out.println("HashCode de reporte2: " + reporte2.hashCode());

        reporte1.setNombre("ReporteElectronica");

        // Revisar si el cambio afecta a la otra instancia
        System.out.println("Conexion en reporte1: " + reporte1.getNombre());
        System.out.println("Conexion en reporte2: " + reporte2.getNombre());

    }
}

package mx.unam.aragon.inicio;
import mx.unam.aragon.config.ConfiguracionServicio;
import mx.unam.aragon.modelo.Estudiante;
import mx.unam.aragon.modelo.Materia;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Inicio {
    public static void main(String[] args) {
        ConfigurableApplicationContext contexto =

                new AnnotationConfigApplicationContext
                        (ConfiguracionServicio.class);
        Estudiante estudiante = (Estudiante) contexto.getBean("estudiante", Estudiante.class);
        Estudiante estudianteDos = (Estudiante) contexto.getBean("estudianteDos", Estudiante.class);
        Estudiante estudianteTres = (Estudiante) contexto.getBean("estudianteTres", Estudiante.class);

        System.out.println(estudiante.toString());
        System.out.println(estudianteDos.toString());
        System.out.println(estudianteTres.toString());

        //cambiar propiedad a estudianteDos
        estudianteDos.setNombre("Martha");
        System.out.println("-------");
        System.out.println(estudiante.toString());
        System.out.println(estudianteDos.toString());

        System.out.println("-------");
        Materia materia = (Materia) contexto.getBean("materia");
        Materia materiaDos = (Materia) contexto.getBean("materiaDos");
        System.out.println(materia.toString());
        System.out.println(materiaDos.toString());
    }
}
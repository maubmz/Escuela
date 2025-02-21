package mx.unam.aragon.config;
import mx.unam.aragon.modelo.Estudiante;
import mx.unam.aragon.modelo.Materia;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;
@Configuration
public class ConfiguracionServicioDos {
    @Bean(name = "estudianteTres")
    @Scope("prototype")
    public Estudiante servicioEstudiante(){
        Estudiante estudiante=new Estudiante();
        estudiante.setNombre("Miguel");
        estudiante.setEdad(46);
        return estudiante;
    }
    @Bean(name="materiaDos")
    @Scope("prototype")
    public Materia getMateria(){
        Materia materia=new Materia();
        materia.setNombre("Estructura de Datos");
        materia.setCreditos(9);
        return materia;
    }
}
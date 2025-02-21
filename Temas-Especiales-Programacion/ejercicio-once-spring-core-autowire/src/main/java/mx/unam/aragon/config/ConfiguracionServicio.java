package mx.unam.aragon.config;

import mx.unam.aragon.config.ConfiguracionServicioDos;
import mx.unam.aragon.modelo.Estudiante;
import org.springframework.context.annotation.*;
@Configuration
@ImportResource(locations = {"classpath:bean-configuration.xml",
        "classpath:bean-services.xml"})
@Import({ConfiguracionServicioDos.class})
//@ComponentScan(basePackages = "mx.unam.aragon")
public class ConfiguracionServicio {
    @Bean(name = "estudiante")
    @Scope("prototype")
    public Estudiante servicioEstudiante(){
        Estudiante estudiante=new Estudiante();
        estudiante.setNombre("Manuel");
        estudiante.setEdad(46);
        return estudiante;
    }
}
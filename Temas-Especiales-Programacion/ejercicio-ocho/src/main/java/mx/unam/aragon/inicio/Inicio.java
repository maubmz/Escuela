package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.Persona;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanDefinitionReader;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

public class Inicio {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                new String[] { "bean-configuration.xml"});
        Persona persona = context.getBean("persona", Persona.class);
        System.out.println(persona);

        Persona personaDos = context.getBean("persona", Persona.class);
        System.out.println(personaDos);

        System.out.println("---------------------");
        persona.setNombre("Rebeca");
        persona.setEdad(30);

        persona.getDireccion().setCalle("Demo");
        persona.getDireccion().setNumero("340");
        System.out.println(persona);
        System.out.println(personaDos);
        ((ClassPathXmlApplicationContext)context).close();

    }
}

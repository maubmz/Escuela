package mx.unam.aragon.inicio;

import mx.unam.aragon.modelo.Persona;
import mx.unam.aragon.servicio.Servicio;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanDefinitionReader;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

public class Inicio {
    public static void main(String[] args) {
        ApplicationContext contexto = new ClassPathXmlApplicationContext(new String[] {
                "bean-configuration.xml", "bean-services.xml"
        });
        Servicio ser = (Servicio) contexto.getBean("servicio");
        System.out.println(ser.toString());
        ((ClassPathXmlApplicationContext) contexto).close();

    }
}

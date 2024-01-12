import java.io.File;
import java.util.ArrayList;

public class Principal {
    public static void main(String[] args) {
        Hilo1 primera = new Hilo1("PrimeraClase");
        Hilo2 segunda = new Hilo2("SegundaClase");
        Hilo3 tercera = new Hilo3("TerceraClase");


        System.out.println(("Bienvenido al Titanic").toUpperCase());
        primera.start();
        segunda.start();
        tercera.start();
        try{
            primera.join();
            segunda.join();
            tercera.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("FIN DE LA TRAVESIA");
    }
}

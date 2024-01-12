import java.io.*;

public class Hilo3 extends Thread{
    File file = new File("Titanic.csv");
    int pasajeros, supervivientes, fallecidos;
    double sup,fal;

    public Hilo3(String name) {
        super(name);
        currentThread().setPriority(MIN_PRIORITY);
    }

    @Override
    public void run() {
        super.run();

        try {
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String cad;
            while((cad = br.readLine()) != null){
                String [] datos = cad.split(";");
                if(datos[0].contains("3")){
                    pasajeros++;
                    if(datos[datos.length-1].contains("S")){
                        supervivientes++;
                    }
                }
            }
            br.close();
            fr.close();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        fallecidos = pasajeros - supervivientes;
        sup = (double) (supervivientes * 100) /pasajeros;
        fal = (double) (fallecidos * 100)/pasajeros;
        System.out.println(currentThread().toString());
    }

    @Override
    public String toString() {
        return "+En Tercera clase viajaban " + pasajeros +
                " pasajeros. Sobrevivieron " + supervivientes + "(" + sup + "%)" +
                " y fallecieron " + fallecidos + "(" + fal + "%)" +
                " pasajeros.";
    }
}
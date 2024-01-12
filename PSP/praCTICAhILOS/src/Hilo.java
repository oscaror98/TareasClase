public class Hilo extends Thread {
    public Hilo(String name) {
        super(name);
    }

    @Override
    public void run() {
        super.run();
        for(int i = 0; i < 5; i++){
            System.out.println(getName()+" con valor = " + i);
        }
    }
}

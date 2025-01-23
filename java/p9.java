interface compute{
    void convert(double factor);
}

class GbtoMb implements compute{
    public void convert(double factor){
        System.out.println("GB to MB: " + factor * 1024);
    }
}
class euroToRupee implements compute{
    public void convert(double factor){
        System.out.println("Euro to Rupee: " + factor * 80);
    }
}
public class p8{
    public static void main(string[] args){
        compute c = new GbtoMb();
        c.convert(2);
        c = new euroToRupee();
        c.convert(2);
    }
}

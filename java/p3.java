import java.util.*;
class complex{
    private int real;
    private int imag;

    public complex(int real, int imag){
        this.real = real;
        this.imag = imag;
    }

    public void display(){
        System.out.println(this.real + " + " + this.imag + "i");
    }

    public void add(complex c2){
        this.real += c2.real;
        this.imag += c2.imag;
        this.display();
    }
    public void subtract(complex c2){
        this.real -= c2.real;
        this.imag -= c2.imag;
        this.display();
    }
    public boolean isEqual(complex c2){
        return this.real == c2.real && this.imag == c2.imag;
    }
}

public class p3{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter real and imaginary part of first complex number");
        int real1 = sc.nextInt();
        int imag1 = sc.nextInt();
        complex c1 = new complex(real1, imag1);
        System.out.println("Enter real and imaginary part of second complex number");
        int real2 = sc.nextInt();
        int imag2 = sc.nextInt();
        complex c2 = new complex(real2, imag2);
        System.out.println("Enter 1 to add, 2 to subtract, 3 to check equality");
        int choice = sc.nextInt();
        switch(choice){
            case 1:
                c1.add(c2);
                break;
            case 2:
                c1.subtract(c2);
                break;
            case 3:
                if(c1.isEqual(c2)){
                    System.out.println("Both complex numbers are equal");
                }
                else{
                    System.out.println("Both complex numbers are not equal");
                }
                break;
            default:
                System.out.println("Invalid choice");
        }
        sc.close();
    }
}

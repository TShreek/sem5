import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            // Read numerator
            System.out.print("Enter a positive numerator: ");
            int numerator = sc.nextInt();
            if (numerator < 0) {
                throw new IllegalArgumentException("Numerator cannot be negative.");
            }

            // Read denominator
            System.out.print("Enter a positive non-zero denominator: ");
            int denominator = sc.nextInt();
            if (denominator <= 0) {
                throw new ArithmeticException(denominator == 0 
                    ? "Denominator cannot be zero." 
                    : "Denominator cannot be negative.");
            }

            // Perform division
            double result = (double) numerator / denominator;
            System.out.println("Result: " + result);

        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            sc.close();
        }
    }
}

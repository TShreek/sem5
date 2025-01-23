import java.util.*;

// Abstract base class
abstract class Bank {
    protected String accName;
    protected int accNo;
    protected double balance;

    // Constructor
    public Bank(String accName, int accNo, double balance) {
        this.accName = accName;
        this.accNo = accNo;
        this.balance = balance;
    }

    // Method to display account details
    public void display() {
        System.out.println("Account Name: " + accName);
        System.out.println("Account Number: " + accNo);
        System.out.println("Balance: " + balance);
    }

    // Abstract method for displaying interest
    public abstract void displayInterest();
}

// Derived class for CityBank
class CityBank extends Bank {
    public CityBank(String accName, int accNo, double balance) {
        super(accName, accNo, balance);
    }

    @Override
    public void displayInterest() {
        double interest = balance * 0.06;
        System.out.println("City Bank Interest: " + interest);
    }
}

// Derived class for SBI
class Sbi extends Bank {
    public Sbi(String accName, int accNo, double balance) {
        super(accName, accNo, balance);
    }

    @Override
    public void displayInterest() {
        double interest = balance * 0.12;
        System.out.println("SBI Bank Interest: " + interest);
    }
}

// Main class
public class BankApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input account details
        System.out.println("Enter account name:");
        String accName = sc.nextLine();
        System.out.println("Enter account number:");
        int accNo = sc.nextInt();
        System.out.println("Enter balance:");
        double balance = sc.nextDouble();

        // Choose bank
        System.out.println("Enter 1 for City Bank or 2 for SBI:");
        int choice = sc.nextInt();

        // Create appropriate bank object
        Bank bank = null;
        if (choice == 1) {
            bank = new CityBank(accName, accNo, balance);
        } else if (choice == 2) {
            bank = new Sbi(accName, accNo, balance);
        } else {
            System.out.println("Invalid choice. Exiting program.");
            sc.close();
            return;
        }

        // Display details and interest
        bank.display();
        bank.displayInterest();

        sc.close();
    }
}

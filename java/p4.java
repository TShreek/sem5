import java.util.Scanner;

class Person {
    private String name, gender;
    private int age;

    public void readDetails(Scanner sc) {
        System.out.print("Enter Name: ");
        name = sc.nextLine();
        System.out.print("Enter Gender: ");
        gender = sc.nextLine();
        System.out.print("Enter Age: ");
        age = sc.nextInt();
        sc.nextLine(); // Consume the newline
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Gender: " + gender);
        System.out.println("Age: " + age);
    }
}

class Employee extends Person {
    private int empid;
    private String dept;

    public void readDetails(Scanner sc) {
        super.readDetails(sc);
        System.out.print("Enter Employee ID: ");
        empid = sc.nextInt();
        sc.nextLine(); // Consume the newline
        System.out.print("Enter Department: ");
        dept = sc.nextLine();
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("Employee ID: " + empid);
        System.out.println("Department: " + dept);
    }
}

class Student extends Person {
    private int USN;
    private String branch;

    public void readDetails(Scanner sc) {
        super.readDetails(sc);
        System.out.print("Enter USN: ");
        USN = sc.nextInt();
        sc.nextLine(); // Consume the newline
        System.out.print("Enter Branch: ");
        branch = sc.nextLine();
    }

    public void displayDetails() {
        super.displayDetails();
        System.out.println("USN: " + USN);
        System.out.println("Branch: " + branch);
    }
}

public class p4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Employee[] emp = new Employee[2];
        Student[] stu = new Student[2];

        // Reading Student Details
        for (int i = 0; i < 2; i++) {
            System.out.println("\nDetails of Student " + (i + 1) + ":");
            stu[i] = new Student();
            stu[i].readDetails(sc);
        }

        // Reading Employee Details
        for (int i = 0; i < 2; i++) {
            System.out.println("\nDetails of Employee " + (i + 1) + ":");
            emp[i] = new Employee();
            emp[i].readDetails(sc);
        }

        // Displaying Employee Details
        System.out.println("\nEmployee Details:");
        for (int i = 0; i < 2; i++) {
            System.out.println("\nDetails of Employee " + (i + 1) + ":");
            emp[i].displayDetails();
        }

        // Displaying Student Details
        System.out.println("\nStudent Details:");
        for (int i = 0; i < 2; i++) {
            System.out.println("\nDetails of Student " + (i + 1) + ":");
            stu[i].displayDetails();
        }

        sc.close();
    }
}


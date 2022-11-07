import java.util.Scanner;

public class phoneBook {
    public static void main(String[] args) {
        int choice;
        Scanner in = new Scanner(System.in);
        do{
        System.out.println("1. Add Contact");
        System.out.println("2. Update Contact");
        System.out.println("3. Delete Contact");
        System.out.println("4. Update Contact");
        System.out.println("Enter Number 1-4");
        choice = in.nextInt();
        switch (choice){
            case 1: System.out.println("Contact Added");
            break;
            case 2: System.out.println("Contact Updated");
            break;
            case 3: System.out.println("Contact Deleted");
            break;
            case 4: System.out.println("Contact Updated");
            break;
            default: System.out.println("Error: invalid choice");
        }
        
    }while(choice !=4);

    }
    
}

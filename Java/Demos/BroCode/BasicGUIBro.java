// Simple GUI

import javax.swing.JOptionPane;

/**
 * JOptionPane is a class library that makes it easy to pop up a
 * simple dialog box that either provides an information message
 * or asks for a simple input from the user.
 */

public class BasicGUIBro {

    // GUI: Graphical User Interface.

    public static void main(String[] args) {

        String name = JOptionPane.showInputDialog("Enter a name");
        // * showInputDialog: Shows a GUI dialog requesting input from the user.

        JOptionPane.showMessageDialog(null, "Hello, " + name);
        // * showMessageDialog: Shows a GUI dialog message.

        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter age"));
        // ! an int variable cannot return a string value (without a parseInt function).
        // * The parseInt function will convert the string an to integer.

        JOptionPane.showMessageDialog(null, "You are " + age + " years old.");

        double height = Double.parseDouble(JOptionPane.showInputDialog("Enter height in inches"));
        JOptionPane.showMessageDialog(null, "You are " + height + " inches tall");
    }
}

// * Java GUI intro
// https://www.youtube.com/watch?v=rWCnZKF-U3Q&list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1&index=6
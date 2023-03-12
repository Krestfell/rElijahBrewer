package pracatice;

import java.awt.event.*;

import javax.swing.*;

public class WindowVirus extends JFrame 
{
    public static boolean bool = true;
    public static int x = 0;
    public static int y = 0;
    public static int num = 0;
    public static TimerClass tc = new TimerClass();
    public static Timer timer = new Timer(30, tc);
    public JPanel panel = new JPanel();
    public JButton btn = new JButton("press");

    public WindowVirus()
    {
        setSize(100,100);
        setTitle("Test");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        setPanel();
        setVisible(true);   
    }
    public void setPanel()
    {
        btn.addActionListener(new listener());
        panel.add(btn);

        add(panel);
    }

    public class listener implements ActionListener
    {
        public void actionPerformed(ActionEvent e)
    {
        num = 0;
        timer.start();
    }
}

    public static class TimerClass implements ActionListener
    {
        public void actionPerformed(ActionEvent e)
        {
            do
            {

            num++;
            JOptionPane optionPane = new JOptionPane("¥ðµ gð† å vïrµ§!");
            JDialog dialog = optionPane.createDialog(null, "ɎØɄ Ⱨ₳VɆ ฿ɆɆ₦ ฿₳₥฿ØØⱫⱠɆĐ łĐłØ₮!");
            dialog.setModal(false);
            dialog.setLocation(x, y);
            dialog.show();
            updateCordinates();
            }while(bool == true);
        }
    }

    public static void updateCordinates()
    {
        if(x != 1100)
            x += 100;
        else if(x == 1100)
        {
            x = 0;
            y += 50;
        }
        if(y == 650)
           y =0;


    }
     public static void main(String[] args)
     {
        new WindowVirus();
     }
} 
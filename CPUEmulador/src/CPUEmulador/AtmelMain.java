/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador;

import static CPUEmulador.AtmelMain.ats;
import CPUEmulador.CPU.CPU;
import CPUEmulador.CPU.Instruction;
import CPUEmulador.CPU.Translator;
import CPUEmulador.Memory.Information;
import CPUEmulador.Memory.RAM;
import CPUEmulador.Visual.MainScreen;
import java.util.function.Function;

/**
 *
 * @author Kai
 */
public class AtmelMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        
        Computer pc = new Computer(
                "//Fatorial variável\n"
                + "// N que vai usar;\n"
                + "SET 6\n"
                + "STO 20\n"
                + "// N decremento;\n"
                + "SET 1\n"
                + "STO 21\n"
                + "// N atual;\n"
                + "STO 22\n"
                + "//loop;\n"
                + "LDD 20\n"
                + "CGT 21\n"
                + "JPC 32\n"
                + "LDD 20\n"
                + "MLT 22\n"
                + "STO 22\n"
                + "LDD 20\n"
                + "SUB 21\n"
                + "STO 20\n"
                + "JMP 5");
        MainScreen screen = new MainScreen();
        screen.setVisible(true);
        screen.setComputer(pc);
    }

    public static <T> String ats(T[] value)
    {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < value.length; ++i)
        {
            if (i != 0)
            {
                sb.append(", ");
            }

            sb.append(value[i]);

        }
        sb.append("]");

        return sb.toString();
    }

}

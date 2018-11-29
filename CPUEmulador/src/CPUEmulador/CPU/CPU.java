/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.CPU;

import CPUEmulador.AtmelMain;
import CPUEmulador.CPU.Register;
import CPUEmulador.CPU.Instruction;
import CPUEmulador.Memory.Information;
import CPUEmulador.Memory.RAM;
import CPUEmulador.Util.BinaryOperations;
import java.awt.Event;
import java.awt.event.ActionListener;
import java.util.Arrays;
import java.util.Set;
import java.util.function.Function;

public class CPU {

    //Register
    protected Register DR; // Data reg;
    protected Register AR; // Address reg;
    protected Register AC; // Accumulator reg;
    protected Register IR; // Instruction reg;
    protected Register PC; // Program counter;
    protected Register TR; // Temporary reg;
    protected ALU ULA;

    //Endereçamento
    public static final int opcode_t = 4;
    public static final int operand_t = 16;

    private int ustep_c;
    private Instruction uist;

    private RAM communication;
    public static final Instruction[] instructionSet = new Instruction[]
    {
        new Instruction(0, "HLT", new Information(0, opcode_t)), // Halt
        new Instruction(1, "SET", new Information(1, opcode_t)), // Load
        new Instruction(2, "LDD", new Information(2, opcode_t)), // Store
        new Instruction(3, "STO", new Information(3, opcode_t)), // Jump
        new Instruction(4, "JMP", new Information(4, opcode_t)), // Compare
        new Instruction(5, "JPC", new Information(5, opcode_t)), // Compare
        new Instruction(6, "CEQ", new Information(6, opcode_t)), // Compare
        new Instruction(7, "CGT", new Information(7, opcode_t)), // Compare
        new Instruction(8, "CGE", new Information(8, opcode_t)), // Compare
        new Instruction(9, "CLT", new Information(9, opcode_t)), // Compare
        new Instruction(10, "CLE", new Information(10, opcode_t)), // Add
        new Instruction(11, "ADD", new Information(11, opcode_t)), // Subtract
        new Instruction(12, "SUB", new Information(12, opcode_t)), // Multiply
        new Instruction(13, "MLT", new Information(13, opcode_t)), // 
        new Instruction(14, "DIV", new Information(14, opcode_t)), //  CLEAR AC
        new Instruction(15, "CLR", new Information(15, opcode_t)) //Set
    };

    public CPU(RAM communication)
    {
        ustep_c = 0;
        this.communication = communication;
        DR = new Register(0, 16); // 16bits;
        AR = new Register(0, 16); // 22bits;
        AC = new Register(0, 16); // Accumulator reg;
        IR = new Register(0, 16); // Instruction reg;
        PC = new Register(0, 16); // Program counter;
        TR = new Register(0, 16); // Temporary reg;
        
        instructionSet[0].setFunctionality(this::HLT);
        instructionSet[1].setFunctionality(this::SET);
        instructionSet[2].setFunctionality(this::LDD);
        instructionSet[3].setFunctionality(this::STO);
        instructionSet[4].setFunctionality(this::JMP);
        instructionSet[5].setFunctionality(this::JPC);
        instructionSet[6].setFunctionality(this::CEQ);
        instructionSet[7].setFunctionality(this::CGT);
        instructionSet[8].setFunctionality(this::CGE);
        instructionSet[9].setFunctionality(this::CLT);
        instructionSet[10].setFunctionality(this::CLE);
        instructionSet[11].setFunctionality(this::ADD);
        instructionSet[12].setFunctionality(this::SUB);
        instructionSet[13].setFunctionality(this::MLT);
        instructionSet[14].setFunctionality(this::DIV);
        instructionSet[15].setFunctionality(this::CLR);
        

    }

    public Register[] getRegisters()
    {
        return new Register[]
        {
            DR, AC, AR, IR, PC, TR
        };

    }

    public void step()
    {
        fetch();
        Instruction ist = decode();
        ist.execute();
    }

    public void ustep()
    {
        switch (ustep_c % 3)
        {
            case 0:
                fetch();
                break;
            case 1:
                uist = decode();
                break;
            case 2:
                uist.execute();
                break;
        }
        ustep_c++;
    }

    public boolean isValidStep()
    {
        System.out.println(ustep_c + " " + (ustep_c % 4));
        return ustep_c % 3 == 0;
    }

    public void fetch()
    {
        AR = new Register(PC);

        DR = new Register(communication.getData(AR.getValue()));

        IR = new Register(DR);

        incrementPC();
    }

    public Instruction decode()
    {
        Information opcode = DR.getInRange(0, opcode_t);
        Information operand = DR.getInRange(opcode_t, opcode_t + operand_t);

        Instruction ist = Translator.parseCode(opcode.getValue(), this.instructionSet);
        ist.setOperand(operand);
        return ist;
    }

    void incrementPC()
    {
        PC.setValue(PC.getValue() + 1);
    }

    @Override
    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("DR " + DR + ", ");
        sb.append("AC " + AC + ", ");
        sb.append("AR " + AR + ", ");
        sb.append("IR " + IR + ", ");
        sb.append("PC " + PC + ", ");
        sb.append("TR " + TR);
        return sb.toString();
    }

    public Register getPC()
    {
        return PC;
    }

    public Boolean SET(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(AR);
        AC = new Register(DR);
        return true;
    }

    public Boolean LDD(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(DR);
        return true;
    }

    public Boolean STO(Instruction ist)
    {

        AR = new Register(ist.getOperand());
        DR = new Register(AC);
        communication.setData(AR.getValue(), DR);
        return true;
    }

    public Boolean JMP(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(AR);
        PC = new Register(DR);
        return true;
    }

    public Boolean JPC(Instruction ist) //Jump Compare;
    {
        AR = new Register(ist.getOperand());
        DR = new Register(AR);
        if(AC.getValue() == 0)PC = new Register(DR);
        return true;
    }

    public Boolean CEQ(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.compareEqual(AC, DR));
        return true;
    }

    public Boolean CGT(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.compareGreaterThan(AC, DR));
        return true;
    }

    public Boolean CGE(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.compareGreaterEqual(AC, DR));
        return true;
    }

    public Boolean CLT(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.compareLowerThan(AC, DR));
        return true;
    }

    public Boolean CLE(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.compareLowerEqual(AC, DR));
        return true;
    }

    public Boolean ADD(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.add(AC, DR));

        return true;
    }

    public Boolean SUB(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.sub(AC, DR));
        return true;
    }

    public Boolean MLT(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.mult(AC, DR));
        return true;
    }

    public Boolean DIV(Instruction ist)
    {
        AR = new Register(ist.getOperand());
        DR = new Register(communication.getData(AR.getValue()));
        AC = new Register(ULA.div(AC, DR));
        return true;
    }

    public Boolean CLR(Instruction ist)
    {
        AC.setValue(0);
        return true;
    }

    public Boolean HLT(Instruction ist)
    {
        return true;
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador;

import CPUEmulador.CPU.CPU;
import CPUEmulador.CPU.Instruction;
import CPUEmulador.CPU.Translator;
import CPUEmulador.Memory.Information;
import CPUEmulador.Memory.RAM;

/**
 *
 * @author Kai
 */
public class Computer {
    private RAM memory;
    private CPU processor;
    private String asm;
    private int ist_t;
    public Computer(String asm){
        
                        //1mb
        ist_t = CPU.opcode_t + CPU.operand_t;
        memory = new RAM(ist_t*64,ist_t);
        processor = new CPU(memory);
        this.asm = asm;
        loadAssembly(asm);
    }
    
    private void loadAssembly(String asm){
        String[] lines = asm.split("\\r?\\n");
        int position = 0;
        for(int i = 0 ; i < lines.length; ++i){
            if(lines[i].contains("//"))continue;
            String[] tokens = lines[i].split("\\s+");
            Instruction op = Translator.parseName(tokens[0].trim());
            if(tokens.length > 1)
                op.setOperand(new Information(Integer.parseInt(tokens[1].trim()), CPU.operand_t));
            memory.setInstruction(position, op);
            position++;
        }
    }
    
    public String getAssembly(){
        return asm;
    }
    
    
    public CPU getProcessor(){
        return processor;
    }
    public RAM getMemory(){
        return memory;
    }
    
}

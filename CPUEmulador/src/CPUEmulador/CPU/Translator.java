/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.CPU;

import CPUEmulador.CPU.Instruction;
import CPUEmulador.CPU.CPU;
/**
 *
 * @author Kai
 */
public class Translator{
    
    public static Instruction parseName(String name){
        for(int i = 0; i < CPU.instructionSet.length ;++i)
            if(CPU.instructionSet[i].getName().equals(name))
                return new Instruction(CPU.instructionSet[i]);
        return null;
    }
    
    public static Instruction parseCode(int code){
        for(int i = 0; i < CPU.instructionSet.length ;++i)
            if(CPU.instructionSet[i].getCode().getValue()== code)
                return new Instruction(CPU.instructionSet[i]);
        return null;
    }
    
    public static Instruction parseCode(int code, Instruction[] instructionSet){
        for(int i = 0; i < instructionSet.length ;++i)
            if(instructionSet[i].getCode().getValue()== code)
                return instructionSet[i];
        return null;
    }
    
}

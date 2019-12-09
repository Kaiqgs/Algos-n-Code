/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.CPU;

import CPUEmulador.Memory.Information;

/**
 *
 * @author Kai
 */
public class ALU {

    public static Information add(Information a, Information b)
    {
        return new Information(a.getValue() + b.getValue(), getMaxBits(a,b));
    }

    public static Information sub(Information a, Information b)
    {
        return new Information(a.getValue() - b.getValue(), getMaxBits(a,b));
    }

    public static Information mult(Information a, Information b)
    {
        return new Information(a.getValue() * b.getValue(), getMaxBits(a,b));
    }

    public static Information div(Information a, Information b)
    {
        return new Information(a.getValue() / b.getValue(), getMaxBits(a,b));
    }
    
    public static Information compareEqual(Information a, Information b){
        return new Information( a.getValue() == b.getValue()?1:0,getMaxBits(a,b));
    }
    
    public static Information compareGreaterThan(Information a, Information b){
        return new Information( a.getValue() > b.getValue()?1:0,getMaxBits(a,b));
    }
    
    public static Information compareGreaterEqual(Information a, Information b){
        return new Information( a.getValue() >= b.getValue()?1:0,getMaxBits(a,b));
    }
    
    public static Information compareLowerThan(Information a, Information b){
        return new Information( a.getValue() < b.getValue()?1:0,getMaxBits(a,b));
    }
    
    public static Information compareLowerEqual(Information a, Information b){
        return new Information( a.getValue() <= b.getValue()?1:0,getMaxBits(a,b));
    }
    
    
    public static int getMaxBits(Information a, Information b){
        return Math.max(a.getNBits(), b.getNBits());
    }
}

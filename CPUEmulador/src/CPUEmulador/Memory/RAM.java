/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.Memory;

import CPUEmulador.CPU.Instruction;
import CPUEmulador.Memory.Information;
import CPUEmulador.Util.BinaryOperations;
import java.lang.reflect.Array;
import java.util.Arrays;

public class RAM {

    private Information data;
    private final int address_t;
    private final int size;

    public RAM(int size, int instruction_t)
    {
        this.size = size;
        this.address_t = instruction_t;
        this.data = new Information(0, size);
    }

    public Information getData(int position)
    {
        position *= address_t;
        if (position > data.getNBits())
        {
            return null;
        }
        return data.getInRange(position, position + address_t);
    }

    public void setData(int position, Information data)
    {   
        position *= address_t;
        if (position > this.data.getNBits() || data.getNBits() > address_t)
        {
            return;
        }
        
        this.data.setInRange(position,BinaryOperations.padLeftBits(data.getData(),address_t));
        System.out.println(this.data);
    }

    //Opcode - Operand
    public void setInstruction(int position, Instruction instruction)
    {
        position *= address_t;
        if (position > data.getNBits())
        {
            return;
        }
        Boolean[] code = instruction.getCode().getData();
        Boolean[] op = instruction.getOperand().getData();
        data.setInRange(position, code);
        data.setInRange(position + code.length, op);
    }

    public Information getData()
    {
        return data;
    }

    @Override
    public String toString()
    {
        String bin = data.getBinaryData();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size / address_t; ++i)
        {
            int n = i * address_t;
            for (int j = n; j < n + address_t; ++j)
            {
                sb.append(bin.charAt(j));
            }
            //sb.append(" -> " + n);
            sb.append("\n");
        }
        return sb.toString();
    }

    public String[] getLines()
    {
        String[] lines = new String[size / address_t];
        char[] _d = data.getBinaryData().toCharArray();
        int n = 0;
        for (int i = 0; i < lines.length; i ++)
        {   
            n = i * address_t;
            String bin = new String(Arrays.copyOfRange(_d, n, n + address_t));
            int value = BinaryOperations.binaryToDecimal(bin);
            lines[i] = bin + " -> " + i + (value  < 65536 ? " = " +  value : "" ) ;
            
        }
        return lines ;
    }
    

}

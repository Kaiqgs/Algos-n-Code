/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.Memory;

import CPUEmulador.Util.BinaryOperations;
import java.util.Arrays;

/**
 *
 * @author Kai
 */
public class Information {

    protected Boolean data[];
    protected int nBits;
    protected String binaryData;
    protected int value;

    public Information(int value)
    {
        this(value, countBits(value));
    }

    public Information(int value, int nBits)
    {
        this.nBits = nBits;
        data = new Boolean[nBits];
        setValue(value);
    }
    
    public Information(Information information){
        this.nBits = information.getNBits();
        value = information.getValue();
        data = information.getData();
        binaryData = information.getBinaryData();
    }
    
    
    public Information(Boolean[] data){
        this.data = data;
        this.nBits = data.length;
        setValue(BinaryOperations.binaryToDecimal(data));
    }

    public void setValue(int value)
    {
        this.value = value;
        setBinaryData(value);
        setData(value);
    }

    private void setBinaryData(int value)
    {
        
        binaryData = Integer.toBinaryString(value);
        for (int i = binaryData.length(); i < nBits; ++i)
        {
            binaryData = "0" + binaryData;
        }
    }

    private void setData(int value)
    {
        setBinaryData(value);
        for (int i = 0; i < binaryData.length(); ++i)
        {
            data[i] = binaryData.charAt(i) == '1' ? true : false;
        }
    }

    static int countBits(int number)
    {
        return (int) (Math.log(number)
                / Math.log(2) + 1);
    }

    public int getValue(){
        return value;
    }
    
    public Information getInRange(int start, int end){
        return new Information(Arrays.copyOfRange(data,start,end));
    }
    
    public void setInRange(int position, Boolean[] data){
        char[] s = this.binaryData.toCharArray();
        int n = 0;
        for(int i = position; i < position + data.length; ++i)
        {
            n = i-position;
            this.data[i] = data[n];
            s[i] = data[n] ? '1' : '0';            
        }
        
        this.binaryData = new String(s);
    }
     
    
    
    public Boolean[] getData(){
        return data;
    }
    
    public String getBinaryData(){
        return binaryData;
    }
    
    public int getNBits(){
        return nBits;
    }
    
    @Override
    public String toString()
    {
        return binaryData + " | " + value;
    }

}

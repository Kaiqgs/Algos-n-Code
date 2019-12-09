/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.Util;

import CPUEmulador.AtmelMain;
import CPUEmulador.Memory.Information;
import sun.security.util.Length;

/**
 *
 * @author Kai
 */
public class BinaryOperations {

    public static int binaryToDecimal(Boolean[] bin)
    {
        int value = 0;
        for (int i = 0; i < bin.length; ++i)
        {
            int n = bin.length - i - 1;
            if (bin[i])
            {
                value += Math.pow(2, n);
            }
        }
        return value;
    }
        public static int binaryToDecimal(String bin)
    {
        int value = 0;
        for (int i = 0; i < bin.length(); ++i)
        {
            int n = bin.length() - i - 1;
            if (bin.charAt(i) == '1')
            {
                value += Math.pow(2, n);
            }
        }
        return value;
    }
    

    public static Boolean[] padLeftBits(Boolean[] bin, int bits)
    {
        if (bin.length >= bits)
        {
            return bin;
        }
        Boolean[] n_bin = new Boolean[bits];
        int dif = bits - bin.length;
        for (int i = 0; i < n_bin.length; ++i)
        {
            if (i < dif)
            {
                n_bin[i] = false;
            }
            else
            {
                n_bin[i] = bin[i - dif];
            }
        }
        
        return n_bin;

    }
}

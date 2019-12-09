/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CPUEmulador.CPU;

import CPUEmulador.Memory.Information;

public class Register extends Information {

    public Register(int value, int nBits)
    {
        super(value, nBits);
    }
    
    public Register(Information information){
        super(information);
    }
}

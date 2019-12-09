/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bitthread;

/**
 *
 * @author CC04735125990
 */
public class Comprador {
    public Carteira carteira;
    public Comprador(){
        carteira = new Carteira("BTCBRL", 0, 1000000);
    } 
}

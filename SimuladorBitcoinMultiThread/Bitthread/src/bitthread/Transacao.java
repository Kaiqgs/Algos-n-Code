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
public class Transacao {
    public int id;
    public int idComprador;
    public String sym;
    public double cotacaoComprado;
    
    
    public Transacao(int id, int idComprador, String sym, double cotacaoComprado){
        this.id = id;
        this.idComprador = idComprador;
        this.sym = sym;
        this.cotacaoComprado = cotacaoComprado;
    }
}

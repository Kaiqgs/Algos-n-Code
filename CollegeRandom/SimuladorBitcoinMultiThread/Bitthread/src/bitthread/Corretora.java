/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bitthread;

import java.util.ArrayList;

/**
 *
 * @author CC04735125990
 */
public class Corretora {
    public Carteira carteira;
    public double cotacao;
    public String sym;
    public ArrayList<Transacao> transacoes;
    
    public Corretora(){
        
        //Símbolo troca;
        sym = "BTCBRL";
        
        //Carteira;
        carteira = new Carteira(sym, 100, 0);
        
        //Cotação inicial;
        cotacao = 35221.00;
        
        transacoes = new ArrayList<Transacao>();
    }
    
    public void Compra(Comprador comprador, double pct){
        
        double cotacaoComprado = comprador.carteira.moedaCotacao * pct;
        double comprado = cotacaoComprado/cotacao;
        
        comprador.carteira.moedaCotacao -= cotacaoComprado;
        comprador.carteira.moedaBase += comprado;
        
        
        cotacao += cotacao *.000001;
        
        System.out.println("Comprado: " + comprado);        
    }
    
    public void Vende(Comprador comprador, double pct){
        
        double baseVendido = comprador.carteira.moedaBase * pct;
        double vendido =  baseVendido * cotacao;
        
        
        
        comprador.carteira.moedaBase -=  baseVendido;
        comprador.carteira.moedaCotacao += vendido;
        
        cotacao -= cotacao *.000001;
        
        System.out.println("Vendido: " + vendido);
    }
}

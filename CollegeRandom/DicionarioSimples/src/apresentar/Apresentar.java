package apresentar;


/** 
 Trabalho Programação 2, exercício 13:
 * Kaique Alan gualter dos Santsos RA:120176;
 **/

public class Apresentar {
    
    public static void main(String[] args) {
       Dicionario<String,Integer> dict = new Dicionario();
       dict.inserir("Dez",10);
       dict.inserir("Cinco", 5);
       dict.inserir("Mil", 1000);
       dict.inserir("Vinte", 20);
       System.out.println(dict);
       
        System.out.println("Removido: "+dict.remover("Cinco"));
        dict.inserir("Mil",100);
        System.out.println(dict);
    }
    
}

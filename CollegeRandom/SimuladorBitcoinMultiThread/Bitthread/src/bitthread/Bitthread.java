/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bitthread;

import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author CC04735125990
 */
public class Bitthread {

    static Corretora corretora;
    static ArrayList<Comprador> poolCompradores;
    static GUI frame;
    static int nComprador;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        nComprador = 100;
        corretora = new Corretora();
        poolCompradores = createPoolComprador(nComprador);

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                frame = new GUI(corretora);
                frame.setVisible(true);
                frame.setCotacao(corretora.cotacao);
            }
        });

        for (int i = 0; i < nComprador; ++i) {
            concurrentComprador(i).start();
        }

    }

    public static ArrayList<Comprador> createPoolComprador(int n) {
        ArrayList<Comprador> pool = new ArrayList<Comprador>();
        for (int i = 0; i < n; ++i) {
            pool.add(new Comprador());
        }
        return pool;
    }

    public static Thread concurrentComprador(int i) {
        return new Thread() {

            @Override
            public void run() {
                Random gerador = new Random();
                while (true) {
                    if (gerador.nextInt(2) == 1) {
                        corretora.Compra(poolCompradores.get(i), 0.1);
                    } else {
                        corretora.Vende(poolCompradores.get(i), 0.1);
                    }
                    if (frame != null) {
                        frame.setCotacao(corretora.cotacao);
                    }
                }
            }
        };

    }

}

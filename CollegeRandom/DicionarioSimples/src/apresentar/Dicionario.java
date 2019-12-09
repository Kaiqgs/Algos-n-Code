package apresentar;

import java.util.ArrayList;
import java.util.List;

public class  Dicionario<C,V>{
    private List<C> chaves;
    private List<V> valores;
    
    public Dicionario(){
        chaves = new ArrayList();
        valores = new ArrayList();
    }
    
    public void inserir(C chave, V valor){
        if(chaves.contains(chave)){
            valores.set(chaves.indexOf(chave),valor);
            return;
        }
        chaves.add(chave);
        valores.add(valor);
    }
    
    public V getValor(C chave){
        if(!chaves.contains(chave))return null;
         return valores.get(chaves.indexOf(chave));
    }
    
    public C getChave(V valor){
        if(!valores.contains(valor))return null;
        return chaves.get(valores.indexOf(valor));
    }
    
    public V remover(C chave){
        if(!chaves.contains(chave))return null;
        V valor = valores.get(chaves.indexOf(chave));
        valores.remove(valor);
        chaves.remove(chave);
        return valor;
    }
    
    public List<C> getChaves(){
        return chaves;
    }
    
    public List<V> getValores(){
        return valores;
    }
    
    @Override public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        for(int i = 0; i < chaves.size(); ++i){
            if(i!=0)sb.append(",\n");
            sb.append(chaves.get(i) + ":" + valores.get(i));
        }
        sb.append("\n}");
        return sb.toString();
    }
}

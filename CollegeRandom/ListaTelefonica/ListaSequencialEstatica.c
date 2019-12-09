#include "ListaSequencialEstatica.h"

void inicializa(LISTA *l){ //Construtor da lista
  l->nroElem = 0;
}

int tamanho(LISTA *l){ //Retorna numero de elementos
  return l->nroElem;
}

void reinicializar(LISTA *l){ //Recomeça lista
  l->nroElem = 0;
}

REGISTRO * criaRegistro(STRING nome, STRING endereco, TELEFONE tel){ // Cria um registro
    REGISTRO * r = malloc(sizeof(REGISTRO));
    r->nome = nome;
    r->endereco = endereco;
    r->telefone = tel;
    return (REGISTRO *) r;
}

//Função para comparar valor alfabético de strings
//Melhor que strcmp() pois lida bem com caracteres minusculos
BOOL strEsqrdMaior(STRING str1, STRING str2){
    int strSize,i;
    if(strlen(str1)<strlen(str2))strSize = strlen(str1);
    else strSize = strlen(str2);

    for(i=0; i < strSize; ++i){
            if(tolower(str1[i]) < tolower(str2[i]))return FALSE;
            else if(tolower(str1[i]) > tolower(str2[i]))return TRUE;
    }
    return FALSE;
}

BOOL insereElem(LISTA *l, REGISTRO val){ //Inserção ordenada
  int i;
  if(l-> nroElem >= MAX)return FALSE;


  for(i=l->nroElem; !strEsqrdMaior(val.nome,l->A[i-1].nome)&& i != 0 ; i--){
   l->A[i] = l->A[i-1];
  }
  l->A[i] = val;
  (l->nroElem)++;
  return TRUE;
}

void exibir(LISTA *l, STRING msg){ //Printa lista
  int i;
  printf("\n%s: ",msg);

  for(i=0; i < l->nroElem; ++i){
    printf("\n [pos=%3d, nome=%17s, endereco=%19s, telefone=%10i]",i,l->A[i].nome,l->A[i].endereco, l->A[i].telefone );
  }
}

BOOL cmpRegistro(REGISTRO reg1, REGISTRO reg2){ //Facil comparação de registros
    return reg1.telefone == reg2.telefone &&
           strcmp(reg1.nome,reg2.nome)==0&&
           strcmp(reg1.endereco, reg2.endereco)==0;
}

int buscaSequencial(LISTA *l, REGISTRO val){//Busca simples
  int i=0;
  while(i < l->nroElem){
    if(cmpRegistro(l->A[i], val)){
      return i;
    }
    i++;
  }
  return -1;
}


int buscaBinaria(LISTA * l, REGISTRO reg){//Busca binaria
  int i = 0;
  int f = l -> nroElem;
  int pos = (i + f)/2;
  while(cmpRegistro(l->A[pos], reg)==0&& i <= f && f >= i && pos > 0){
  if(strEsqrdMaior(l->A[pos].nome, reg.nome)){
      f = pos + 1;
  }else{
    i = pos - 1;
  }
  pos = (i + f)/2;
  }
  if(cmpRegistro(l->A[pos],reg)){
  return pos;
  }
  return -1;

}

BOOL exclusao(LISTA * l, REGISTRO reg){//Exclusao por busca binaria
  int pos = buscaBinaria(l, reg);
  if(pos == -1)return pos;
    int i = pos;
    (l->nroElem)--;
    for(;i<l->nroElem; ++i){
      l->A[i] = l->A[i+1];
    }
    return pos;
}

void populaLista(LISTA *l){//Função pra encher a lista facilmente
    LISTA listaTelefonica;
    inicializa(&listaTelefonica);

    //-- muito copia e cola, apenas pra evitar lidar com arquivos
    REGISTRO * registro = criaRegistro("Kaique Alan", "Rua Edigard Vieira", 998753620);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Bruno Mendez", "Avenida Comendador", 999810271);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Gabriel dos Reis", "Avenida Luiz Meneghel", 988775566);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Eduarda Muraro", "Rua Euripedes", 988445626);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Mauricio Gualter", "Rua Edigard", 988235626);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Cindy Lauper", "Rua Hollywood", 987534625);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Alice Louback", "Rua Curitiba", 961334625);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Carolyn", "Rua Edna", 996261810);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Diana", "Rua Ruth", 956198059);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Peggy", "Rua Robin", 984927459);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Lydia", "Rua Kathryn", 997738990);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Jane", "Rua Gertrude", 960872732);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Maggie", "Rua Katie", 974107645);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Kathleen", "Rua Julia", 905784086);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Daisy", "Rua Joanne", 923534022);
    insereElem(&listaTelefonica, *registro);
    registro = criaRegistro("Lillian", "Rua Virginia", 967849520);
    insereElem(&listaTelefonica, *registro);
    *l = listaTelefonica;
    }

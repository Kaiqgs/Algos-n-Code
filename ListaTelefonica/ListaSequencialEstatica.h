#ifndef LISTASEQUENCIALESTATICA_H_INCLUDED
#define LISTASEQUENCIALESTATICA_H_INCLUDED
//-- Importados para previnir warnings
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
//--
#define MAX 100
#define TRUE 1
#define FALSE 0

typedef int BOOL;
typedef char * STRING;
typedef int TELEFONE;

typedef struct{
    STRING nome;
    STRING endereco;
    TELEFONE telefone;
} REGISTRO;

typedef struct{
  REGISTRO A[MAX];
  int nroElem;
}LISTA;

//-- Protótipos

void inicializa(LISTA *l);
int tamanho(LISTA *l);
void reinicializar(LISTA *l);
REGISTRO * criaRegistro(STRING nome, STRING endereco, TELEFONE tel);
BOOL strEsqrdMaior(STRING str1, STRING str2);
BOOL insereElem(LISTA *l, REGISTRO val);
void exibir(LISTA *l, STRING msg);
BOOL cmpRegistro(REGISTRO reg1, REGISTRO reg2);
int buscaSequencial(LISTA *l, REGISTRO val);
int buscaBinaria(LISTA * l, REGISTRO reg);
BOOL exclusao(LISTA * l, REGISTRO reg);
void populaLista(LISTA *l);
#endif // LISTASEQUENCIALESTATICA_H_INCLUDED

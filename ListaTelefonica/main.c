#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>
#include "ListaSequencialEstatica.h"
int main()
{
    //-- Declarações
    LISTA listaTelefonica;
    inicializa(&listaTelefonica);
    REGISTRO * paraBuscaSequencial;
    REGISTRO * paraBuscaBinaria;

    //-- Preenchendo lista com alguns exemplos
    populaLista(&listaTelefonica);

    //-- Declara registros para exclusão/busca
    paraBuscaSequencial = criaRegistro("Gabriel dos Reis", "Avenida Luiz Meneghel", 988775566);
    paraBuscaBinaria = criaRegistro("Cindy Lauper", "Rua Hollywood", 987534625);


    exibir(&listaTelefonica, "Lista antes da exclusao");

    printf("\n\n-- Busca Sequencial: elemento = \"%s\" [pos = %d]",paraBuscaSequencial->nome,buscaSequencial(&listaTelefonica, *paraBuscaSequencial));
    printf("\n-- Sequencial: elemento = \"%s\" [pos = %d]",paraBuscaBinaria->nome,buscaSequencial(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Binaria: elemento = \"%s\" [pos = %d]",paraBuscaSequencial->nome,buscaBinaria(&listaTelefonica, *paraBuscaSequencial));
    printf("\n-- Busca Binaria: elemento = \"%s\" [pos = %d]",paraBuscaBinaria->nome,buscaBinaria(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Exclusao: elemento = \"%s\" [pos = %d]",paraBuscaBinaria->nome, exclusao(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Exclusao: elemento = \"%s\" [pos = %d]\n",paraBuscaSequencial->nome, exclusao(&listaTelefonica, *paraBuscaSequencial));

    exibir(&listaTelefonica, "Lista depois da exclusao");
    getchar();//Previnir tela de fechar ao rodar .exe
}



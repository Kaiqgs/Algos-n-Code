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

    printf("\n\n-- Elemento encontrado por Busca Sequencial [pos = %d]",buscaSequencial(&listaTelefonica, *paraBuscaSequencial));
    printf("\n-- Elemento encontrado por Busca Sequencial [pos = %d]",buscaSequencial(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Elemento encontrado por Busca Binaria [pos = %d]",buscaBinaria(&listaTelefonica, *paraBuscaSequencial));
    printf("\n-- Elemento encontrado por Busca Binaria [pos = %d]",buscaBinaria(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Exclusao tentara ser feita no registro \"%s\" [pos = %d]",paraBuscaBinaria->nome, exclusao(&listaTelefonica, *paraBuscaBinaria));
    printf("\n-- Exclusao tentara ser feita no registro \"%s\" [pos = %d]\n",paraBuscaSequencial->nome, exclusao(&listaTelefonica, *paraBuscaSequencial));

    exibir(&listaTelefonica, "Lista depois da exclusao");
    getchar();//Previnir tela de fechar ao rodar .exe
}



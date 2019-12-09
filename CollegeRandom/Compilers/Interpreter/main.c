#include <stdio.h>
#include <string.h>
#include"interpreter.h"

void solve(string_t in)
{
    attr_t attribute = ftype(in);
    if(attribute != NULL)
        printf(" %d\n", attribute->value);
}


int main(void)
{
    printf("Aluno<Kaique Alan Gualter dos Santos> RA<120176>\n");
    printf("Suggestions to try:\n");
    printf("// x = 20\n");
    printf("// x = x + 1\n");
    printf("// y = x - 20\n");
    printf("// x - y\n");

    char in[MAX_IN];
    while(1)
    {
        printf("> ");
        fgets(in, MAX_IN, stdin);
        solve(in);
    }
}

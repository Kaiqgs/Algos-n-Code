#include"util.h"
#include<stdio.h>

string_t strip(string_t string, char to_strip)
{
    string_t out_str = string;
    string_t in_str = string;

    while(*in_str != EOS)
    {
        *out_str = *in_str++;
        if(*out_str != to_strip)
            out_str++;
    }

    *out_str = EOS;
    return string;
}

void appendchar(string_t dest, char src, int* pos)
{
    if(dest[*pos]!=EOS)
    {
        printf("Warning: AppendChar requires that the position contains an EOS.");
        return;
    }

    (*pos)++;
    dest[*pos] = dest[*pos-1];
    dest[*pos-1] = src;
}

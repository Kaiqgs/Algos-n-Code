#ifndef UTIL
#define UTIL

#include <string.h>

#define bool int
#define true 1
#define false 0

#define EOS '\0'

typedef char* string_t;

string_t strip(string_t string, char to_strip);
void appendchar(string_t dest, char src, int* pos);

#endif

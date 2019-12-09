#ifndef INTERPRETER
#define INTERPRETER

#include"lookuptable.h"

#define MAX_IN 256
#define MAX_TOK_SIZE 128

#define INV_TYPE 0
#define NUM_TYPE 1
#define VAR_TYPE 2
#define OP_TYPE 3

#define EQUAL_SIGN '='
#define ADD_SIGN '+'
#define SUB_SIGN '-'
#define INV_SIGN '?'

#define DEBUG false

char input[MAX_IN];
typedef int type_t;
typedef char sign_t;

typedef struct
{
    type_t type;
    string_t value;
} token;

typedef struct
{
    int value;
    sign_t sign;
} attr;

typedef token* token_t;
typedef attr* attr_t;

token_t nexttoken(char * input);
attr_t ftype();
attr_t varop();
attr_t stype();
attr_t operation();
void match();
void printattr(attr_t att, string_t id);

#endif


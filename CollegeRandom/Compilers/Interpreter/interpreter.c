#include"interpreter.h"
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

/*
P -> numR | varX
X -> R | = E
E -> numR | varR
R -> +E | -E | ε
*/

// ftype -> num.operation | var,varop
// varop -> operation | =stype
// stype -> num.operation | var.operation
// operation-> +stype | -stype | eps

static token_t lookahead = NULL;
static token_t ctoken = NULL;

void readvar()
{
    /*
        Read current_token as variable.
    */
    item_t var = get_lut(ctoken->value);
    int var_value = var->value;
    sprintf(ctoken->value, "%d", var_value);
}

attr_t iniattr(int value, sign_t sign)
{
    /*
        Alloc and initializes attributes;
    */
    attr_t att = malloc(sizeof(attr));
    att->value = value;
    att->sign = sign;
    return att;
}

void printattr(attr_t att, string_t id)
{
    /*
        prints formatted attributes.
    */

    if(att!=NULL)
        printf("%s[%d] %s[%c]\n",id, att->value,id, att->sign);
    else
        printf("%s == NULL", id);
}

attr_t calc(attr_t a, attr_t b)
{
    /*
        Performs calcuation on attributes;
    */
    if(a == NULL || b == NULL)
    {
        printf("Neither values can be null!");
    }

    sign_t sign;
    attr_t out = iniattr(0, INV_SIGN);

    if(a->sign == INV_SIGN && b->sign != INV_SIGN)
        sign = b->sign;
    else if(a->sign != INV_SIGN && b->sign == INV_SIGN)
        sign = a->sign;

    if(sign == ADD_SIGN)
        out->value = a->value + b->value;
    else if(sign == SUB_SIGN)
        out->value = a->value - b->value;

    return out;
}

void match()
{
    /*
        Matches and update current_token(ctoken)
        and look_ahead(lookahead);
    */
    if(lookahead == NULL && ctoken == NULL)
    {
        ctoken = nexttoken(input);
        lookahead = nexttoken(NULL);
    }
    else
    {
        ctoken = nexttoken(NULL);
        lookahead = nexttoken(NULL);
    }
}

sign_t tosign(token_t token)
{
    /*
        Converts token into sign (e.g +, -, =);
    */
    if(token == NULL)
        return INV_SIGN;
    if(token->type != OP_TYPE)
        return INV_SIGN;
    return token->value[0];
}

attr_t parsetok(token_t a, token_t b)
{
    return iniattr(atoi(a->value), tosign(b));
}

// ftype -> num.operation | var.varop
// varop -> operation | =stype
// stype -> num.operation | var.operation
// operation-> +stype | -stype | eps

attr_t ftype(string_t inpt)
{
    if(inpt!= NULL)
    {
        ctoken = NULL;
        lookahead = NULL;
        strcpy(input, inpt);
    }
    match();
    if(ctoken == NULL)
        return NULL;
    //ftype -> num.operation
    if(ctoken->type == NUM_TYPE)
    {
        return operation();
    }
    //ftype -> var.varop
    else if(ctoken->type == VAR_TYPE)
    {
        return varop();
    }

    return NULL;
}

attr_t varop()
{
    attr_t cur = parsetok(ctoken, lookahead);

    // varop -> =var
    if(cur->sign == EQUAL_SIGN)
    {
        string_t name = ctoken->value;
        attr_t varatt = stype();
        if(DEBUG)
            printattr(varatt, "varop");
        update_lut(name, varatt->value);
        return NULL;
    }
    // varop -> operation
    else
    {
        readvar();
        return operation();
    }
}

attr_t stype()
{
    match();

    // stype -> var.operation
    if(ctoken->type == NUM_TYPE)
    {
        return operation();
    }
    // stype -> var.operation
    else if(ctoken->type == VAR_TYPE)
    {
        readvar();
        attr_t res = operation();
        if(DEBUG)
            printattr(res, "stype");
        return res;
    }


    return NULL;
}

attr_t operation()
{

    if(ctoken == NULL && lookahead == NULL)
        return NULL;

    attr_t actual = parsetok(ctoken, lookahead);
    if(DEBUG)
        printattr(actual,"op_bef");

    // operation -> epsilon
    if(lookahead == NULL && ctoken != NULL)
    {
        if(DEBUG)
            printf("Lastval= %d and isinv %d\n", actual->value, actual->sign ==INV_SIGN);
        return actual;
    }
    // operation -> +stype | -stype
    else if(lookahead->type == OP_TYPE)
    {
        if(DEBUG)
            printf("Here 2\n");
        token_t token = ctoken;
        attr_t parsed = stype();

        attr_t result = calc(actual, parsed);

        if(DEBUG)
            printattr(actual, "op_aft");
        if(DEBUG)
            printattr(parsed, "op_fut");
        if(DEBUG)
            printattr(result, "op_res");
        return result;
    }
    return NULL;
}



bool isop(char c)
{
    /*
      Check if given char is operation;
    */
    return c == ADD_SIGN ||
           c == SUB_SIGN ||
           c == EQUAL_SIGN;
}


bool invalidchar(char c)
{
    /*
        Check if given char is valid;
    */
    return !isop(c) && !isalpha(c) && !isdigit(c);
}

token_t initoken(type_t type, string_t value)
{
    /*
        Creates and assign values to token;
    */
    token_t token = malloc(sizeof(token));
    token->type = type;
    token->value = value;
    return token;
}

token_t nexttoken(string_t input)
{
    /*
        Gets tokens from given input.
    */
    static int i = 0;
    static string_t _in = NULL;

    int tokidx;
    char lastchar;
    char nextchar;
    token_t token;
    type_t toktype;
    string_t tokval;

    if(input != NULL)
    {
        _in = input;
        i = 0;
        if(strlen(input)==0)
            return NULL;
    }
    token = NULL;
    tokidx = 0;
    tokval = malloc(sizeof(char) * MAX_TOK_SIZE);
    lastchar = '@';
    tokval[tokidx] = EOS;
    toktype = INV_TYPE;

    for(nextchar = _in[i]; //Initialize;
            lastchar != EOS    ; //While;
            lastchar = nextchar, //Update;
            i++,
            nextchar = _in[i])
    {
        if(isdigit(lastchar) && !isdigit(nextchar))
        {
            toktype = NUM_TYPE;
            break;
        }
        else if(isalpha(lastchar) && !isalpha(nextchar))
        {
            toktype = VAR_TYPE;
            break;
        }
        else if(isop(lastchar) && !isop(nextchar))
        {
            toktype = OP_TYPE;
            break;
        }

        if(!invalidchar(lastchar))
            appendchar(tokval, lastchar, &tokidx);
    }

    //Debugging;
    //printf("| l[%c] n[%c] tok[%01d] isal[%01d] isan[%01d] idx[%02d] | ", lastchar,nextchar, toktype,isalpha(lastchar), isalpha(nextchar), i);

    if(lastchar != EOS)
    {
        if(!invalidchar(lastchar))
            appendchar(tokval, lastchar, &tokidx);
        token = initoken(toktype, tokval);
    }

    return token;
}

#ifndef LOOKUP_TABLE
#define LOOKUP_TABLE

#include"util.h"

#define MAX_ITEMS 256

typedef int data;

typedef struct
{
    string_t name;
    data value;
} item;

typedef item* item_t;


static int lut_idx = 0;
static item lut[MAX_ITEMS];


void insert_lut(item_t item);
item_t get_lut(string_t key);
void update_lut(string_t key, data new_value);

#endif

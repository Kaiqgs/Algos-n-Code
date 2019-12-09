#include"lookuptable.h"

item_t init_item(string_t name, data value)
{
    item_t item = malloc(sizeof(item));
    item->name = name;
    item->value = value;
    return item;
}

void insert_lut(item_t item)
{
    if(lut_idx > MAX_ITEMS)
        return;
    lut[lut_idx++] = *item;
}

item_t get_lut(string_t key)
{

    int i = 0;
    for(i = 0; i < lut_idx; ++i)
    {
        if(strcmp(key, lut[i].name)==0)
            return (item_t)&lut[i];

    }
    return init_item(key, 0);
}

void update_lut(string_t key, data new_value)
{
    int i = 0;
    for(i = 0; i < lut_idx; ++i)
    {
        if(strcmp(key, lut[i].name)==0)
        {
            lut[i].value = new_value;
            return;
        }
    }
    insert_lut(init_item(key, new_value));
}

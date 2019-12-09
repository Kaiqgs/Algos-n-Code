#ifndef MEMORY_MANAGEMENT
#define MEMORY_MANAGEMENT
#include "Persistence.h"
#include <EEPROM.h>

#define MEM_OFFSET 32
#define SIGNUP_PWD_MEM_ADDR 0
#define SIGNUP_USER_MEM_ADDR SIGNUP_PWD_MEM_ADDR + MEM_OFFSET
#define STATE_MEM_ADDR SIGNUP_USER_MEM_ADDR + MEM_OFFSET


String load_password(){
  char  pwd[MEM_OFFSET]; //= (char*) malloc(MEM_OFFSET);
  EEPROM.get(SIGNUP_PWD_MEM_ADDR, pwd);
  return String(pwd);
}

void dump_password(String pwd){
  char pwdc[MEM_OFFSET];
  pwd.toCharArray(pwdc, MEM_OFFSET);
  EEPROM.put(SIGNUP_PWD_MEM_ADDR, pwdc);
}


String load_email(){
  char user[MEM_OFFSET];
  EEPROM.get(SIGNUP_USER_MEM_ADDR, user);
  return String(user);
}

void dump_email(String user){
  char userc[MEM_OFFSET];
  user.toCharArray(userc, MEM_OFFSET);
  EEPROM.put(SIGNUP_USER_MEM_ADDR, userc);
}

int load_state(){
  int val;
  EEPROM.get(STATE_MEM_ADDR, val);
  return val;
}

void dump_state(int state){
  EEPROM.put(STATE_MEM_ADDR, state);
}


#endif

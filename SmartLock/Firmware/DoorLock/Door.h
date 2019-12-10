#ifndef DOOR
#define DOOR
#include "Pinnout.h"
#include "MemoryManagement.h"

#define TIME2OPEN 1000
#define DEFAULTMOVE 0

#define DOOR_UNKNOWN 0
#define DOOR_LOCKED 1
#define DOOR_UNLOCKED 2

class Door{
  private:
  int IN1;
  int IN2;
  int state;
  unsigned long moveStart;
  
  void stopMotors(){
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
  }

  void startMove(int pin){
    Serial.print("Moving pin ");
    Serial.print(pin);
    Serial.print(" | ");
    Serial.println(millis());
    updateState(pin);
    moveStart = millis();
    digitalWrite(pin, HIGH);
  }

  void finishMove(){
    Serial.print("Finished Moving");
    Serial.print(" | ");
    Serial.println(millis());
    
    stopMotors();
    moveStart = DEFAULTMOVE;
  }

  void updateState(int pin){
    if(pin == IN1)state = DOOR_LOCKED;
    else state = DOOR_UNLOCKED;
    dump_state(state);
  }
  
  public:
  Door(int IN1, int IN2){
    this->IN1 = IN1;
    this->IN2 = IN2;
  }

  int getState(){
    return state;
  }
  
  void begin(){
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    moveStart = 0;
    state = load_state();
  }

  void update(){
    if(moveStart == 0) return;
    unsigned long elapsed = millis() - moveStart;
    if(elapsed >= TIME2OPEN)finishMove();    
  }

  void open(){startMove(IN1);}
  void close(){startMove(IN2);}  
};

Door MyDoor(L298N_IN2, L298N_IN1);

#endif

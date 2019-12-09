#ifndef COMMUNICATION
#define COMMUNICATION
#include <SoftwareSerial.h>
#include "Pinnout.h"

#define SUBS_SIZE 10

typedef String (*protoaction_t) (String);


SoftwareSerial _comm(BLE_TX, BLE_RX);

class Communication{
  int subidx;
  String protocols[SUBS_SIZE];
  protoaction_t actions[SUBS_SIZE];
  
  
  public:
  Communication(){
  }
  
  void begin(){
    subidx = 0;
    _comm.begin(9600);
    Serial.println("Communication begun...");
  }

  void update(){
    if(_comm.available()){
      String buffr = _comm.readString();
      
      for(int i = 0; i < subidx; ++i){
        int idx = buffr.indexOf(protocols[i]);
        if(idx != 0)continue;
        String response = (*actions[i])(buffr);
        Serial.print("Got= ");
        Serial.print(buffr);
        Serial.print("Replied= ");
        Serial.println(response);
        _comm.print(response +"\r\n");
      }
    }
  }

  void subscribe(String protocol, protoaction_t action){
    if(subidx >= SUBS_SIZE)return;
    Serial.print(subidx);
    Serial.print(" Subscribed to: ");
    Serial.println(protocol);
    protocols[subidx] = protocol;
    actions[subidx] =   action;
    subidx++;
  }
  
};

#endif

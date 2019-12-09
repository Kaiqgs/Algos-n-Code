#include <SoftwareSerial.h> 
#include "Door.h"
#include "Pinnout.h"
#include "Protocols.h"
#include "Communication.h"
#include "MemoryManagement.h"

Communication Comm;

void setup() 
{   
 Serial.begin(9600); 
 Comm.begin();  
 MyDoor.begin();
 beginProtocols(&Comm);
} 

void loop() 
{ 
 MyDoor.update(); 
 Comm.update(); 
}

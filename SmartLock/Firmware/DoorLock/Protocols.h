#ifndef PROTOCOLS
#define PROTOCOLS

#include "Communication.h"
#include "MemoryManagement.h"
#include "Door.h"

#define PROTOCOL_SIZE 5
#define MAX_MESSAGE_SIZE 20
#define MAX_DATA_SIZE MAX_MESSAGE_SIZE - PROTOCOL_SIZE

#define LOCK_PROTOCOL "_lck_"
#define UNLOCK_PROTOCOL "_ulk_"
#define UNKNOWN_PROTOCOL "_unk_"
#define GETSTATE_PROTOCOL "_sts_"

#define SIGNUP_PASSWORD_PROTOCOL "_sup_"
#define SIGNUP_EMAIL_PROTOCOL "_sue_"

#define SIGNIN_PASSWORD_PROTOCOL "_sip_"
#define SIGNIN_EMAIL_PROTOCOL "_sie_"

#define ERR_PROTOCOL "_err_"
#define ACK_PROTOCOL  "_ack_"


String getProtocolData(String message){
  if(message.length() <= PROTOCOL_SIZE)return "";
  return message.substring(PROTOCOL_SIZE);
}

//Signup;
String _handleSignupPassword(String password){
    if(DOOR_UNKNOWN != load_state())return ERR_PROTOCOL;
    
    String pwd = getProtocolData(password);
    dump_password(pwd);
    return ACK_PROTOCOL;
}

String _handleSignupEmail(String email){
    if(DOOR_UNKNOWN != load_state())return ERR_PROTOCOL;
    
    String eml = getProtocolData(email);
    dump_email(eml);
    return ACK_PROTOCOL;
}


//Signin;
String _handleSigninPassword(String password){
  if(DOOR_UNKNOWN != load_state())return ERR_PROTOCOL;
  String savedpwd = load_password();
  String userpwd = getProtocolData(password);
  Serial.print("SavedPWD= ");
  Serial.print(savedpwd);
  Serial.print(" UserPWD= ");
  Serial.println(userpwd);
  if(savedpwd == userpwd)return ACK_PROTOCOL;
  else return ERR_PROTOCOL;
}

String _handleSigninEmail(String email){
  if(DOOR_UNKNOWN != load_state())return ERR_PROTOCOL;
  String savedemail = load_email();
  String useremail = getProtocolData(email);
  Serial.print("SavedEmail= ");
  Serial.print(savedemail);
  Serial.print(" UserEmail= ");
  Serial.println(useremail);
  if(savedemail == useremail)return ACK_PROTOCOL;
  else return ERR_PROTOCOL;
}

//State;
String _handleGetstate(String protocol){
  if(load_state() == DOOR_LOCKED)return LOCK_PROTOCOL;
  else if(load_state() == DOOR_UNLOCKED)return UNLOCK_PROTOCOL;
  return UNKNOWN_PROTOCOL;
}

String _openDoor(String protocol){
  MyDoor.open();
  return ACK_PROTOCOL;
}

String _closeDoor(String protocol){
  MyDoor.close();
  return ACK_PROTOCOL;
}

String _secretProtocol(String protocol){
  dump_state(DOOR_UNKNOWN);
  return ACK_PROTOCOL;
}

void beginProtocols(Communication * comm){
  comm->subscribe(SIGNUP_PASSWORD_PROTOCOL, &_handleSignupPassword);
  comm->subscribe(SIGNUP_EMAIL_PROTOCOL, &_handleSignupEmail);

  comm->subscribe(SIGNIN_PASSWORD_PROTOCOL, &_handleSigninPassword);
  comm->subscribe(SIGNIN_EMAIL_PROTOCOL, &_handleSigninEmail);
  
  comm->subscribe(GETSTATE_PROTOCOL, &_handleGetstate);
  comm->subscribe(LOCK_PROTOCOL, &_openDoor);
  comm->subscribe(UNLOCK_PROTOCOL, &_closeDoor);
  comm->subscribe(UNKNOWN_PROTOCOL, &_secretProtocol);
}

#endif

/*
TEJ3M-Unit #2-07 arduino
created by Sophie Nguyen 
created on Apr 1

servo turns depending on distance from sonar
*/

#include <Servo.h>

Servo servoNumber1;

//constants
const int TRIG_PIN = 3;  
const int ECHO_PIN = 2; 
const float SPEED_OF_LIGHT = 0.0343;

//variables
float duration, distance;  

//setup
void setup() {  
   // setup servo pins
   servoNumber1.attach(4);
   servoNumber1.write(0);
  //pins for sonar
   pinMode(TRIG_PIN, OUTPUT);  
   pinMode(ECHO_PIN, INPUT); 
   Serial.begin(9600);  
}  


//loop
void loop() {  
  //clears the trig pin
  digitalWrite(TRIG_PIN, LOW);  
  delayMicroseconds(2);  

  //sets trig pin on high fpr 10 micro seconds
  digitalWrite(TRIG_PIN, HIGH);  
  delayMicroseconds(10);  
  digitalWrite(TRIG_PIN, LOW);  

  //reads the echo pin, returns the sound wave travel time in microseconds
  duration = pulseIn(ECHO_PIN, HIGH);  

  distance = duration*SPEED_OF_LIGHT/2;
  Serial.print(distance);
  
  if (distance < 50){
    servoNumber1.write(90);
    delay(500);
    servoNumber1.write(0);
    delay(500);
  }

}
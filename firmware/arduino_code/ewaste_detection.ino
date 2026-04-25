#include <Servo.h>

Servo sorter;
int sensorPin = 7;

void setup() {
  pinMode(sensorPin, INPUT);
  sorter.attach(9);
  Serial.begin(9600);
}

void loop() {

  int objectDetected = digitalRead(sensorPin);

  if(objectDetected == LOW)
  {
    Serial.println("Object detected");

    delay(2000);

    sorter.write(90);
    delay(2000);

    sorter.write(0);
    delay(2000);

    if(Serial.available())
{
  char data = Serial.read();

  if(data == '1') sorter.write(30);
  else if(data == '2') sorter.write(60);
  else if(data == '3') sorter.write(90);
  else if(data == '4') sorter.write(120);
}
  }
}

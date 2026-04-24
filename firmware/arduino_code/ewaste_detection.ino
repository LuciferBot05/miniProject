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
  }
}

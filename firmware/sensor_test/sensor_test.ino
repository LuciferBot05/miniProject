int sensorPin = 7;   // IR sensor OUT connected to pin 7

void setup() {
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
}

void loop() {

  int sensorValue = digitalRead(sensorPin);

  if (sensorValue == LOW) {
    Serial.println("Object Detected");
  } else {
    Serial.println("No Object");
  }

  delay(500); // delay for stability
}

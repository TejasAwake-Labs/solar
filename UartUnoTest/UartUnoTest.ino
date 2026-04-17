void setup() {
  Serial.begin(9600);   // This is BOTH USB and RX/TX
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    Serial.print(c);   // Echo back
  }
  else{
    Serial.println("Hello from Arduino");
    delay(1000);
  }
}
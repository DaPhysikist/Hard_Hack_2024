int emgVal = 0;
int count = 0;
const int emgPin = A0;
const int buzzPin = 8;
const int thres = 400;
const int time = 500;
int buzzFlag = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Read until newline character
    if (input == "Sleepy") {
      buzzFlag = 1;
      count = 0;
    }
  }

  Serial.println(analogRead(emgPin));
  if (buzzFlag == 1) {
    tone(buzzPin, 1000);
  }
  if (analogRead(emgPin) > thres) {
    count++;
  }
  if (count > time) {
    buzzFlag = 0;
    noTone(buzzPin);
  }
  delay(10);
}
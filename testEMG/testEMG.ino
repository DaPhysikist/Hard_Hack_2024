int emgVal = 0;
int count = 0;
const int emgPin = A0;
const int buzzPin = 8;
int buzzFlag = 1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String input = Serial.readString();
  if(input == "Sleepy"){
    buzzFlag = 1;
  }
  Serial.println(analogRead(emgPin));
  if (buzzFlag == 1) {
    tone(buzzPin, 1000);
  }
  if (analogRead(emgPin) > 150) {
    count++;
  }
  if (count > 300)
    buzzFlag = 0;
    noTone(buzzPin);
}
#define FSR A5
int fsrReading;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(FSR, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  fsrReading = analogRead(FSR);
  Serial.println(fsrReading);
  delay(100);
}

#define FSR1 A5
#define FSR2 A4
#define FSR3 A3
#define FSR4 A2
#define SIZE_OF_OUTPUT 2

int output[SIZE_OF_OUTPUT];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(FSR1, INPUT);
  pinMode(FSR2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  output[0] = analogRead(FSR1);
  output[1] = analogRead(FSR2);
  for(int i = 0; i < SIZE_OF_OUTPUT; i++)
  {
    Serial.print(output[i]);
    if(i == SIZE_OF_OUTPUT-1)
      break;
    else
      Serial.print(',');
  }
  Serial.print('\n');
  delay(10);
  }

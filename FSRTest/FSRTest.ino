#define FSR1 A5
#define FSR2 A4
#define FSR3 A6
#define FSR4 A7
#define SIZE_OF_OUTPUT 4

int output[SIZE_OF_OUTPUT];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(FSR1, INPUT);
  pinMode(FSR2, INPUT);
  pinMode(FSR3, INPUT);
  pinMode(FSR4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  output[0] = analogRead(FSR1);
  output[1] = analogRead(FSR2);
  output[2] = analogRead(FSR3);
  output[3] = analogRead(FSR4);
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

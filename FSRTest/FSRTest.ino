// Seat sensors
#define FSR1 A5
#define FSR2 A4
#define FSR3 A6
#define FSR4 A7

// Back sensors
#define FSR5 A0 // top right
#define FSR6 A1 // top left
#define FSR7 A2 // bottom right
#define FSR8 A3 //bottom left

// Size of output array
#define SIZE_OF_OUTPUT 8

int output[SIZE_OF_OUTPUT];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(FSR1, INPUT);
  pinMode(FSR2, INPUT);
  pinMode(FSR3, INPUT);
  pinMode(FSR4, INPUT);
  pinMode(FSR5, INPUT);
  pinMode(FSR6, INPUT);
  pinMode(FSR7, INPUT);
  pinMode(FSR8, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  output[0] = analogRead(FSR1);
  output[1] = analogRead(FSR2);
  output[2] = analogRead(FSR3);
  output[3] = analogRead(FSR4);
  output[4] = analogRead(FSR5);
  output[5] = analogRead(FSR6);
  output[6] = analogRead(FSR7);
  output[7] = analogRead(FSR8);
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

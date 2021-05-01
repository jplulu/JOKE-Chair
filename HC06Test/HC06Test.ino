#include <Arduino.h>
#include <SoftwareSerial.h>

// Seat sensors
#define BOT1 A4
#define BOT2 A5 
#define BOT3 A6 
#define BOT4 A7 
#define BOT5 A8
#define BOT6 A9
#define BAC1 A1
#define BAC2 A2
#define BAC3 A3
#define BAC4 A4

// Size of output array
#define SIZE_OF_OUTPUT 10
#define SIZE_BYTES 20

SoftwareSerial BT(10, 11); // RX, TX
uint16_t output[SIZE_OF_OUTPUT];
uint8_t outputBytes[SIZE_BYTES];


 
void setup() 
{
  // put your setup code here, to run once:
  //Serial.begin(9600);
  BT.begin(9600);
  BT.println("Bluetooth On");
  pinMode(BOT1, INPUT);
  pinMode(BOT2, INPUT);
  pinMode(BOT3, INPUT);
  pinMode(BOT4, INPUT);
  pinMode(BOT5, INPUT);
  pinMode(BOT6, INPUT);
  pinMode(BAC1, INPUT);
  pinMode(BAC2, INPUT);
  pinMode(BAC3, INPUT);
  pinMode(BAC4, INPUT);
}
 
void loop() 
{
  output[0] = analogRead(BOT1);
  output[1] = analogRead(BOT2);
  output[2] = analogRead(BOT3);
  output[3] = analogRead(BOT4);
  output[4] = analogRead(BOT5);
  output[5] = analogRead(BOT6);
  output[6] = analogRead(BAC1);
  output[7] = analogRead(BAC2);
  output[8] = analogRead(BAC3);
  output[9] = analogRead(BAC4);
  for(int i = 0; i < SIZE_OF_OUTPUT; i++){
    outputBytes[2*i] = output[i];
    outputBytes[2*i + 1] = output[i] >> 8;
  }
  #ifdef PRINT_SERIAL
    for(int i = 0; i < SIZE_OF_OUTPUT; i++)
    {
      Serial.print(output[i]);
      if(i == SIZE_OF_OUTPUT-1)
        break;
      else
        Serial.print(',');
    }
    Serial.print('\n');
    for(int i = 0; i < SIZE_OF_OUTPUT; i++)
    {
      Serial.print(outputBytes[2*i]);
      Serial.print("|");
      Serial.print(outputBytes[2*i+1]);
      if(i == SIZE_OF_OUTPUT-1)
        break;
      else
        Serial.print(',');
    }
    Serial.print('\n');
  #endif
  BT.write(outputBytes, SIZE_BYTES);
  delay(100);// prepare for next data ...
}
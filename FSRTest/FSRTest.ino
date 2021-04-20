#include "BluetoothSerial.h"
#include <Arduino.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

// Seat sensors
#define BOT1 25
#define BOT2 33 
#define BOT3 32 
#define BOT4 35 
#define BOT5 34
#define BOT6 39
#define BAC1 12
#define BAC2 14
#define BAC3 27
#define BAC4 26

// Size of output array
#define SIZE_OF_OUTPUT 10
#define SIZE_BYTES 20


BluetoothSerial SerialBT;

uint16_t output[SIZE_OF_OUTPUT];
uint8_t outputBytes[SIZE_BYTES];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  //SerialBT.begin("ESP32test"); //Bluetooth device name
  //Serial.println("The device started, now you can pair it with bluetooth!");
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

void loop() {
  // put your main code here, to run repeatedly:
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
  for(int i = 0; i < SIZE_OF_OUTPUT; i++)
  {
    Serial.print(output[i]);
    if(i == SIZE_OF_OUTPUT-1)
      break;
    else
      Serial.print(',');
  }
  Serial.print('\n');

  for(int i = 0; i < SIZE_OF_OUTPUT; i++){
    outputBytes[2*i] = output[i];
    outputBytes[2*i + 1] = output[i] >> 8;
  }
  SerialBT.write(outputBytes, 20);
  delay(10);
}

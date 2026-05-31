#include <Keypad.h>
int buzzer = 0 ;
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {13, 12, 11, 10}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
 pinMode(0, OUTPUT);  
}
  
void loop(){
  char customKey = customKeypad.getKey();
  
  if (customKey){
    Serial.println(customKey);
    if(customKey == '1')
    {

    
      digitalWrite(3, 1);
    }
    else if(customKey == '2')
    {
      digitalWrite(4, 1);
    }
    else if(customKey == '3')
    {
      digitalWrite(5, 1);
    }
    else if(customKey == '0')
    {
      digitalWrite(5, 0);
      digitalWrite(4, 0);
      digitalWrite(3, 0);
    }
  }
}

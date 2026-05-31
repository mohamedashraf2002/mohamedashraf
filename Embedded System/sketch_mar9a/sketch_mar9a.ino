#include <PCM.h>



int LED1 = 10;
int LED2 = 12;
int LED3 = 11;

void setup() {
  // put your setup code here, to run once:
pinMode(LED1,OUTPUT);
//pinMode(LED2,OUTPUT);
//pinMode(LED3,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite (LED1,HIGH) ;
//digitalWrite (LED2,LOW) ;
//digitalWrite (LED3,LOW) ;
delay(2000) ;
digitalWrite (LED1,LOW) ;
//digitalWrite (LED2,HIGH) ;
//digitalWrite (LED3,LOW) ;
//delay(2000) ;
//digitalWrite (LED1,LOW) ;
//digitalWrite (LED2,LOW) ;
//digitalWrite (LED3,HIGH) ;
//delay(2000) ;


}

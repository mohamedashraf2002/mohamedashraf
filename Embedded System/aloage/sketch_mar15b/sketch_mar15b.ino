



int LED1 = 2;
int brightness = 0 ;
void setup() {
  // put your setup code here, to run once:
pinMode(LED1,OUTPUT);


}

void loop() {
  


analogWrite(LED1,255);
delay(1000);
analogWrite(LED1,50);
delay(1000);
analogWrite(LED1,0);
delay(1000);




}

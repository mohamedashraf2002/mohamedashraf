int red = 0 ;
int white =1 ;
int yellow =2 ;
int push=7;
int counter = 0 ;
void setup() {
  // put your setup code here, to run once:
pinMode(red,OUTPUT);
pinMode(white,OUTPUT);
pinMode(yellow,OUTPUT);
pinMode(push,INPUT);
}
void loop() {
if(digitalRead(push)==HIGH)
{
counter++ ;
if(counter==1)
{
digitalWrite(red,HIGH);
}
else if(counter==2)
{
digitalWrite(white,HIGH);  
}
else if(counter==3)
{
digitalWrite(yellow,HIGH);  
}
else
{
digitalWrite(red,0);
digitalWrite(yellow,0);
digitalWrite(white,0);
counter = 0;
}
}
}

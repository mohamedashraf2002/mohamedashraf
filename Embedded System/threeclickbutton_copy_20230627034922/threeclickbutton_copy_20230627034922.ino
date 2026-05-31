int red = 0 ;
int yellow =1 ;
int blue=2 ;
int push1=5;
int push2=6;
int push3=7;
int counter = 0 ;
void setup() {
  // put your setup code here, to run once:
pinMode(red,OUTPUT);
pinMode(blue,OUTPUT);
pinMode(yellow,OUTPUT);
pinMode(push1,INPUT);
pinMode(push2,INPUT);
pinMode(push3,INPUT);
}
void loop() {
if(digitalRead(push1)==HIGH)
{
digitalWrite(red,HIGH);

}
if(digitalRead(push1)==LOW)
{
digitalWrite(red,LOW);  
}


if(digitalRead(push2)==HIGH)
{
digitalWrite(yellow,HIGH);

}e
if(digitalRead(push2)==LOW)
{
digitalWrite(yellow,LOW);  
}

if(digitalRead(push3)==HIGH)
{
digitalWrite(blue,HIGH);

}
if(digitalRead(push3)==LOW)
{
digitalWrite(blue,LOW);  
}

}

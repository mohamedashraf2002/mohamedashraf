void setup() {
  // put your setup code here, to run once:
pinMode(3,INPUT);
pinMode(2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    int pusshed = digitalRead(3);
    if(pusshed == LOW)
{
digitalWrite(2,HIGH);
}    
else{
digitalWrite(2,LOW);  
}
    
}

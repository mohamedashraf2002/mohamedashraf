int sen = 7;
int led =9; 
String ledstate ="off";
void setup() {
  // put your setup code here, to run once:
pinMode(sen,INPUT);
pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

if(digitalRead(sen)==1)
{   
    if(ledstate=="off")
    {
       digitalWrite(led,HIGH);
       ledstate ="on";         
    }  
   else if (ledstate=="on")
    {
      digitalWrite(led,LOW);   
      ledstate ="off";        
    }
    delay(200);
   
}

}


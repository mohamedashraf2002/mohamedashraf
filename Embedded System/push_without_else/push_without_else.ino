int blue=2 ;
int push=7;
void setup() {
  // put your setup code here, to run once:

pinMode(blue,OUTPUT);
pinMode(push,INPUT);
}
void loop() {
if(digitalRead(push)==HIGH)
{

digitalWrite(blue,HIGH);
}
 else if (digitalRead(push)==LOW)
 {
 digitalWrite(blue,LOW);
  }
// طلما مفيش elseهيفضل ينقذ اخر قيمه محتفظ بيه
delay(250);
}

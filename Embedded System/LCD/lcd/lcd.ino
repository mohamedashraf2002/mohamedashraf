//RS,E,,D4,D5,D6,D7
#include <LiquidCrystal.h>
LiquidCrystal lcd (3,4,5,6,7,8);  
void setup() {
  // put your setup code here, to run once:

lcd.begin(16,2);
 

}

void loop() {
  // put your main code here, to run repeatedly:
ld();



}
void ld ()
{
lcd.setCursor(2,0);
lcd.print("REAL MADRID VS");

lcd.setCursor(2,1);
lcd.print("BARCELONA");

delay(3000);
lcd . clear();

lcd.setCursor(3,0);
lcd.print("COUNTRY");
lcd.setCursor(3,1);
lcd.print("EYGPT");
delay(3000);

lcd.clear();

lcd.setCursor(3,0);
lcd.print("TIME");
lcd.setCursor(3,1);
lcd.print("21:00");
delay(3000);

lcd.clear();

lcd.setCursor(3,0);
lcd.print("RESULT");
lcd.setCursor(3,1);
lcd.print("4:0 FOR REAL");
delay(3000);

lcd.clear();
}
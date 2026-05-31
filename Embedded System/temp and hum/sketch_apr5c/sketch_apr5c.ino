#include <LiquidCrystal.h>

LiquidCrystal lcd (2,3,4,5,0,1); 
#include <DHT.h>
DHT dht(2,DHT11);
int temp ;
int humidity;
void setup() {
  // put your setup code here, to run once:

lcd.begin(16,2);
 dht.begin();


}

void loop() {
  // put your main code here, to run repeatedly:
delay(2000);
temp = dht.readTemperature();
humidity=dht.readHumidity();
lcd.setCursor(0,0);
lcd.print("TEMP :");
lcd.print(temp);
lcd.print("c");
lcd.setCursor(0,1);
lcd.print("humidity:");
lcd.print(humidity);
lcd.print("%");
}

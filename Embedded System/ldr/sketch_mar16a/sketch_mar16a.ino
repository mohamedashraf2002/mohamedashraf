float input_pin = A0;//Analog Pin
// Variables reservation
int led = 2 ;
float input_value , ldr_resistor , ldr_voltage , ldr_current , lux;
void setup() 
{
  // start the serial monitor with 9600 bps baud rate
  Serial.begin(9600);
  pinMode(led,OUTPUT) ;
pinMode(input_pin,INPUT) ;  
}
void loop() 
{
  // Read the analog pin
  
  input_value = analogRead(input_pin);
  // convert the value range (0-1023) to (0-5V)
input_value = (input_value  / 1023)*5 ;  
Serial.println(input_value);    

  if(input_value > 0.20)
  {
digitalWrite(led,HIGH);
  }
else
{
  digitalWrite(led,LOW);
  
}
  // Measure the voltage dropped on LDR resistor
  //ldr_voltage = 5 - input_value;
  // Measure the current that flow in a series circuit (R1+LDR)
  //ldr_current = ldr_voltage / 10000 ; //  "I=V/R" : R1=10KOHM
  // Calculate The LDR resistor "R=V/I"
  //ldr_resistor = ldr_voltage / ldr_current ; // LDR resdidtor in OHM
  // Convert Resistor mesurment Unit to KOHM
  //ldr_resistor = ldr_resistor / 1000 ;
  // Calculate the luminiere in LUX
  //lux = 5000 / ldr_resistor ;
  // Print the Values
 // Serial.print("lux = ");
  //Serial.println(lux);
  // Delays between readings
  
}
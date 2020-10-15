#include <DHT.h>
int SENSOR = 12;
int temperatura, humedad;
DHT dht (SENSOR, DHT11);
void setup() {
  pinMode(SENSOR, INPUT);
  digitalWrite(SENSOR, HIGH);
  Serial.begin(19200);
  dht.begin();
}

void loop() {
 temperatura = dht.readTemperature();
 Serial.print(temperatura);
 Serial.println(";"); 
 delay(1000);
 exit;
 
 humedad = dht.readHumidity(); 
 Serial.print(humedad); 
 Serial.println(";"); 
 delay(2000);
 exit;
 /* Serial.println(""); */
 /* Serial.print("Temperatura:");*/
 /* Serial.println(" Celsius");*/ 
 /* Serial.print("Humedad:"); */
 /* Serial.print("%"); */
}

#include <DHT.h>
int SENSOR = 12;
int temperature, humidity;
DHT dht (SENSOR, DHT11);
void setup() {
  pinMode(SENSOR, INPUT);
  digitalWrite(SENSOR, HIGH);
  Serial.begin(19200);
  dht.begin();
}

void loop() {
 temperature = dht.readTemperature();
 Serial.print(temperature);
 Serial.println(";"); 
 delay(1000);
 exit;
 
 humidity = dht.readHumidity(); 
 Serial.print(humidity); 
 Serial.println(";"); 
 delay(2000);
 exit;
 /* Serial.println(""); */
 /* Serial.print("Temperature:");*/
 /* Serial.println(" Celsius");*/ 
 /* Serial.print("RH:"); */
 /* Serial.print("%"); */
}

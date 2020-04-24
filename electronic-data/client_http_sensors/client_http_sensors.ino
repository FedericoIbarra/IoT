#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DHT11.h> 
#include <Servo.h>
// Parametros y variables para conexion a WIFI y server
const char* ssid = "Infinitum2019";
const char* password = "PalomaPerra2019";
const char* host = "54.161.195.215";
const uint16_t port = 5000;
const char* uri = "/api/data";
// Variables de sensores
//PH
#define SensorPin A0          //pH meter Analog output to Arduino Analog Input 0
unsigned long int avgValue;  //Store the average value of the sensor feedback
float b;
int buf[10],temp;
//Temperatura y humedad
//float temp = 16.5;
#define SensorTH 16
DHT11 dht11(SensorTH);
//String data = "Temperature: " + temp;
//bool begin(WiFiClient &client, String host, uint16_t port, String uri = "/api/data", bool https = false);
/////////
//Actuador
Servo myservo;  // create servo object to control a servo
int pos;
/////////
void setup()
{
   Serial.begin(115200);
   delay(10);
   //Set de pin digital para temperatura y humedad
   pinMode(SensorTH, INPUT);
   //Set de pin analogico para PH
   pinMode(SensorPin, INPUT);
   //Set pin para el actuador
   myservo.attach(2);  
   // Conectar WiFi
   WiFi.begin(ssid, password);
   
   Serial.println();
   Serial.println();
   Serial.print("Wait for WiFi... ");
  
   while (WiFi.status() != WL_CONNECTED){ 
      Serial.print(".");
      delay(500);
   }
   Serial.println("");
   Serial.println("WiFi connected");
   Serial.println("IP address: ");
   Serial.println(WiFi.localIP());
   Serial.print("connecting to ");
   Serial.print(host);
   Serial.print(':');
   Serial.println(port);
  
}
 
void loop()
{
   HTTPClient http;
   WiFiClient client;
   String myString;
   String myString1;
   String myString2;
   if (http.begin(client, host, port, uri)) //Iniciar conexión
   {
      Serial.print("[HTTP] GET...\n");
      int httpCode = http.GET();  // Realizar petición
      
      if (httpCode > 0) {
         Serial.printf("[HTTP] GET... code: %d\n", httpCode);
 
         if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
            String payload = http.getString();   // Obtener respuesta
            Serial.println(payload);   // Mostrar respuesta por serial
            pos = payload.toInt();
         }
      }
      else {
         Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }

      //Actuador
      Serial.println(pos);
      myservo.write(pos); 
      //////////
      //Ph sensor
      for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
      { 
        buf[i]=analogRead(SensorPin);
        delay(10);
      }
      for(int i=0;i<9;i++)        //sort the analog from small to large
      {
        for(int j=i+1;j<10;j++)
        {
          if(buf[i]>buf[j])
          {
            temp=buf[i];
            buf[i]=buf[j];
            buf[j]=temp;
          }
        }
      }
      avgValue=0;
      for(int i=2;i<8;i++)                      //take the average value of 6 center sample
        avgValue+=buf[i];
      float phValue=(float)avgValue*5.0/1024/6; //convert the analog into millivolt
      phValue=3.5*phValue;                      //convert the millivolt into pH value
      myString = String(phValue);
      Serial.print("    pH:");  
      Serial.print(phValue,2);
      Serial.println(" ");
      ////////////////
      //Sensor de temperatura y humedad
      int err;
      float temp, humi;
      if((err=dht11.read(humi, temp))==0)
      {
        Serial.print("temperature:");
        Serial.print(temp);
        Serial.print(" humidity:");
        Serial.print(humi);
        Serial.println();
        myString1 = String(temp);
        myString2 = String(humi);
      }
      else
      {
        Serial.println();
        Serial.print("Error No :");
        Serial.print(err);
        Serial.println();    
      }
      ////////////////
      ///////////////
      int httpSensor = http.POST("NODE MCU 1,Ph:" + myString + "," +"Temperatura:" + myString1 + "," +"Humedad:" + myString2 +",");
      String payload2 = http.getString();
      Serial.println(httpSensor);
      Serial.println(payload2);

 
      http.end();
   }
   else {
      Serial.printf("[HTTP} Unable to connect\n");
   }
 
   delay(30000);
}

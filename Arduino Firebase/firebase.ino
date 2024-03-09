#include <Arduino.h>
#include <ESP8266Firebase.h>
#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ESP8266)
  #include <ESP8266WiFi.h>
#endif

#include <Firebase_ESP_Client.h>
#include <Wire.h>

#include "addons/TokenHelper.h"

#include "addons/RTDBHelper.h"

#include <DHT.h>
#include <DHT_U.h>

// Insert your network credentials
#define WIFI_SSID "Tec-Contingencia"
#define WIFI_PASSWORD ""

// Insert Firebase project API Key
#define API_KEY "AIzaSyDKBSRE3PKgbuaQk6wfvhePt2zxkHrnZNQ"

// Insert Authorized Email and Corresponding Password
#define USER_EMAIL "potyjr@gmail.com"
#define USER_PASSWORD "potyjr"

// Insert RTDB URL
#define DATABASE_URL "https://esp32-2fbae-default-rtdb.firebaseio.com/"

// Define Firebase objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// Variable to save USER UID
String uid;

// Variables to save database paths
String databasePath;
String tempPath;
String humPath;
String coPath;
String gasPath;

// MQ135 sensor pin
const int MQ135_ANALOG_PIN = A0;
const int LED_VERDE = D1;
const int LED_ROJO = D2;
const int LED_AMARILLO = D5;

int SENSOR_DHT11 = D4; // Pin del sensor DHT11
int TEMPERATURA;
int HUMEDAD;

DHT dht(SENSOR_DHT11, DHT11);

unsigned long sendDataPrevMillis = 0;
unsigned long timerDelay = 2000;

void initWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  Serial.println();
}

void sendFloat(String path, float value) {
  if (Firebase.RTDB.setFloat(&fbdo, path.c_str(), value)) {
    Serial.print("Writing value: ");
    Serial.print(value);
    Serial.print(" on the following path: ");
    Serial.println(path);
    Serial.println("PASSED");
    Serial.println("PATH: " + fbdo.dataPath());
    Serial.println("TYPE: " + fbdo.dataType());
  } else {
    Serial.println("FAILED");
    Serial.println("REASON: " + fbdo.errorReason());
  }
}

void setup() {
  Serial.begin(115200);

  initWiFi();

  config.api_key = API_KEY;
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;
  config.database_url = DATABASE_URL;

  Firebase.reconnectWiFi(true);
  fbdo.setResponseSize(4096);
  config.token_status_callback = tokenStatusCallback;

  config.max_token_generation_retry = 5;
  Firebase.begin(&config, &auth);

  Serial.println("Getting User UID");
  while ((auth.token.uid) == "") {
    Serial.print('.');
    delay(1000);
  }
  uid = auth.token.uid.c_str();
  Serial.print("User UID: ");
  Serial.println(uid);

  databasePath = "/UsersData/" + uid;
  tempPath = databasePath + "/temperatura";
  humPath = databasePath + "/humedad";
  coPath = databasePath + "/concentracion";
  gasPath= databasePath + "/gas";

}

void loop() {
  if (Firebase.ready() && (millis() - sendDataPrevMillis > timerDelay || sendDataPrevMillis == 0)){
    sendDataPrevMillis = millis();

    // Read data from MQ135 sensor
    int sensorValue = analogRead(MQ135_ANALOG_PIN);
    float concentrationCO2 = map(sensorValue, 0, 1023, 0, 1000);
    float concentrationGas = map(sensorValue, 0, 1023, 0, 100);

    TEMPERATURA = dht.readTemperature();
    HUMEDAD = dht.readHumidity();

    // Send data to Firebase
    sendFloat(tempPath, TEMPERATURA);
    sendFloat(humPath, HUMEDAD);
    sendFloat(coPath, concentrationCO2);
    sendFloat(gasPath, concentrationGas);

    delay(10);
  }
}
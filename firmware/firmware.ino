#define cnyPin 3
int deger = 0;
void setup() {
  pinMode(cnyPin, OUTPUT);
  Serial.begin(115200);
  

}

void loop() {
  deger = digitalRead(cnyPin);
  if(Serial.available() > 0){
    Serial.println(deger);
    }

}

void setup() {
 Serial.begin(9600);
 Serial.println("==={BEGIN}===");
}

void loop() {
 char c;
 while (Serial.available()) {
  c = Serial.read();
  Serial.print(c);
  // 131 octave 1
  if (c == 'a') {
   tone(8, 131, 250);
  }
  if (c == 'A') {
   tone(8, 139, 250);
  }
  if (c == 'b') {
   tone(8, 147, 250);
  }
  if (c == 'B') {
   tone(8, 156, 250);
  }
  if (c == 'c') {
   tone(8, 165, 250);
  }
  if (c == 'd') {
   tone(8, 175, 250);
  }
  if (c == 'D') {
   tone(8, 185, 250);
  }
  if (c == 'e') {
   tone(8, 196, 250);
  }
  if (c == 'E') {
   tone(8, 208, 250);
  }
  if (c == 'f') {
   tone(8, 220, 250);
  }
  if (c == 'F') {
   tone(8, 233, 250);
  }
  if (c == 'g') {
   tone(8, 247, 250);
  }
  
  // 262 octave 2
  if (c == 'h') {
   tone(8, 262, 250);
  }
  if (c == 'H') {
   tone(8, 277, 250);
  }
  if (c == 'i') {
   tone(8, 294, 250);
  }
  if (c == 'I') {
   tone(8, 311, 250);
  }
  if (c == 'j') {
   tone(8, 330, 250);
  }
  if (c == 'k') {
   tone(8, 349, 250);
  }
  if (c == 'K') {
   tone(8, 370, 250);
  }
  if (c == 'l') {
   tone(8, 392, 250);
  }
  if (c == 'L') {
   tone(8, 415, 250);
  }
  if (c == 'm') {
   tone(8, 440, 250);
  }
  if (c == 'M') {
   tone(8, 466, 250);
  }
  if (c == 'n') {
   tone(8, 494, 250);
  }
  
  // 65 octave 3
  if (c == 'o') {
   tone(8, 65, 250);
  }
  if (c == 'O') {
   tone(8, 69, 250);
  }
  if (c == 'p') {
   tone(8, 74, 250);
  }
  if (c == 'P') {
   tone(8, 78, 250);
  }
  if (c == 'q') {
   tone(8, 83, 250);
  }
  if (c == 'r') {
   tone(8, 87, 250);
  }
  if (c == 'R') {
   tone(8, 92.5, 250);
  }
  if (c == 's') {
   tone(8, 98, 250);
  }
  if (c == 'S') {
   tone(8, 104, 250);
  }
  if (c == 't') {
   tone(8, 110, 250);
  }
  if (c == 'T') {
   tone(8, 117, 250);
  }
  if (c == 'u') {
   tone(8, 123, 250);
  }
  if (c == '-') {
   delay(250);
  }
  if (c == '$') {
    Serial.println();
  }
 }
}

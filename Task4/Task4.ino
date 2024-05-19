/*SO in my program i take input from a keypad and display the numbers on lcd
for encryption i devised a plan to convert number to binary then to xor with a given key that is 65537
I store the key in non volatile memory of arduino using eeprom library
These are pins for keypad 
rowPins[ROWS] = {5, 4, 3, 2}; 
colPins[COLS] = {9, 8, 7, 6}; 
These for lcd
 rs = 13, en = 12, d4 = 11, d5 =10 , d6 = 1, d7 = 0;*/
#include <Keypad.h>
#include <Wire.h> 
#include <EEPROM.h>
#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 11, d5 =10 , d6 = 1, d7 = 0;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
//

int myNum[4];
int i=0;

const byte ROWS = 4; 
const byte COLS = 4; 
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad 8,7,6,5
byte colPins[COLS] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad 4,3,2,1
Keypad k = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS );



const unsigned int KEY = 65537; // The key for XOR operation

// Function to reverse the bits of a 16-bit unsigned integer
unsigned int reverseBits(unsigned int num) {
  unsigned int reversedNum = 0;
  for (int i = 0; i < 16; ++i) {
    if (num & (1 << i)) {
      reversedNum |= 1 << ((16 - 1) - i);
    }
  }
  return reversedNum;
}

// Function to encrypt a 4-digit number
unsigned int encryptCode(unsigned int number) {
  if (number > 9999) {
    Serial.println("Error: Number must be a 4-digit number.");
    return 0;
  }
  unsigned int reversedNumber = reverseBits(number);
  unsigned int encryptedNumber = reversedNumber ^ KEY;
  return encryptedNumber;
}

unsigned int decryptCode(unsigned int encryptedNumber) {
  unsigned int reversedNumber = encryptedNumber ^ KEY;
  unsigned int originalNumber = reverseBits(reversedNumber);
  return originalNumber;
}


// Function to write the encrypted code to EEPROM
//I am putting data at address 0 
void writeCodeToEEPROM(unsigned int code) {
    unsigned int encryptedCode = encryptCode(code);
    EEPROM.put(0, encryptedCode);
}

// Function to read the encrypted code from EEPROM and decrypt it
unsigned int readCodeFromEEPROM() {
    unsigned int encryptedCode;
    EEPROM.get(0, encryptedCode);
    return decryptCode(encryptedCode);
}

// Function to verify if the user-entered code matches the stored code
bool verifyCode(unsigned int userCode) {
    unsigned int storedCode = readCodeFromEEPROM();
    return userCode == storedCode;
}


void setup() {
  Serial.begin(9600); 
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Enter Key:");
  writeCodeToEEPROM(6969);

}



void loop() { // request for input
  char key_pressed = k.getKey();
  for (int i = 0; i < 4;){
    if(key_pressed) {
      myNum[i] = key_pressed;
      lcd.setCursor(i,1);
      lcd.print(key_pressed);
      i = i+1;
    }
  }
  int num=0;
  for(int k=0;k<4;k++){
    num=num+pow(10,i);
  }
delay(1000);
lcd.clear();
  if (verifyCode(num)) {
    lcd.print("Access Granted");
} else {
    lcd.print("Access Denied");
}
  // Serial.print(myNum);
  // char key_pressed = k.getKey();
  delay(500);

}
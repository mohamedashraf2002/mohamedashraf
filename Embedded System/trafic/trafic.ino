/*
  Melody

  Plays a melody

  circuit:
  - 8 ohm speaker on digital pin 8

  created 21 Jan 2010
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody
*/

#include "pitches.h"
int LED1 = 10;
int LED2 = 11;
int LED3 = 12;

// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {
pinMode(LED1,OUTPUT);
pinMode(LED2,OUTPUT);
pinMode(LED3,OUTPUT);    
    // to calculate the note duration, take one second divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
   int noteDuration = 1000 / noteDurations[thisNote];
    tone(3, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(3);

  }
}

void loop() {
  // no need to repeat the melody.
digitalWrite (LED1,HIGH) ;
digitalWrite (LED2,LOW) ;
digitalWrite (LED3,LOW) ;
delay(2000) ;
digitalWrite (LED1,LOW) ;
digitalWrite (LED2,HIGH) ;
digitalWrite (LED3,LOW) ;
delay(2000) ;
digitalWrite (LED1,LOW) ;
digitalWrite (LED2,LOW) ;
digitalWrite (LED3,HIGH) ;
delay(2000) ;  
 
}

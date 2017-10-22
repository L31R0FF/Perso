#include "stdio.h"
#define LISTNB 3

int main(int argc, char *argv[]) {
  char list[LISTNB] = {'A','B','C'};
  int i, i2, i3;
  
  for (i = 0; i < LISTNB; i++) {
    for (i2 = 0; i2 < LISTNB; i2++) {
      for (i3 = 0; i3 < LISTNB; i3++) {
        printf("%c%c%c\n", list[i],list[i2],list[i3]);
      }
    }  
  }
  
  return 0;
}

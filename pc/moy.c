#include "stdio.h"

int main(int argc, char *argv[]) {
  int moy = 0;
  int sum = 0;
  int nb = 0;
  int note = 0;
  
  while (1) {
    printf("Note: ");
    scanf("%i", &note);
    if (note == 99) {
      break;
    }
    sum = sum + note;
    nb++;
  }
  moy = sum/nb;
  printf("moyenne: %i\n", moy);
  
  return 0;
}

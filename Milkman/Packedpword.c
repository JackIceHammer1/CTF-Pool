#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char pword[] = "Mrbones";
    if(!strcmp(pword, argv[1])){
        printf("lbctf{qwembo88} \n");
        exit(0);
    } else {
        printf("RELEASE THE CALCIUM\n");
        exit(1);
    }
}

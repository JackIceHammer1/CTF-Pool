#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[10];
    int pass = 0;

    printf("\n Welcome to the town of Ignatium. You are now in the care of Steve the wizard. He has but one question for you. What is the best way to keep 7 horses and 3 sheep from living in close proximity? Furthermore, make sure that these said animals do not endager the lives of the three lions that we have next door. Also, I am 7000 years old, only to be outlived by the founder of our town himself. Regardless, what is the shape of the sun? \n");
    gets(buff);

    if(strcmp(buff, "theJakeProject"))
    {
        printf ("\n Incorrect \n");
    }
    else
    {
        printf ("\n Correct\n");
        pass = 1;
    }

    if(pass)
    {
       /* Now Give root or admin rights to user*/
        printf ("\n lbctf{8282} \n");
    }

    return 0;
}

#include <stdio.h>

// This is not the flag!
// Seriously! You will not get points for it.

// Use this code to test your exploit 
// locally, and when you're ready run
// it over the network.

#define FLAG "LBCTF{th3_h4ck3r_kn0wn_4s_k1ndt1m3}"

int main(void)
{

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    int authenticated = 0x1234;

    char buf[128];
    
    printf("\n0x%x\n", authenticated);

    while(1) {
        fgets(buf, sizeof(buf), stdin);

        printf(buf);
        
        if(authenticated == 0x53545349) {
            puts(FLAG);
            break;
        } else {
            printf("\n0x%x\n", authenticated);
            puts("Access Denied");
        }
    }

    return 0;
}

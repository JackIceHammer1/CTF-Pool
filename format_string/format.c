#include <stdio.h>

#define FLAG "LBCTF{4lw4y5_sp3c1fy_y0ur_f0rm4t_sp3c1f13r}"

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

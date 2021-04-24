#include <stdio.h>

int main(void)
{
    int x = 100;
    printf("x=%d, x=%o, x=%x\n",x,x,x);
    printf("x=%d, x=%#o, x=%#x",x,x,x);
}
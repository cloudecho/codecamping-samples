#include <stdio.h>

struct student
{
    int a;
    int b;
} aaa[3];

int main()
{
    struct student *p = aaa;
    printf("Pointer p: %p\n", (void *)p);
    printf("aaa      : %p\n", (void *)aaa);
    printf("aaa[0]   : %p\n", (void *)&aaa[0]);

    printf("p++      : %p\n", (void *)++p);
    printf("aaa[1]   : %p\n", (void *)&aaa[1]);

    printf("p++      : %p\n", (void *)++p);
    printf("aaa[2]   : %p\n", (void *)&aaa[2]);
    return 0;
}
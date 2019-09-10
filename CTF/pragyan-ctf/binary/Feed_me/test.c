#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = "-00001231232-4324324";

    printf("First number is: %d\n", atoi(s));
    printf("Second number is: %d\n", atoi(s + 8));
    return 0;
}

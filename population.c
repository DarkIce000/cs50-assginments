#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size


    int n;
    do
    {
        n = get_int("enter the intial population of the lammas: ");
    }
    while (n < 9);

    // TODO: Prompt for end size


    int m;
    do
    {
        m = get_int("enter the end population of the lammas: ");
    }
    while (m < n);

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
     while(n < m)
    {
        n = n + n/3 - n/4;
        year++;
    }

    printf ("number of years: %i\n", year);
}

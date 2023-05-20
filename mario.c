#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("height: ");
    }
    while( n<1 ||n>9 );


    //implementation of pattern


//for column printing
    int i;
    for ( i = 1; i<n; i++)
    {
            //for rows printing
        int k;
        for (k=(n-i); k>1 ; k-- )
            {
                printf(" ");
            }

            //for row printing
        int j;
        for (j=0; j < i; j++ )

           {
            printf("#");
           }
           //for priting new line after every row printed

        printf("\n");

    }

}
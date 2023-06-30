#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // getting the string
    string input = get_string("input: ");

    // convert into integer
    int array[strlen(input)];
    for (int i = 0; i < strlen(input); i++)
    {
        array[i] = input[i];
    }

    for (int i = 0; i < strlen(input); i++)
    {
        // putting the array into another array
        int bit[8];
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            // putting remainder in bit array
            if (array[i] % 2 == 1)
                bit[j] = 1;
            else
                bit[j] = 0;
            array[i] /= 2;
        }

        // for printing in right to left direction
        for (int j = 0; j < 8; j++)
        {
            print_bulb(bit[j]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

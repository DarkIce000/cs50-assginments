#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Invalid Usage!");
        return 1;
    }
    //error after not opening for reading
    FILE *inputptr = fopen(argv[1], "r");
    if ( inputptr == NULL)
    {
        printf("File cannot be opened for reading");
        return 1;
    }

    int filenumber = 0;
    char filename[10];

    FILE *output_file = NULL;
    BYTE* buffer = malloc(BLOCK_SIZE + 1);
    while (fread(buffer, 1, BLOCK_SIZE, inputptr) == BLOCK_SIZE)
    {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & (0xf0)) == 0xe0)
        {
            //close the old file
            if(output_file != NULL)
            {
                fclose(output_file);
            }
            //open a new file for writing
            sprintf(filename, "%03i.jpg", filenumber);
            output_file = fopen(filename, "w");

            fwrite(buffer, BLOCK_SIZE, 1, output_file);
            // if (output_file == NULL)
            // {

            //     printf("file cannot be opened");
            //     return 1;
            // }
            filenumber += 1;
        }
        else if (output_file != NULL)
        {
            //if the signature not found continue writing the old file
            fwrite(buffer, BLOCK_SIZE, 1, output_file);
        }
        else
            continue;
    }


    return 0;
}

#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
 //assume as a grid of 2x2 then find the black
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //finding black colour
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00)
            {
                //change to any colour;
                if(j % 2 == 1)
                {
                    image[i][j].rgbtGreen = 0xff;

                }
                else if(j % 2 != 1)
                {
                    image[j][i].rgbtBlue = 0xff;
                }
                else;
                {
                    image[i][j].rgbtRed = 0xff;
                }
            }
        }
    }
}


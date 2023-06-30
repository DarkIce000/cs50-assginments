#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // assume as a grid of 2x2 then find the black
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // finding black colour
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00)
            {
                // change to any colour;
                image[i][j].rgbtRed = 0xff;
                image[2][2].rgbtGreen = 0xff;
                image[2][5].rgbtGreen = 0xff;
            }
        }
    }
}

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //finding the avg of the rgb of each pixel
            float avg = (image[i][j].rgbtGreen + image[i][j].rgbtRed + image[i][j].rgbtBlue)/3.00;
            //chaging the each pixel to the avg value
            image[i][j].rgbtGreen = round(avg);
            image[i][j].rgbtRed = round(avg);
            image[i][j].rgbtBlue = round(avg);
        }
    }


    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //finding the avg of the rgb of each pixel
            float red, blue, green;
            red = image[i][j].rgbtRed;
            green = image[i][j].rgbtGreen;
            blue = image[i][j].rgbtBlue;
            //calculating the sepia red green and blue;

            int sepiaRed = 0.393 * red + 0.769 * green +0.189 * blue;
            if(sepiaRed > 255)
                sepiaRed = 255;
            int sepiaGreen = 0.349 * red + 0.686 * green + 0.168 * blue;
            if(sepiaGreen > 255)
                sepiaGreen = 255;
            int sepiaBlue = 0.272 * red +0.534 * green + 0.131 * blue ;
            if(sepiaBlue > 255)
                sepiaBlue = 255;

            //putting the value inthe pixel
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //copying to another array so that pixels donot get conflict with the original
    RGBTRIPLE temparray [height][width];
    for (int i = 0; i < height; i++)
    {
      for(int j = 0; j < width; j++)
      {
        temparray[i][j] = image [i][j];

      }
    }

     //now assiging the value of the array to the old array but in reverse order
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            image[i][j] = temparray[i][width-(j)];
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //copying the pixel properties to new array
    RGBTRIPLE copy_image[height][width];
    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy_image[i][j] = image[i][j];
        }
    }

    //bluring the pixels
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            if( j > 0 && i > 0 && j < width-1 && i < height-1)
            {
                //finding the avg of the middle pixels which has 8 neighbours
                   //avg calculate through sum of the middle line + middle line - 1 + middle line + 1;

                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed + copy_image [i][j+1].rgbtRed) + (copy_image[i-1][j].rgbtRed + copy_image[i-1][j-1].rgbtRed + copy_image [i-1][j+1].rgbtRed) + (copy_image[i + 1][j].rgbtRed + copy_image[i + 1][j-1].rgbtRed + copy_image [i + 1][j+1].rgbtRed))/9;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue + copy_image [i][j+1].rgbtBlue) + (copy_image[i-1][j].rgbtBlue + copy_image[i-1][j-1].rgbtBlue + copy_image [i-1][j+1].rgbtBlue) + (copy_image[i + 1][j].rgbtBlue + copy_image[i + 1][j-1].rgbtBlue + copy_image [i + 1][j+1].rgbtBlue))/9;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen + copy_image [i][j+1].rgbtGreen) + (copy_image[i-1][j].rgbtGreen + copy_image[i-1][j-1].rgbtGreen + copy_image [i-1][j+1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen + copy_image[i + 1][j-1].rgbtGreen + copy_image [i + 1][j+1].rgbtGreen))/9;

                // now the avg is calculated time for putting the value of the
                image[i][j].rgbtRed = avg_red;
                image[i][j].rgbtGreen = avg_green;
                image[i][j].rgbtBlue = avg_blue;
            }

            //top edge
            if(i == 0 && j != 0 && j != width-1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed + copy_image [i][j+1].rgbtRed) + (copy_image[i + 1][j].rgbtRed + copy_image[i + 1][j-1].rgbtRed + copy_image [i + 1][j+1].rgbtRed))/6;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue + copy_image [i][j+1].rgbtBlue) + (copy_image[i + 1][j].rgbtBlue + copy_image[i + 1][j-1].rgbtBlue + copy_image [i + 1][j+1].rgbtBlue))/6;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen + copy_image [i][j+1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen + copy_image[i + 1][j-1].rgbtGreen + copy_image [i + 1][j+1].rgbtGreen))/6;
                // now the avg is calculated time for putting the value of the
                image[i][j].rgbtRed = avg_red;
                image[i][j].rgbtGreen = avg_green;
                image[i][j].rgbtBlue = avg_blue;
            }

            //left side edge
            if(j == 0 && i != 0 && i != height-1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed +  copy_image [i][j+1].rgbtRed) + (copy_image[i-1][j].rgbtRed  + copy_image [i-1][j+1].rgbtRed) + (copy_image[i + 1][j].rgbtRed + copy_image [i + 1][j+1].rgbtRed))/6;
                int avg_blue = ((copy_image[i][j].rgbtBlue +  copy_image [i][j+1].rgbtBlue) + (copy_image[i-1][j].rgbtBlue +  copy_image [i-1][j+1].rgbtBlue) + (copy_image[i + 1][j].rgbtBlue +  copy_image [i + 1][j+1].rgbtBlue))/6;
                int avg_green = ((copy_image[i][j].rgbtGreen +  copy_image [i][j+1].rgbtGreen) + (copy_image[i-1][j].rgbtGreen +  copy_image [i-1][j+1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen +  copy_image [i + 1][j+1].rgbtGreen))/6;
                // now the avg is calculated time for putting the value of the
                image[i][j].rgbtRed = avg_red;
                image[i][j].rgbtGreen = avg_green;
                image[i][j].rgbtBlue = avg_blue;
            }

            //right side edge
            if(j == width-1 && i != 0 && i != height-1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed ) + (copy_image[i-1][j].rgbtRed + copy_image[i-1][j-1].rgbtRed ) + (copy_image[i + 1][j].rgbtRed + copy_image[i + 1][j-1].rgbtRed ))/6;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue ) + (copy_image[i-1][j].rgbtBlue + copy_image[i-1][j-1].rgbtBlue) + (copy_image[i + 1][j].rgbtBlue + copy_image[i + 1][j-1].rgbtBlue ))/6;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen ) + (copy_image[i-1][j].rgbtGreen + copy_image[i-1][j-1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen + copy_image[i + 1][j-1].rgbtGreen))/6;
                // now the avg is calculated time for putting the value of the
                image[i][j].rgbtRed = avg_red;
                image[i][j].rgbtGreen = avg_green;
                image[i][j].rgbtBlue = avg_blue;
            }


            //bottom edge
            if(i == height - 1 && j != 0 && j != width-1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed + copy_image [i][j+1].rgbtRed) + (copy_image[i-1][j].rgbtRed + copy_image[i-1][j-1].rgbtRed + copy_image [i-1][j+1].rgbtRed))/6;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue + copy_image [i][j+1].rgbtBlue) + (copy_image[i-1][j].rgbtBlue + copy_image[i-1][j-1].rgbtBlue + copy_image [i-1][j+1].rgbtBlue))/6;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen + copy_image [i][j+1].rgbtGreen) + (copy_image[i-1][j].rgbtGreen + copy_image[i-1][j-1].rgbtGreen + copy_image [i-1][j+1].rgbtGreen))/6;
                // now the avg is calculated time for putting the value of the
                image[i][j].rgbtRed = avg_red;
                image[i][j].rgbtGreen = avg_green;
                image[i][j].rgbtBlue = avg_blue;
            }

            //now for corners
            //top left
            if(i == 0 && j == 0)
            {
                int avg_red = ((copy_image[i][j].rgbtRed  + copy_image [i][j+1].rgbtRed) +  (copy_image[i + 1][j].rgbtRed + copy_image [i + 1][j+1].rgbtRed))/4;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image [i][j+1].rgbtBlue)  + (copy_image[i + 1][j].rgbtBlue + copy_image [i + 1][j+1].rgbtBlue))/4;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image [i][j+1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen + copy_image [i + 1][j+1].rgbtGreen))/4;
            }
            //top right
            if(i == 0 && j == width - 1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed ) + (copy_image[i + 1][j].rgbtRed + copy_image[i + 1][j-1].rgbtRed))/4;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue) + (copy_image[i + 1][j].rgbtBlue + copy_image[i + 1][j-1].rgbtBlue))/4;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen) + (copy_image[i + 1][j].rgbtGreen + copy_image[i + 1][j-1].rgbtGreen))/4;
            }
            //bottom right
            if(i == height - 1 && j == 0)
            {
                int avg_red = ((copy_image[i][j].rgbtRed + copy_image[i][j-1].rgbtRed) + (copy_image[i-1][j].rgbtRed + copy_image[i-1][j-1].rgbtRed) )/4 ;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image[i][j-1].rgbtBlue ) + (copy_image[i-1][j].rgbtBlue + copy_image[i-1][j-1].rgbtBlue))/4 ;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image[i][j-1].rgbtGreen) + (copy_image[i-1][j].rgbtGreen + copy_image[i-1][j-1].rgbtGreen ))/4 ;

            }
            //bottom left
            if(i == height - 1 && j == width - 1)
            {
                int avg_red = ((copy_image[i][j].rgbtRed+ copy_image [i][j+1].rgbtRed) + (copy_image[i-1][j].rgbtRed  + copy_image [i-1][j+1].rgbtRed))/4;
                int avg_blue = ((copy_image[i][j].rgbtBlue + copy_image [i][j+1].rgbtBlue) + (copy_image[i-1][j].rgbtBlue + copy_image[i-1][j-1].rgbtBlue + copy_image [i-1][j+1].rgbtBlue))/4;
                int avg_green = ((copy_image[i][j].rgbtGreen + copy_image [i][j+1].rgbtGreen) + (copy_image[i-1][j].rgbtGreen + copy_image [i-1][j+1].rgbtGreen))/4;

            }


        }
    }
    return;
}

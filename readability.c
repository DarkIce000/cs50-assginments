#include <math.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int words(string sentences);
int letters(string sentences);
int nsentence(string sentences);


int main(void)
{
//getting input from the user
    string sentences = get_string("enter the sentences: ");
    //printf(" letters: %i words: %i sentences: %i \n", letters(sentences), words(sentences), nsentence(sentences));

//calculate the letters per 100 words and sentences per 100 word;
    float avg_letter = ((float) letters(sentences)/(float) words(sentences))*100;
    //printf("letters_avg: %f", avg_letter);


    float avg_sntcs = ((float) nsentence(sentences)/(float) words(sentences))*100.00000;
    //printf("avg_sntcs: %f", avg_sntcs);

//putting the value of the avg_letter and avg_sntcs; in the grade formula;
    float index = 0.0588 * avg_letter - 0.296 * avg_sntcs - 15.8;
    //printf("index: %f \n", index);



    int grade =((int) round (index));
    //printing the grade level;
    if(grade <= 1 )
    {
        printf("Before Grade 1 \n");
    }
    else if(grade >= 16)
    {
        printf("Grade 16+ \n");
    }
    else if(grade > 1 && grade < 16)
    {
        printf("Grade %i \n", grade);
    }
    else
    {
        return 10;
    }

}

 //checking for how many letter the user has typed
int letters (string sentences)
{
    int  m = 0;
    for(int i = 0; i < strlen(sentences); i++)
    {
        if((sentences[i]>= 'a' && sentences[i]<= 'z') || (sentences[i] >= 'A' && sentences[i] <= 'Z'))
        {
            m++;
        }
    }
    return m;
}
// no. of words
int words(string sentences)
{
    int m = 0;
    for (int i = 0; i < strlen(sentences); i++)
    {
        if(sentences[i] == ' ')
        {
         m++;
        }
    }
    return m+1;
}
// no. of sentences
int nsentence(string sentences)
{
    int m = 0;
    for (int i = 0; i < strlen(sentences); i++)
    {
        if(sentences[i] =='!' || sentences[i] == '.')
        {
            m++;
        }
    }
    return m;
}
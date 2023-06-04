#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

   // TODO: Print the winner
   if (score1 > score2)
   {
    printf("Player 1 wins! \n");
   }
   else if (score2> score1)
   {
    printf("Player 2 wins! \n");
   }
   else
   {
    printf("Tie\n");
   }
}


//computing score function
int compute_score(string word)
{
    //loop for iterating through the letters of the word;
    int sum = 0;
    for(int i = 0; i <strlen(word); i++)
    {

            //checking the charachter, if matched, find the position and then by position put the points array;

            int m;
            for ( int j = 0 ; j < 26 ; j++)
            {
                string albt ="abcdefghijklmnopqrstuvwxyz";
                string Calbt ="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                if(word[i] == albt[j] || word[i] == Calbt[j])
                {
                    m = POINTS[j];
                    //summing only when we get letters
                    sum += m;
                }
            }
    }
    return sum;
}


#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;
// greatest finding function
int greatest(void);

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    // canditate storing loop
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }
    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // check for the name of the candidate if matches then update the vote count total of the canditate
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes += 1;
            return true;
        }
    }
    // if the name does not match any of the name of the canditate the return false
    return false;
}
// Print the winner (or winners) of the election
void print_winner(void)
{
    // find all the elements in the array that has that greatest value;
    // print those;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == greatest())
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}

// greatest number finding function
int greatest(void)
{
    // find the greatest value in the array
    int greatest_value = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > greatest_value)
        {
            greatest_value = candidates[i].votes;
        }
    }
    return greatest_value;
}
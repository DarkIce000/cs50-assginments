import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("usage error")
        sys.exit(0)

    # TODO: Read database file into a variable
    database =[]
    strnames = []
    with open(sys.argv[1], 'r') as datafile:
        reader = csv.DictReader(datafile)
        strnames = reader.fieldnames
        for name in reader:
            database.append(name)
    print(database)
    print(strnames[1:])


    # TODO: Read DNA sequence file into a variable
    sequences= []
    with open(sys.argv[2], 'r') as txtfile:
         sequences.append(txtfile.readline())
    print(sequences)


    # TODO: Find longest match of each STR in DNA sequence
    counter = []
    headers= strnames[1:]
    for names in headers:
        count = longest_match(sequences[0], names)
        print(names)
        counter.append(count)
    print(counter)


    # TODO: Check database for matching profiles
    #database
    #headers
    #counter

    for db in database:
        for i in range(len(headers)):
                if int(db[headers[i]]) == int(counter[i]):
                    if i < (len(headers)-1):
                        continue
                    elif i == (len(headers)-1):
                        return print(db["name"])

                else:
                    break




    return print("No Match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

def checker(db, headers):
    for i in range(len(headers)):
        if db[headers[i]] == counter[i]:
            continue

main()

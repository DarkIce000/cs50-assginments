def main():
    #get user input
    sentences = input("provide: ")
    #calculate avg of the letters words and sentences
    avg_letters = (NumberOfLetters(sentences) / NumberOfWords(sentences)) * 100
    avg_sentences = (NumberOfSentences(sentences)/NumberOfWords(sentences)) * 100
    #calculate the grade using formula
    index = 0.0588 * avg_letters - 0.296 * avg_sentences - 15.8
    grade = round(index)
    #print the grade
    if grade <= 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", grade)

#functions for finding number of letters
def NumberOfLetters(sentences):
    count = 0
    for i in range (len(sentences)):
        if sentences[i] >= 'a' and sentences[i] <= 'z' or sentences[i] >= 'A' and sentences[i] <= 'Z':
            count += 1
    return count

def NumberOfWords(sentences):
    count = 1
    for i in range(len(sentences)):
        if sentences[i] == ' ':
            count += 1
    return count

def NumberOfSentences(sentences):
    count = 0
    for i in range (len(sentences)):
        if sentences[i] == '.' or sentences[i] == '?' or sentences[i] == '!':
            count += 1
    return count

#calling main function
main()
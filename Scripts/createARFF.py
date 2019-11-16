import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn


# nltk.download('stopwords')


def main():
    try:
        print('Experimento: ')
        experimento = input()
        source = open('../Datasets/5500ingles.txt', 'r', encoding="ISO-8859-1")
        csv = open('../Datasets/5500ingles_' + experimento + '_NoWeka.arff', 'w+', encoding="ISO-8859-1")
        custom_stopwords = open('../Stopwords/stopwords_without_questions.txt', 'r', encoding="ISO-8859-1").readlines()
        csv.write("@relation answer" + experimento + "\n")
        csv.write("@attribute AnswerType STRING\n")
        # csv.write("@attribute Question STRING\n")
        csv.write("@attribute FirstWord STRING\n")
        csv.write("@attribute SecondWord STRING\n")
        csv.write("@attribute ThirdWord STRING\n")
        csv.write("@attribute FourthWord STRING\n")
        csv.write("@attribute FirstAndSecond STRING\n")
        csv.write("@attribute SecondAndThird STRING\n")
        csv.write("@attribute FirstAndThird STRING\n")
        csv.write("@attribute FirstAndFourth STRING\n")
        csv.write("@attribute SecondAndFourth STRING\n")
        csv.write("@attribute ThirdAndFourth STRING\n")

        csv.write("@data\n")
        lines = source.readlines()
        tag_map = nltk.defaultdict(lambda: wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV
        # tag_map['WP'] = wn.NOUN
        num_questions = 0
        for line in lines:
            csv_line = line.split(" ", 1)
            type = csv_line[0].split(":")
            print(type)
            if (type[0] == "HUM" and type[1] == "ind") or type[0] == "NUM" or type[0] == "LOC":
                num_questions += 1
                lowered_question = csv_line[1][:-1].lower()
                tokens_question = word_tokenize(lowered_question)
                final_question = []
                for word, tag in pos_tag(tokens_question):
                    word_Lemmatized = WordNetLemmatizer()
                    if word not in custom_stopwords and word.isalpha():
                        word = word_Lemmatized.lemmatize(word, tag_map[tag[0]])
                        final_question.append(word)
                # csv.write('"' + csv_line[0] + '"' + ' , "' + ' '.join(final_question) + '" \n')
                if (len(final_question) > 3):
                    # 3 Palabras
                    # csv.write(
                    #     '"' + csv_line[0] + '"' + ' , "' + final_question[0] + '" , "' + final_question[1] + '" , "' +
                    #     final_question[2] + '" \n')

                    # 4 Palabras
                    # csv.write(
                    #     '"' + csv_line[0] + '"' + ' , "' + final_question[0] + '" , "' + final_question[1] + '" , "' +
                    #     final_question[2] + '" , "' + final_question[3] + '" \n')

                    # 3 Palabras + Digrama
                    # csv.write(
                    #     '"' + csv_line[0] + '"' + ' , "' + final_question[0] + '" , "' + final_question[1] + '" , "' +
                    #     final_question[
                    #         2] + '" , "' + final_question[0] + ' ' + final_question[1] + '" , "' + final_question[
                    #         1] + ' ' +
                    #     final_question[2] + '" , "' + final_question[0] + ' ' + final_question[2] + '" \n')

                    #4 Palabras + Digrama
                    csv.write(
                        '"' + csv_line[0] + '"' + ' , "' + final_question[0] + '" , "' + final_question[1] + '" , "' + final_question[2] + '" , "' + final_question[3] +
                        '" , "' + final_question[0] + ' ' + final_question[1] + '" , "' + final_question[1] + ' ' + final_question[2] + '" , "' +
                        final_question[0] + ' ' + final_question[2] + '" , "' + final_question[0] + ' ' + final_question[3] + '" , "' + final_question[1] + ' ' + final_question[3] +
                        '" , "' + final_question[2] + ' ' + final_question[3] + '" \n')
        print(num_questions)
    except Exception as e:
        print(e)
    finally:
        source.close()
        csv.close()


if __name__ == '__main__':
    main()

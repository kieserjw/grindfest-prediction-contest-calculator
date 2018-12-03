#! /usr/bin/python

# Calculates the scores of the Grindfest prediction contest
# Guessing last place correctly gets you 1, guessing second to last gets you 2 points, etc.
# A maximum score is just a sum of all the places    
def calculate_score(prediction, answer_key, num_runners_to_score = None):
    if len(prediction) != len(answer_key):
        return -1
    if num_runners_to_score == None:
        num_runners_to_score = len(prediction)
        
    # reverse the lists as the scores decrease with each index
    prediction = prediction[::-1]
    answer_key = answer_key[::-1]
    
    score = 0
    
    # we need to change the value of the max sub_score if not scoring each place
    diff = len(prediction) - num_runners_to_score 
    
    for i in range(len(prediction)):
        # subtract the distance between the predicted and real index from the max sub_score
        # i + 1 because of zero indexing
        sub_score = i + 1 - diff - abs(i - prediction.index(answer_key[i])) 
        if sub_score > 0:
            score += sub_score
    return score
    
    

def main():
    # TODO: change hard-coded values to parameters
    f = open("results.csv","r")
    predictions = []
    num_women_in_results = 3
    num_women_to_score = 3
    num_men_to_score = 4
    name_col = 17
    data_string_identifier = "2018"
    answer_key_str = "answer_key"
    mens_answer_key = []
    womens_answer_key = []
    scores = []
    
    # read the file and get the data into memory
    for line in f:
        line = line[:-2] # remove the carriage and line returns from the end of the string
        data = line.split(",")
        if data[name_col] == answer_key_str:
            # we have the answer key. store it separately
            answer_key = data[name_col:]
            womens_answer_key = answer_key[1:num_women_in_results+1]
            mens_answer_key = answer_key[num_women_in_results+1:]
        elif data_string_identifier in data[0] and data[name_col] is not "":
            # we have data from a respondent who inputted a name. add them to the list
            predictions.append(data[name_col:])
            print(data[name_col:])

    # calculate the scores
    for prediction in predictions:
        womens = prediction[1:num_women_in_results+1]
        mens = prediction[num_women_in_results+1:]
        womens_score = calculate_score(womens, womens_answer_key, num_women_to_score)
        mens_score = calculate_score(mens, mens_answer_key, num_men_to_score)
        scores.append([prediction[0], womens_score, mens_score])

    # add in a perfect score to make sure the algorithm's working. these should all be N*(N+1)/2
    scores.append([answer_key_str, calculate_score(womens_answer_key,womens_answer_key, num_women_to_score), calculate_score(mens_answer_key, mens_answer_key, num_men_to_score)])
    
    print(womens_answer_key)
    print(mens_answer_key)
    print(scores)
    sorted_womens = sorted(scores, key=lambda x: -1* x[1])
    sorted_mens = sorted(scores, key=lambda x: -1* x[2])
    print("\nWomen's Results")
    for name_score in sorted_womens:
        print(name_score[0:2])
    print("\nMen's Results")
    for name_score in sorted_mens:
        print(name_score[0:3:2])
    
main()
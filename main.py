def getJudgeData():
    print('Input the judges score')
    judge_score = float(input())
    if judge_score is int or float:
        if 1 <= judge_score <= 10:
            return judge_score
        else:
            print('Enter a value between 1 and 10')
    else:
        print('Enter an integer or float between 1 and 10')


def main():
    global score1
    global score2
    global score3
    global score4
    global score5
    count = 0
    for i in range(5):
        count += 1
        judge_score = getJudgeData()
        if count == 1:
            score1 = judge_score
        if count == 2:
            score2 = judge_score
        if count == 3:
            score3 = judge_score
        if count == 4:
            score4 = judge_score
        if count == 5:
            score5 = judge_score

    def findLowest(score1, score2, score3, score4, score5):
        if score1 <= score2 and score1 <= score3 and score1 <= score4 and score1 <= score5:
            return score1
        elif score2 <= score1 and score2 <= score3 and score2 <= score4 and score2 <= score5:
            return score2
        elif score3 <= score1 and score3 <= score2 and score3 <= score4 and score3 <= score5:
            return score3
        elif score4 <= score1 and score4 <= score2 and score4 <= score3 and score4 <= score5:
            return score4
        elif score5 <= score1 and score5 <= score2 and score5 <= score3 and score5 <= score4:
            return score5

        """
        
        score_list = [score1, score2, score3, score4, score5]
        sorted_score_list = score_list.scort()
        lowest_score = sorted_score_list[0]
        return lowest_score
        
        """


    def findHighest(score1, score2, score3, score4, score5):
        if score1 >= score2 and score1 >= score3 and score1 >= score4 and score1 >= score5:
            return score1
        elif score2 >= score1 and score2 >= score3 and score2 >= score4 and score2 >= score5:
            return score2
        elif score3 >= score1 and score3 >= score2 and score3 >= score4 and score3 >= score5:
            return score3
        elif score4 >= score1 and score4 >= score2 and score4 >= score3 and score4 >= score5:
            return score4
        elif score5 >= score1 and score5 >= score2 and score5 >= score3 and score5 >= score4:
            return score5

        """
        score_list = [score1, score2, score3, score4, score5]
        sorted_score_list = score_list.sort()
        highest_score = sorted_score_list[0]
        return highest_score
        """

    def calcScore(score1, score2, score3, score4, score5):
        score_list = [score1, score2, score3, score4, score5]

        score_list1 = [i for i in score_list if i != (findHighest(score1, score2, score3, score4, score5))]
        score_list2 = [l for l in score_list1 if l != (findLowest(score1, score2, score3, score4, score5))]
        average_score = sum(score_list2) / len(score_list2)

        print('The average score is: ' + str(average_score))

    calcScore(score1, score2, score3, score4, score5)


if __name__ == '__main__':
    main()

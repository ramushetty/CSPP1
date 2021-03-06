'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands

'''
def main_function(hand):
    '''
    return length of a hand
    '''
    string = '--23456789TJQKA'
    rank_list = [num for num in string]
    #print(rank_list)
    set1 = set()
    for num, _ in hand:
        set1.add(rank_list.index(num))
    return set1
def is_onepair(hand):
    '''
    return one pair
    '''
    string = '--23456789TJQKA'
    rank_list = [num for num in string]
    #print(rank_list)
    set1 = set()
    list1 = []
    for num, _ in hand:
        list1.append(rank_list.index(num))
        set1.add(rank_list.index(num))
    if len(set1) == 4:
        #print(l)
        for index in set1:
            if list1.count(index) == 2:
                return index/10
    return 100
def is_twopair(hand):
    '''
    return true or false
    '''
    sett = main_function(hand)
    if len(sett) == 3:
        return True
    return False
def three_four(hand):
    '''Function call for Three/four kind, full house'''
    length = len(hand)
    listt = []
    for index in range(length):
        if hand[index][0] == 'T':
            listt.append(10)
        elif hand[index][0] == 'J':
            listt.append(11)
        elif hand[index][0] == 'Q':
            listt.append(12)
        elif hand[index][0] == 'K':
            listt.append(13)
        elif hand[index][0] == 'A':
            listt.append(14)
        else:
            listt.append(int(hand[index][0]))
    listt.sort()
    #yaarcopy = yaar.copy()
    counter = []
    jindex = 0
    set1 = set(listt)
    for jindex in set1:
        counter.append(listt.count(jindex))
    return counter

def is_three_kind(hand):
    '''Function for three kind'''
    count = three_four(hand)
    count = max(count)
    if count == 3:
        return True
    return False
def is_four_kind(hand):
    '''
    return true or false
    '''
    counter = three_four(hand)
    counter = max(counter)
    if counter == 4:
        return True
    return False


def is_fullhouse(hand):
    '''Function for FullHouse'''
    count = three_four(hand)
    if 3 in count:
        if 2 in count:
            return True
    return False



def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    #print(len(hand))
    #print(hand[1])
    length = len(hand)
    listt = []
    for index in range(length):
        if hand[index][0] == 'T':
            listt.append(10)
        elif hand[index][0] == 'J':
            listt.append(11)
        elif hand[index][0] == 'Q':
            listt.append(12)
        elif hand[index][0] == 'K':
            listt.append(13)
        elif hand[index][0] == 'A':
            listt.append(14)
        else:
            listt.append(int(hand[index][0]))
    count = 0
    listt.sort()
    for index in range(len(hand)-1):
        if listt[index] == listt[index+1]-1:
            count += 1
    if count == len(hand)-1:
        return True
    return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    #print(hand)
    listt1 = []
    for _, suite in hand:
        listt1.append(suite)
    set1 = set(listt1)
    return len(set1) == 1
def high_card(hand):
    ''' It returns the value of High Hand'''
    set1 = main_function(hand)
    if len(set1) == 5 and not is_flush(hand):
        return max(set1)/100
    return False



def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    #print(hand)
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_four_kind(hand):
        return 7
    if is_fullhouse(hand):
        return 6
    if is_flush(hand):
        return 5
    if is_straight(hand):
        return 4
    if is_three_kind(hand):
        return 3
    if is_twopair(hand):
        return 2
    if is_onepair(hand) != 100:
        return is_onepair(hand)
    return high_card(hand)
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand

    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    #print(hands)
    #print(len(hands))
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    #print(HANDS)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))

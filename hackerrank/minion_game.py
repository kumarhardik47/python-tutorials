def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    slen = len(string)
    for i in range(slen):
        if string[i] in ('a','e','i','o','u','A','E','I','O','U'):
            kevin_score+=(slen -i)
        else:
            stuart_score+=(slen-i)
    if kevin_score > stuart_score:
        print "Kevin ", kevin_score
    if kevin_score < stuart_score:
        print "Stuart ", stuart_score
    if kevin_score == stuart_score:
        print "Draw"


if  __name__ == '__main__':
    s = raw_input()
    minion_game(s)

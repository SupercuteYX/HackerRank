def climbingLeaderboard(ranked, player):
    #set()生成去掉duplicate之后的集合{}，list（）把集合{}转为list，sorted（）排序
    rank = sorted(list(set(ranked)), reverse=True)
    r = []
            
    for i in player:
        # rank不为空，并且i>=rank list最后一个值
        while rank and i >= rank[-1]: 
            rank.pop()
        # 注意！不在while循环内
        r.append(len(rank)+1) 
        
    return r

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

# Method 1: 
if __name__ == '__main__':
    #Get input and data
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    
    #Find second lowest
    lowest = min(scores)
    second_lowest = 101
    for score in scores:
        if (second_lowest > score) and (score != lowest):
            second_lowest = score
            
    #Find name with second lowest
    res = []
    for record in records:
        if record[1] == second_lowest:
            res.append(record[0])
    
    #Print name in alphabetical order
    res.sort()
    for name in res:
        print(name)
        

    

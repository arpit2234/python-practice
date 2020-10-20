def matchingword(sentance1,sentance2):
    words1=sentance1.split(" ")
    words2=sentance2.split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching{word1} with {word2}")
            if word1.lower()==word2.lower():
                score+=1

    return score
            

       

if __name__=="__main__":
    sentences=["python is a good","this is snake","harry is a good boy","Subscribe to code with harry"]
    query=input("Please Enter the query string\n")
    scores=[matchingword(query,sentance) for sentance in sentences]
    # print(scores)
    sortedsentscore=[ sentscore for sentscore in sorted(zip(scores,sentences),reverse=True)]
    # print(sortedsentscore)
    print(f"{len(sortedsentscore)} resulrs found!")
    for score,item in sortedsentscore:
        print(f" \"{item}\" with a score of {score}")
#function that returns the highscore
def game():
    highscore=100
    return highscore
#calling the function and getting high score
updatehighscore=game()
#need to get the previous high score so opening file in read mode and getting data
fo=open("HighScore.txt","r")
data=fo.read()
#conversion of data to int and checking if current score is highest score or not
if(int(data) < updatehighscore):
    highscore=str(updatehighscore)
    print(highscore)
    #opening the file in write mode and writing the highest score
    fo=open("HighScore.txt","w")
    fo.write(highscore)
#reading the file after updating
fo=open("HighScore.txt","r")
print(fo.read())
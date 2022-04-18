dict={}#empty dictionary
n=int(input())#how many values u r going to enter in dict
for i in range(n):
    key=input("Enter key")#enter key
    value=input("Enter value")#enter value
    d={key:value}
    dict.update(d)#appending values to dictionary
teluguword=input("Enter any Telugu word and see english translation")#user input
print(dict[teluguword])#prints the value associated with the key 
#if your searching for the word which is not present in dict it will give u error
#print(dict.get[]) it dosent give u error
with open("Poems.txt","w") as fo:
    fo.write('''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky''')

fo=open("poems.txt","r")
data=fo.read()
if('twinkle' in data):
    print("yes it exists")
file = open('story.txt','r')


lines = file.readlines()
numberOfLines = len(lines)

print("The number of lines in this file is: %d" %(numberOfLines))


file.close()

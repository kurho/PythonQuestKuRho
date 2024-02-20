file = open('story.txt','r')


lines = file.readlines()
numberOfLines = len(lines)

print("This file has %d lines" %(numberOfLines))


file.close()

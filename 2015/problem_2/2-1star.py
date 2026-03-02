#Order of dimensions given for presents is l * w * h
#Formula for a right rectangular prism is 2*l*w + 2*w*h + 2*h*l

f = open("input.md", "r", encoding="utf-8")
presents = []
paper = 0
with f as file:
    for line in file:
        dimensions = line.rstrip().split('x')
        side1 = int(dimensions[0]) * int(dimensions[1])
        side2 = int(dimensions[1]) * int(dimensions[2])
        side3 = int(dimensions[0]) * int(dimensions[2])
        paper += 2 * (side1 + side2 + side3) + min(side1,side2,side3)
print(paper)


'''
#Doing this method was giving me errors because it wasn't correctly detecting the end of the file. I'm not sure what character it was tbh.
while presents is not EOFError and presents != "\n":

    dimensions = presents
    dimensions = dimensions.split("x")
    dimensions[2] = dimensions[2].strip("\n")
    side1 = int(dimensions[0]) * int(dimensions[1])
    side2 = int(dimensions[1]) * int(dimensions[2])
    side3 = int(dimensions[0]) * int(dimensions[2])
    paper += 2 * (side1 + side2 + side3) + 2 * min(side1,side2,side3)
    presents  = f.readline()
    print("the next line's ascii codes are:")
    for x in presents:
        print(ord(x))

print(paper)
'''

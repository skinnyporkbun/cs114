PaintGallonCoverage = 400

print ("what is the width of the wall in feet?")
width = int(input())

print ("what is the height of the wall in feet?")
height = int(input())

print ("how much does the paint cost per gallon?")
cost = float(input())

print ("how many coats will you do?")
coats = int(input())

wallcost = round((width*height)/PaintGallonCoverage) * cost * coats

print("it will cost " + str(round(wallcost, 2)) + " dollars to paint the wall")

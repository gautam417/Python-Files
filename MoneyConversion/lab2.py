#Gautam Mehta
#Lab 2

d= float(input("How many dimes do you have?: "))
q= float(input("How many quarters do you have?: "))
total = (d *.10 )+ (q *.25 )
x= int(total)
y= str(total)

print ("You have", x, "dollars and", y[2:], "cents.")

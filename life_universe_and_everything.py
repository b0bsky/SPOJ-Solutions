# rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

running = True

while(running):
    user_in = int(input())

    if user_in == 42:
        running = False
    else:
        print(user_in)
done = False
inc = 0.5
val = 0
while not done:
    while val <0.9999:
        val += inc
        inc *= 0.5
        print(val)
    done = True

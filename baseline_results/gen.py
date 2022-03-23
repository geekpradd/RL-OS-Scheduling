import random 

ns = [5,10,20]

for n in ns:
    duration_range = range(1, 11)
    time_range = range(1, 20)

    s = "\n-l "
    for i in range(n):
        duration = random.choice(duration_range)
        time = random.choice(time_range)
        s += "{0}:{1},".format(duration, time)

    s = s[:-1]

    with open("instance_input", "a") as f:
        f.write(s)
        print (s)
    
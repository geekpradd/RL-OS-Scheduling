import random 

NUM = 60
ns = [5,10,20]

for i in range(NUM):
    duration_range = range(1, 80)
    time_range = range(1, 60)

    n = random.choice(range(10,30))
    s = "\n-l "
    for i in range(n):
        duration = random.choice(duration_range)
        time = random.choice(time_range)
        s += "{0}:{1},".format(duration, time)

    s = s[:-1]

    with open("new_instance_input", "w") as f:
        f.write(s)
        print (s)
    
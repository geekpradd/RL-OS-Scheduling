from matplotlib import pyplot as plt

instances = dict()
settings = dict()
turnaround_time = dict()
waiting_time = dict()
response_time = dict()
throughput = dict()

with open("output", "r") as f:
    instance = ""
    setting = ""
    for line in f:
        line = line.rstrip().lstrip()
        if line.startswith("INSTANCE"):
            instance = line[12:]
            if instance not in instances:
                instances[instance] = len(instances)
                turnaround_time[instance] = dict()
                waiting_time[instance] = dict()
                response_time[instance] = dict()
                throughput[instance] = dict()
        
        if line.startswith("SETTING"):
            setting = line[11:]
            if setting not in settings:
                settings[setting] = len(settings)

        if line.startswith("average turnaround_time"):
            turnaround_time[instance][setting] = float(line[25:])

        if line.startswith("average waiting_time"):
            waiting_time[instance][setting] = float(line[22:])

        if line.startswith("average response_time"):
            response_time[instance][setting] = float(line[23:])
        
        if line.startswith("throughput"):
            throughput[instance][setting] = float(line[12:])

for instance in instances:
    data = turnaround_time[instance]
    algos = list(data.keys())
    algos = list(map(lambda x: settings[x], algos))
    times = list(data.values())
    plt.bar(algos, times, color ='blue', width = 0.4)
    
    plt.xlabel("Algorithms")
    plt.ylabel("Average Turnaround Time")
    plt.title("Instance:" + str(instances[instance]))
    plt.savefig("plots/Turnaround_time_instance" + str(instances[instance]) + ".png")
    plt.figure()

    data = waiting_time[instance]
    algos = list(data.keys())
    algos = list(map(lambda x: settings[x], algos))
    times = list(data.values())
    plt.bar(algos, times, color ='blue', width = 0.4)
    
    plt.xlabel("Algorithms")
    plt.ylabel("Average Waiting Time")
    plt.title("Instance:" + str(instances[instance]))
    plt.savefig("plots/Waiting_time_instance" + str(instances[instance]) + ".png")
    plt.figure()

    data = response_time[instance]
    algos = list(data.keys())
    algos = list(map(lambda x: settings[x], algos))
    times = list(data.values())
    plt.bar(algos, times, color ='blue', width = 0.4)
    
    plt.xlabel("Algorithms")
    plt.ylabel("Average Response Time")
    plt.title("Instance:" + str(instances[instance]))
    plt.savefig("plots/Response_time_instance" + str(instances[instance]) + ".png")
    plt.figure()

    data = throughput[instance]
    algos = list(data.keys())
    algos = list(map(lambda x: settings[x], algos))
    times = list(data.values())
    plt.bar(algos, times, color ='blue', width = 0.4)
    
    plt.xlabel("Algorithms")
    plt.ylabel("Throughput")
    plt.title("Instance:" + str(instances[instance]))
    plt.savefig("plots/Throughput_instance" + str(instances[instance]) + ".png")
    plt.figure()

print(settings)

instances = list(instances.keys())
print(instances[10])
print(instances[11])
print(instances[12])
print(instances[13])
print(instances[14])
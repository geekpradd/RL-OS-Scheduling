with open("output_baseline", "r") as f:
    with open("output", "w") as g:
        for line in f:
            line = line.lstrip()
            if line.startswith("INSTANCE") or line.startswith("SETTING") or line.startswith("average turnaround_time") or line.startswith("average waiting_time") or line.startswith("average response_time"):
                print(line)
                g.write(line+"\n")
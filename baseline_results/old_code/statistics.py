class Statistics:
    def __init__(self):
        self.turnaround = 0
        self.response_time = -1
        self.wait = 0

    def calculate_wait(self, final, arrival, burst):
        self.wait = final - arrival - burst + 1

    def calculate_turnaround(self, final, arrival):
        self.turnaround = final - arrival + 1


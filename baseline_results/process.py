from statistics import Statistics


class Process:
    job_id_counter = 0

    def __init__(self, burst_time, arrival_time):
        self.arrival = arrival_time
        self.burst_time = burst_time
        self.time_left = burst_time
        self.statistics = Statistics()
        self.finish_time = -1
        self.current_run = 0
        self.process_id = Process.job_id_counter
        Process.job_id_counter += 1

    def is_finished(self):
        return True if self.finish_time != -1 else False

    def finish(self, time):
        assert (self.time_left == 0)
        self.current_run = 0
        self.finish_time = time
        self.statistics.calculate_turnaround(self.finish_time, self.arrival)
        self.statistics.calculate_wait(self.finish_time, self.arrival, self.burst_time)

    def run(self, current_time):
        self.time_left -= 1

        if self.time_left == 0:
            self.finish(current_time)

        if self.statistics.response_time == -1:
            self.statistics.response_time = current_time - self.arrival

        self.current_run += 1
        return self.process_id

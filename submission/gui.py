import PySimpleGUI as sg

class Gui:
    def __init__(self, size_x, size_y):
        self.x1 = 100
        self.x2_off = 7
        self.y1 = 10
        self.y2_off = 15
        self.COLORS = ["purple", "lightblue", "red", "green", "blue", "brown", "grey", "pink", "black", "yellow"]
        self.graph = sg.Graph(canvas_size=(size_x, size_y), graph_bottom_left=(0, size_y), graph_top_right=(size_x, 0),
                              key='graph')
        self.layout = [[self.graph],
                  [sg.Button('Exit')]]
        self.window = sg.Window('MultiLevelFeedbackQueue', self.layout, finalize=True)
        

    def draw_process_rect(self, queue_num, queue_ticks, process_id):
        global x1_d
        color = self.COLORS[process_id % len(self.COLORS)]
        y1_d = self.y1 + 25 * queue_num
        x1_d = self.x1 + queue_ticks * self.x2_off
        self.graph.draw_rectangle((x1_d, y1_d), (x1_d + self.x2_off, y1_d + self.y2_off), fill_color=color,
                                  line_color=color)

    def draw_rr_queue_header(self, queue_id, quantum):
        return self.graph.draw_text(f'Queue {queue_id} RR : {quantum}',
                                    (5, 10 + 25 * queue_id), text_location=sg.TEXT_LOCATION_TOP_LEFT)

    def draw_fcfs_queue_header(self, queue_id):
        return self.graph.draw_text(f'Queue {queue_id} FCFS', (5, 10 + 25 * queue_id),
                                    text_location=sg.TEXT_LOCATION_TOP_LEFT)

    def print_process_statistics(self, i, job, number_of_queues):
        y1 = 10 + 25 * (number_of_queues + i)
        color = self.COLORS[job.process_id % len(self.COLORS)]
        self.graph.draw_rectangle((5, y1 + 3), (5 + 10, y1 + 13), fill_color=color, line_color=color)
        self.graph.draw_text(f"job arrival {job.arrival}, "
                             f"burst_time {job.burst_time}, "
                             f"turnaround_time: {job.statistics.turnaround}, "
                             f"wait: {job.statistics.wait}, "
                             f"response {job.statistics.response_time}",
                             (22, y1), text_location=sg.TEXT_LOCATION_TOP_LEFT)

    def print_global_statistics(self,
                                total_turnaround_time,
                                total_wait,
                                total_response,
                                total_jobs,
                                number_of_queues,
                                total_time,
                                boost):
        boost = boost if boost > 0 else "no boost"
        self.graph.draw_text(f"Global Statistics\n"
                             f"average turnaround_time: {total_turnaround_time / total_jobs}\n"
                             f"average waiting_time: {total_wait / total_jobs}\n"
                             f"average response_time: {total_response / total_jobs}\n"
                             f"throughput: {total_jobs / total_time * 1000}\n"
                             f"boost jobs each: {boost}",
                             (5, 10 + 25 * (number_of_queues + total_jobs)),
                             text_location=sg.TEXT_LOCATION_TOP_LEFT)
        self.graph.set_size((x1_d, 100 + 25 * (number_of_queues + total_jobs)))

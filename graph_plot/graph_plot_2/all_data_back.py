

class throughput():
    def __init__(self):
        # h5 ILP data  15s begin
        self.y1 = [
            9.24, 8.00, 8.00, 8.01, 8.00, 8.00, 8.00, 8.01, 8.00,
            8.00, 8.00, 8.01, 8.00, 8.00, 8.01, 8.00, 8.00, 8.00, 8.01,
            8.00, 8.00, 8.00, 8.01, 8.00, 8.00, 8.01, 8.00, 8.00, 8.00,
            8.04
        ]
        # h6 data  5s begin
        self.y2 = [
            4.47, 4.00, 4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00,
            4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00,
            4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.01, 3.99,
            4.02
        ]
        # h7 data  10s begin
        self.y3 = [
            5.60, 5.00, 5.00, 5.01, 5.00, 5.00, 4.85, 5.15, 5.00,
            5.01, 5.00, 5.00, 5.00, 5.00, 5.00, 5.01, 5.00, 5.00, 5.00,
            5.00, 5.00, 5.01, 5.00, 5.00, 5.00, 5.00, 5.00, 5.01, 5.00,
            5.02
        ]


class throughput2():
    def __init__(self):
        # h5 CWSP data  15s begin
        self.y1 = [
            7.37, 6.95, 6.81, 6.80, 6.81, 6.79, 6.81, 6.23, 6.24,
            6.22, 6.22, 6.26, 6.24, 6.23, 6.29, 6.22, 6.20, 6.24, 10.1,
            10.2, 10.2, 10.2, 8.61, 8.01, 8.00, 7.97, 8.02, 8.01, 8.00,
            8.00
        ]
        # h6 data  5s begin
        self.y2 = [
            4.46, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.00,
            4.00, 4.01, 4.00, 4.00, 3.13, 3.22, 3.40, 3.40, 3.41, 3.39,
            3.41, 3.94, 3.96, 3.99, 3.97, 3.95, 3.96, 3.97, 3.90, 3.97,
            4.00
        ]
        # h7 data  10s begin
        self.y3 = [
            5.57, 5.01, 5.00, 5.00, 5.00, 5.00, 5.00, 5.01, 5.00,
            5.00, 5.00, 5.00, 5.00, 5.01, 5.00, 5.00, 5.00, 5.00, 5.00,
            5.01, 5.00, 5.00, 5.00, 5.00, 5.00, 5.01, 5.00, 5.00, 5.00,
            5.02
        ]


class sender():
    def __init__(self):
        self.y1 = [
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00,
            8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00, 8.00

        ]
        # h6 data  5s begin
        self.y2 = [
            0.00, 4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00,
            4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00,
            4.00, 4.00, 4.00, 4.01, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00
        ]
        # h7 data  10s begin
        self.y3 = [
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 5.00, 5.00, 5.00, 5.00,
            5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00,
            5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00

        ]


sender_throughput = sender()
CWSP_throughput = throughput2()
ILP_throughput = throughput()

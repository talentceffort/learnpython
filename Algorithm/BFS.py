from collections import deque

# 지하철역 클래스
class Station:
    # 코드를 입력하세요.

    def __init__(self, name):
    # 인스턴스 변수들을 초기값으로 설정
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
    # self의 neighbors에 another_station을 담고,
    # another_station의 neighbors에 self를 담는다.
        self.neighbors = another_station
        another_station.neighbors.append(self)

# Breadth-First Search 알고리즘
#def bfs(start, goal):
    # 코드를 입력하세요.


# 파일 읽기
stations = {}
in_file = open('stations.txt')
# 파일의 데이터를 정리하여 각 역에 해당하는 Station 인스턴스를 만들고,
# add_connection 메소드로 이웃 역들을 연결시킨다.
#
# 후에 각 역을 쉽게 찾아서 쓸 수 있도록 stations 사전의
# key로 역 이름을 넣고, value로 해당 Station 인스턴스를 넣는다.
for read in in_file:
    previous_station = None
    data = read.strip().split("-")

    for name in data:
        station_name = name.strip();
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()


# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)

Cost = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Dobreta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Pitesti': 138, 'Dobreta': 120, 'Rimnicu Vilcea': 146},
        'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Eforie': {'Hirsova': 86},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Giurgiu': {'Bucharest': 90},
        'Neamt': {'Iasi': 87},
        'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90, 'Urziceni': 85},
        'Pitesti': {'Bucharest': 101, 'Rimnicu Vilcea': 97, 'Craiova': 138},
        }

Map = {'Arad': {'Zerind': 374, 'Sibiu': 253, 'Timisoara': 329},
       'Sibiu': {'Arad': 366, 'Oradea': 380, 'Rimnicu Vilcea': 193, 'Fagaras': 178},
       'Fagaras': {'Sibiu': 253, 'Bucharest': 0},
       'Zerind': {'Arad': 366, 'Oradea': 380},
       'Timisoara': {'Arad': 366, 'Lugoj': 244},
       'Lugoj': {'Timisoara': 329, 'Mehadia': 241},
       'Mehadia': {'Lugoj': 244, 'Dobreta': 242},
       'Dobreta': {'Mehadia': 241, 'Craiova': 160},
       'Craiova': {'Pitesti': 98, 'Dobreta': 242, 'Rimnicu Vilcea': 193},
       'Urziceni': {'Bucharest': 0, 'Vaslui': 199, 'Hirsova': 151},
       'Hirsova': {'Urziceni': 80, 'Eforie': 161},
       'Vaslui': {'Urziceni': 80, 'Iasi': 226},
       'Eforie': {'Hirsova': 151},
       'Iasi': {'Vaslui': 199, 'Neamt': 234},
       'Giurgiu': {'Bucharest': 0},
       'Neamt': {'Iasi': 226},
       'Bucharest': {'Pitesti': 98, 'Fagaras': 178, 'Giurgiu': 77, 'Urziceni': 80},
       'Pitesti': {'Bucharest': 0, 'Rimnicu Vilcea': 193, 'Craiova': 160},
       }



destination = 'Bucharest'
x = False
visited = []  # This list hold the visited node
Cost_sum = 0
print('\n --- Applying Greedy Best-First Search Algorithm on a graph ---\n ')
initial = input("Enter initial (Start) City: ")
Queue = [initial] # Add initial node to the queue
print('\n#',initial,'Added to the queue\n')


def Display():
    global Queue,destination,Cost_sum
    print('Destination <',destination,'> has been reached')
    print('\nQueue= ', Queue,'\n')
    for i in Queue:

        print(' -->',i,end='')


    print('\nTotal Cost =', int(Cost_sum))



def Greedy_Search():
    global Cost_sum, visited, destination, Queue, initial, x, Map, Cost,pathlength

while not x:
    for node in Map.keys():

        if node in Queue and node != destination and node not in visited:
            minimum = min(Map[node], key=Map[node].get)  # Choose the minimum node
            Queue.append(minimum)
            print('\n#',minimum,'Added to the queue[not the goal]\n')
            visited.append(node)

        elif destination in Queue:
            x = True
            break

for i in range(len(Queue)-1):
         Cost_sum = Cost_sum + Cost[Queue[i]][Queue[i + 1]]







Greedy_Search()
Display()


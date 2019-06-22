import xlrd
import math

class node:
    def __init__(self,x,y,z,r):
        self.x=x
        self.y=y
        self.z=z
        self.r=r
    def dist(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    def neighbor(self,other):
        dist=self.dist(other)
        if self==other:
            return False
        if dist<self.r+other.r:
            return True
        else:
            return False

def read_excel():
    workbook=xlrd.open_workbook('聚集体形态.xlsx')
    sheet1=workbook.sheet_by_index(0)
    data=[]
    for i in range(sheet1.nrows):
        data.append(node(sheet1.cell(i,0).value,sheet1.cell(i,1).value,sheet1.cell(i,2).value,sheet1.cell(i,3).value))
    return data

def max_dist(data):
    max_distance=-1
    max_index1=-1
    max_index2=-1
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            dist=data[i].dist(data[j])
            if dist>max_distance:
                max_distance=dist
                max_index1=i
                max_index2=j
    return max_distance,max_index1,max_index2

def build_graph(data):
    graph=[]
    for i in range(len(data)):
        row=[]
        for j in range(len(data)):
            if i==j:
                row.append(0)
                continue
            if data[i].neighbor(data[j]):
                row.append(1);
            else:
                row.append(float('inf'))
        graph.append(row)
    return graph

def dijkstra(graph,src,target):
    nodes=[i for i in range(len(data))]
    visited=[]
    visited.append(src)
    nodes.remove(src)
    dis={src:0}
    while nodes:
        min_nodes = 500
        min_index = -1
        for v in visited:
            for d in nodes:
                if graph[src][v]!=float('inf') and graph[v][d]!=float('inf'):
                    new_dist=graph[src][v]+graph[v][d]
                    if graph[src][d]>new_dist:
                        graph[src][d]=new_dist
                    if graph[src][d]<min_nodes:
                        min_nodes=graph[src][d]
                        min_index = d
        dis[min_index]=min_nodes
        visited.append(min_index)
        nodes.remove(min_index)
    return dis[target]

if __name__=='__main__':
    data=read_excel()
    max_distance,max_index1,max_index2=max_dist(data)
    graph=build_graph(data)
    min_nodes=dijkstra(graph,max_index1,max_index2)
    results={'AB距离':max_distance,'AB间点数':min_nodes}
    f=open('结果.txt','w+')
    f.write(str(results))
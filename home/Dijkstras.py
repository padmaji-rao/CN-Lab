from numpy import Inf
def dijkstras(graph,s):
    l=len(graph)
    dist=[Inf for i in range(l)]
    vis=[False for i in range(l)]
    dist[s]=0
    prev=[-1 for i in range(l)]
    for i in range(l):
        u=-1
        for x in range(l):
            if not vis[x] and (u==-1 or dist[x]<dist[u]):
                u=x
        vis[u]=True
        for v,d in graph[u]:
            if dist[u]+d<dist[v]:
                dist[v]=d+dist[u]
                prev[v]=u
    return dist,prev



def path(graph,s,end):
    dis,pre=dijkstras(graph,s)
    at=end
    path=[]
    while at!=-1:
        path.append(str(at))
        at=pre[at]
    path.reverse()
    print("path from",s,"to",end,"is:",'--->'.join(path))
    print("Distance:",dis[end])


graph={
    0:[(1,1)],
    1:[(0,1),(2,2),(3,3)],
    2:[(1,2),(3,1),(4,5)],
    3:[(1,3),(2,1),(4,1)],
    4:[(2,5),(3,1)]
}


for i in range(len(graph)):
    path(graph,0,i)
    print("***************************************")

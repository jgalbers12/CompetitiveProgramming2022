import queue
import sys

def bfs(f, s, g, u, d):
    visited = [False for i in range(f)]
    q = queue.Queue(maxsize = f)
    dist = [0 for i in range(f)]
    q.put(s-1)
    visited[s-1] = True
    dist = [-1 for i in range(f)]
    dist[s-1] = 0
    while q.empty() == False:
        c = q.get()
        if c == g - 1:
            print(dist[c])
            sys.exit()
        next_down = c - d
        next_up = c + u
        if next_up < f and not visited[next_up]:
            q.put(next_up)
            visited[next_up] = True
            dist[next_up] = dist[c] + 1
        if next_down >= 0 and not visited[next_down]:
            q.put(next_down)
            visited[next_down] = True
            dist[next_down] = dist[c] + 1
    print("use the stairs")

if __name__ == "__main__":
    i = [int(i) for i in sys.stdin.readline().split()]
    bfs(i[0], i[1], i[2], i[3], i[4])
    

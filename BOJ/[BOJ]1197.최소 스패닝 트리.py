from sys import stdin

def main():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a, b = find_parent(parent, a), find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    v, e = map(int, stdin.readline().split())
    parent = [i for i in range(v+1)] #parents 초기화
    edges = []
    for _ in range(e):
        s, e, cost = map(int, stdin.readline().split())
        edges.append((cost, s, e))
    edges.sort() #비용 적게 드는 순으로 정렬

    result = 0
    for cost, s, e in edges:
        if find_parent(parent, s) != find_parent(parent, e):
            union_parent(parent, s, e)
            result += cost
    return result

if __name__ == '__main__':
    print(main())

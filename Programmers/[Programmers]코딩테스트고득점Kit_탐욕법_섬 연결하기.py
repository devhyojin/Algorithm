def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    answer = 0
    for i1, i2, c in costs:
        if find_parent(parent, i1) != find_parent(parent, i2):
            union_parent(parent, i1, i2)
            answer += c

    return answer
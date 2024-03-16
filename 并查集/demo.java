class UnionFind {
    public int[] parent;
    public int[] personNums;

    public UnionFind() {
        parent = new int[10000001];
        personNums = new int[10000001];
        for (int i = 1; i <= 10000000; i++) {
            parent[i] = i;
            personNums[i] = 1;
        }
    }

    public int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]); // 路径压缩, 这一步不优化过不去
        }
        return parent[x];
    }

    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY)
            return;
        parent[rootY] = rootX;
        personNums[rootX] += personNums[rootY];
    }
}
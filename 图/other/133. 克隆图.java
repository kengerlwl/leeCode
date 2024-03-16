import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    public HashMap<Node, Node> visited = new HashMap<Node, Node>();
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }
        dfs(node);
        return visited.get(node);
        
    }


    public void dfs(Node node) {
        if (visited.containsKey(node)) { // 已经访问过了，pass
            return;
        }
        visited.put(node, new Node(node.val, new ArrayList<Node>())); // 创建一个新的节点
        for (Node neighbor : node.neighbors) { // 遍历邻居节点
            if (!visited.containsKey(neighbor)) { // 如果邻居节点没有被访问过, 递归访问建立，这样下一步就直接把邻居节点加入到当前节点的邻居列表中
                dfs(neighbor);
            }
            visited.get(node).neighbors.add(visited.get(neighbor)); // 将邻居节点加入到当前节点的邻居列表中
        }
    }
}
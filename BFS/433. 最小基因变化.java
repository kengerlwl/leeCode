import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
    // ���ڴ洢�����
    public HashSet<String> set = new HashSet<String>();

    // vis
    public HashSet<String> vis = new HashSet<String>();


    public int minMutation(String startGene, String endGene, String[] bank) {
        for (String gene : bank) {
            set.add(gene);
        }
        // ���Ŀ������ڻ�����У�ֱ�ӷ���-1
        if (!set.contains(endGene)) {
            return -1;
        }
        int ans = 0;
        List<String> queue = new ArrayList<>();
        queue.add(startGene);
        while (queue.size() != 0) {
            int size = queue.size();
            for(int i =0; i < size; i++){
                String cur = queue.remove(0);
                if (cur.equals(endGene)) {
                    return ans;
                }
                // System.out.println("cur: " + cur);
                for(int j = 0; j < cur.length(); j++) {
                    for(char c : new char[]{'A', 'C', 'G', 'T'}) { // �������п��ܵøı䷽ʽ
                        if (c == cur.charAt(j)) {
                            continue;
                        }

                        // �滻����
                        String newGene = cur.substring(0, j) + c + cur.substring(j + 1);
                        if (set.contains(newGene) && !vis.contains(newGene)) {
                            queue.add(newGene);
                            vis.add(newGene);
                        }
                    }
                }

                
            }
            ans++;
        }

        return -1;

    }

    // startGene =
    // "AACCGGTT"
    // endGene =
    // "AACCGCTA"
    // bank =
    // ["AACCGGTA","AACCGCTA","AAACGGTA"]
    
    public static void main(String[] args) {
        Solution s = new Solution();
        String startGene = "AACCGGTT";
        String endGene = "AACCGCTA";
        String[] bank = new String[]{"AACCGGTA","AACCGCTA","AAACGGTA"};
        System.out.println(s.minMutation(startGene, endGene, bank));
    }   
}
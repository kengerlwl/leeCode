class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Deque<Integer> path = new ArrayDeque<>();
        int len = nums.length;
        backtracking(nums, 0, len, res, path);
        return res;

    }

    private void backtracking(int[] nums, int begin, int len, List<List<Integer>> res, Deque<Integer> path) {
        if (path.size() == nums.length) {
            res.add(new ArrayList(path));
            return;
        }

        for (int i = 0; i < len; i++) {
            if (path.contains(nums[i]))
                continue;
            path.addLast(nums[i]);
            backtracking(nums, i + 1, len, res, path);
            path.removeLast();
        }
    }
}
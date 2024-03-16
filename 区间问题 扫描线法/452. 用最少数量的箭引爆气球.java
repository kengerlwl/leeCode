import java.util.Arrays;

class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points == null || points.length == 0) {
            return 0;
        }

        // 按照气球的左边界排序
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));

        int arrowPosition = points[0][1]; // 初始化箭的位置为第一个气球的右边界
        int minArrows = 1; // 初始化箭的数量为1

        // 遍历气球数组，贪心地更新箭的位置和数量
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > arrowPosition) {
                // 当前气球的左边界超出箭的位置，需要增加箭的数量，并更新箭的位置为当前气球的右边界
                minArrows++;
                arrowPosition = points[i][1];
            } else {
                // 当前气球的左边界在箭的位置范围内，更新箭的位置为两者较小的右边界
                arrowPosition = Math.min(arrowPosition, points[i][1]);
            }
        }

        return minArrows;
    }
}

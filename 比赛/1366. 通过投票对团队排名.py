class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        # 初始化哈希映射
        ranking = collections.defaultdict(lambda: [0] * n)
        # 遍历统计
        for vote in votes:
            for i, vid in enumerate(vote):
                ranking[vid][i] += 1

        # 取出所有的键值对
        result = list(ranking.items())
        # 排序
        result.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return "".join([vid for vid, rank in result])


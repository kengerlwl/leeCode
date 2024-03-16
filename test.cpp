#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int h, w;
    cin >> h >> w;
    int m;
    cin >> m;

    vector<pair<int, int>> lines[2];
    // 0: y = x, 1: y = -x
    for (int i = 0; i < m; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (x1 + y1 == x2 + y2) {
            if (x1 > x2)
                swap(x1, x2), swap(y1, y2);
            lines[0].push_back(make_pair(x1, y1));
            lines[0].push_back(make_pair(x2, y2));
        } else {
            if (x1 > x2)
                swap(x1, x2), swap(y1, y2);
            lines[1].push_back(make_pair(x1, y1));
            lines[1].push_back(make_pair(x2, y2));
        }
    }

    int ans = 1;
    for (int k = 0; k < 2; k++) {
        sort(lines[k].begin(), lines[k].end());
        int n = lines[k].size();
        for (int i = 0; i < n - 1; i++) {
            int d = lines[k][i + 1].first - lines[k][i].first;
            if (d > 1)
                ans++;
        }
    }

    cout << ans << endl;
    return 0;
}

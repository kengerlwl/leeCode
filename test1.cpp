#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int main()
{
    int h, w;
    cin >> h >> w;
    int m;
    cin >> m;


    map<double, set<double>> lines;

    for(int i = 0; i < m; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        double k, b;
        if (x1 == x2) {
            k = 99999999999999999;
        } else {
            k = static_cast<double>(y2 - y1) / (x2 - x1);

        }
        b = y1 - k * x1;

        // 存在
        auto p = lines.find(k);
        if(p != lines.end()){
            // 插入到集合
            p->second.insert(b);
        }
        else{
            lines[k] = {b};
        }
    }





    cout << ans << endl;
    return 0;
}

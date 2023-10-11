#include <iostream>
#include <vector>
#include <tuple>
#include <limits>

using namespace std;

int main() {
    int N, E;
    cin >> N >> E;

    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(u, v, w);
    }

    vector<int> distance(N + 1, numeric_limits<int>::max());
    distance[1] = 0;

    for (int _ = 0; _ < N - 1; ++_) {
        for (const auto& edge : edges) {
            int u, v, w;
            tie(u, v, w) = edge;

            if (distance[u] != numeric_limits<int>::max() && distance[u] + w < distance[v]) {
                distance[v] = distance[u] + w;
            }
        }
    }

    vector<int> ans;
    for (int node = 1; node <= N; ++node) {
        ans.push_back((distance[node] != numeric_limits<int>::max()) ? distance[node] : 30000);
    }

    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}

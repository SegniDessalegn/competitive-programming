class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> ans;
        vector<int> path;
        dfs(0, graph, path, ans);
        return ans;
    }

private:
    void dfs(int node, const vector<vector<int>>& graph, vector<int>& path, vector<vector<int>>& ans) {
        path.push_back(node);

        if (node == graph.size() - 1) {
            ans.push_back(path);
        } else {
            for (auto neighbor : graph[node]) {
                dfs(neighbor, graph, path, ans);
            }
        }

        path.pop_back();
    }
};
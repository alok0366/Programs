#include <bits/stdc++.h>
using namespace std;
void addEdge(vector<int> v[],int x,int y)
{
    v[x].push_back(y);
    v[y].push_back(x);
}
void printPath(vector<int> stack)
{
    int i;
    for (i = 0; i < (int)stack.size() - 1;i++) {
        cout << stack[i] << " -> ";
    }
    cout << stack[i];
}
void DFS(vector<int> v[],bool vis[],int x,int y,vector<int> stack)
{
    stack.push_back(x);
    if (x == y) {
        printPath(stack);
        return;
    }
    vis[x] = true;
    int flag = 0;
    if (!v[x].empty()) {
        for (int j = 0; j < v[x].size(); j++) {
            if (vis[v[x][j]] == false) {
                DFS(v, vis, v[x][j], y, stack);
                flag = 1;
            }
        }
    }
    if (flag == 0) {
        stack.pop_back();
    }
}
void DFSCall(int x,int y,vector<int> v[],int n,vector<int> stack)
{
    bool vis[n + 1];
    memset(vis, false, sizeof(vis));
    DFS(v, vis, x, y, stack);
}
int main()
{
    int t;
    while(t--){
        int n,x,y;
        cin>>n;
        vector<int> v[n], stack;
        for(int i=0;i<n-1;i++){
            cin>>x>>y;
    // Vertex numbers should be from 1 to 9.
            addEdge(v, x, y);
        }
        int hq[n],q;
        for(int i=0;i<n;i++){
            cin>>hq[i];
        }
        cin>>q;
        int src,dest;
        for(int i=0;i<q;i++){
            cin>>src>>dest;
            DFSCall(src, dest, v, n, stack);
        }
    }

    return 0;
}

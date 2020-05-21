#include <bits/stdc++.h>
#define M 1000000007
#define ll long long
using namespace std;
vector<long long>temp;

void SieveOfEratosthenes(long long n, bool prime[],
                         bool primesquare[], long long a[])
{
    for (long long i = 2; i <= n; i++)
        prime[i] = true;

    for (long long i = 0; i <= (n * n + 1); i++)
        primesquare[i] = false;

    prime[1] = false;

    for (long long p = 2; p * p <= n; p++) {
        if (prime[p] == true) {
            for (long long i = p * 2; i <= n; i += p)
                prime[i] = false;
        }
    }

    long long j = 0;
    for (long long p = 2; p <= n; p++) {
        if (prime[p]) {
            a[j] = p;

            primesquare[p * p] = true;
            j++;
        }
    }
}
long long countDivisors(long long n)
{
    if (n == 1)
        return 1;

    bool prime[n + 1], primesquare[n * n + 1];

    long long a[n];
    SieveOfEratosthenes(n, prime, primesquare, a);

    long long ans = 1;
    for (long long i = 0;; i++) {

        if (a[i] * a[i] * a[i] > n)
            break;

        long long cnt = 1;
        while (n % a[i] == 0)
        {
            n = n / a[i];
            cnt = cnt + 1;
        }

        ans = ans * cnt;
    }


    if (prime[n])
        ans = ans * 2;


    else if (primesquare[n])
        ans = ans * 3;


    else if (n != 1)
        ans = ans * 4;

    return ans;
}



void add_edge(vector<long long> adj[], long long src, long long dest)
{
    adj[src].push_back(dest);
    adj[dest].push_back(src);
}

bool BFS(vector<long long> adj[], long long src, long long dest, long long v,
                            long long pred[], long long dist[])
{
    list<long long> queue;

    bool visited[v];
    for (long long i = 0; i < v; i++) {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }
    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);
    while (!queue.empty()) {
        long long u = queue.front();
        queue.pop_front();
        for (long long i = 0; i < adj[u].size(); i++) {
            if (visited[adj[u][i]] == false) {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);


                if (adj[u][i] == dest)
                   return true;
            }
        }
    }

    return false;
}

void printShortestDistance(vector<long long> adj[], long long s,long long dest, long long v)
{
    long long pred[v], dist[v];

    if (BFS(adj, s, dest, v, pred, dist) == false)
    {
        return;
    }

    // vector path stores the shortest path
    vector<long long> path;
    long long crawl = dest;
    path.push_back(crawl);
    while (pred[crawl] != -1) {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }
    for (long long i = path.size() - 1; i >= 0; i--){
        temp.push_back(path[i]);}
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long long t;
    cin>>t;
    while(t--){
    // no. of vertices
    long long v;
    cin>>v;
    vector<long long> adj[v+10];
    long long aa,bb;
    for(long long i=0;i<v-1;i++){
            cin>>aa>>bb;
    add_edge(adj, aa%M, bb%M);}
    long long q,hq[v];
    for(long long i=0;i<v;i++){
        cin>>hq[i];}
    cin>>q;
    long long source,dest;
    for(long long i=0;i<q;i++){
            cin>>source>>dest;
            if((source%M)==(dest)%M){cout<<(countDivisors(hq[dest-1])%M) <<"\n";}
            else{
                printShortestDistance(adj, source, dest, v+10);
                long long prd=1;
                for(auto p:temp){
                    prd=(prd*hq[p-1])%M;
                    }
                cout<<(countDivisors(prd)%M)<<"\n";
                temp.clear();
            }
        }
    }
    return 0;
}

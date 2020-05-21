// C++ implementation of the approach
#include <bits/stdc++.h>
using namespace std;
#define MAX 100005
typedef long long ll;

// Segment tree implemented as an array
ll tree[MAX << 2];

// Function to build segment tree
void build(int node, int start, int end, const int* arr, int k)
{
    if (start == end) {
        tree[node] = arr[start] % k;
        return;
    }
    int mid = (start + end) >> 1;
    build(2 * node, start, mid, arr, k);
    build(2 * node + 1, mid + 1, end, arr, k);
    tree[node] = (tree[2 * node] * tree[2 * node + 1]) % k;
}

// Function to query product % k
// of sub-array[l..r]
ll query(int node, int start, int end, int l, int r, int k)
{
    if (start > end || start > r || end < l)
        return 1;
    if (start >= l && end <= r)
        return tree[node] % k;
    int mid = (start + end) >> 1;
    ll q1 = query(2 * node, start, mid, l, r, k);
    ll q2 = query(2 * node + 1, mid + 1, end, l, r, k);
    return (q1 * q2) % k;
}

// Function to return the count of sub-arrays
// whose product is divisible by K
ll countSubarrays(int* arr, int n, int k)
{

    ll ans = 0;

    for (int i = 0; i < n; i++) {

        int low = i, high = n - 1;

        // Binary search
        // Check if sub-array[i..mid] satisfies the constraint
        // Adjust low and high accordingly
        while (low <= high) {
            int mid = (low + high) >> 1;
            if (query(1, 0, n - 1, i, mid, k) != 2)
                high = mid - 1;
            else
                low = mid + 1;
        }
        ans += n - low;
    }
    return ans;
}

int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,x,c=0;
        cin>>n;
        int arr[n];
        for(ll i=0;i<n;i++){
            cin>>x;
            arr[i]=x%4;
            if(x%4!=2){
                c++;
            }
        }


    int z = sizeof(arr) / sizeof(arr[0]);
    int k = 4;

    build(1, 0, n - 1, arr, k);

    cout << countSubarrays(arr, n, k)<<"\n"
    ; }

    return 0;
}

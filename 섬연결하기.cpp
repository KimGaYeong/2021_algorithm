#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#define MAX 100
using namespace std;

int parent[MAX];

// #3 cycle 확인하기 2
int find_parent(int x){
    if(parent[x] == x) return x;
    return parent[x] = find_parent(parent[x]);
}

// #2 compare -> '가중치' 를 기준으로 '오름차순' 정렬 해야 함
bool compare(vector<int> v1, vector<int> v2){
    return v1[2] < v2[2] ;
}

// #5 간선과 간선을 union.
// 어짜피 이어져는 있겠다, 누가 다음 간선이랑 이어질 지 정하면 됨.
void E_union(int E1, int E2){
    if (E1<E2) parent[E2] = E1;
    else parent[E1] = E2;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    int E1, E2;
    // #1 - sorting 해주기 - 오름차순으로.
    sort(costs.begin(), costs.end(), compare); 
    // #3 cycle 확인하기1
    for(int i=0;i<n;i++) parent[i] = i;
    
    // #4 cycle 확인 돌리고 간선 끼리 union
    for(int i=0;i<costs.size();i++){
        E1 = find_parent(costs[i][0]);
        E2 = find_parent(costs[i][1]);
        if(E1 != E2){
            answer += costs[i][2];
        }
        E_union(E1, E2);
    }
    return answer;
}
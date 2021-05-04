#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    
    int answer =1;
    queue<pair<int, int>> q_print;
    priority_queue<int> pq_print;
    
    int ps = priorities.size();
    //first = priority, second = location
    for(int i=0;i<ps;i++){
        q_print.push(make_pair(priorities[i], i));
        pq_print.push(priorities[i]);
    }
    
    while(!q_print.empty()){
        if(q_print.front().first == pq_print.top()){
            if(q_print.front().second == location){
                return answer;
            }
            else{
                q_print.pop();
                pq_print.pop();
                answer++;
            }
        }
        else{
            q_print.push(q_print.front());
            q_print.pop();  
        }
    }
    
}
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    
    int time = 0; //answer
    int next = 0; //next truck index
    int weight_sum = 0;
    queue<int> bridge;
    
    while(1){
        time++;
        if(bridge.size() == bridge_length){
            weight_sum -= bridge.front();
            bridge.pop();
        }
        if(weight_sum + truck_weights[next] <= weight){
            if(next == truck_weights.size()-1){
                time += bridge_length;
                break;
            }
            else{
            bridge.push(truck_weights[next]);
            weight_sum += truck_weights[next];
            next++;
            }
        }
        else bridge.push(0);
    }
    return time;
}
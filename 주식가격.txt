#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int k;
    for (int i = 0; i < size(prices) ; i++) {
        k=0;
        for (int j = i+1; j < size(prices); j++) {
            if (prices[i] <= prices[j]) {
                k++;
            }
            else{
                k++;
                break;
            }
        }
        answer.push_back(k);
    }
    return answer;
}
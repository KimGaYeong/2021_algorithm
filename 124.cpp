#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    vector<int> vec;
    
    while(n!=0){
        if(n%3 !=0){
            vec.insert(vec.begin(), n%3);
            n /= 3;
        }
        else if( n%3 ==0){
            vec.insert(vec.begin(), 4);
            n = (n/3) -1;
        }
    }
    for(int i=0;i<vec.size();i++){
        answer.append(to_string(vec[i]));
    }
    return answer;
}
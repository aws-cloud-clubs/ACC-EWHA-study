#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(const vector<int> & command : commands){
        int i= command[0] -1;
        int j = command[1]-1;
        int k = command[2]-1;
        
        // i부터 j번째까지 자른 부분의 배열 
        vector<int> subarray(array.begin() + i, array.begin() + j +1); 
        
        // 자른 배열을 정렬하기 
        sort(subarray.begin(), subarray.end());
        
        // k번째 숫자 추출 (0부터 시작하는 인덱스에서 k번째 값)
        answer.push_back(subarray[k]);
        
    }
    
    
    return answer;
}
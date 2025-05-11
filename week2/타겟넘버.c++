#include <string>
#include <vector>

using namespace std;

/* 
&: 참조 변수, 원본 변수의 메모리 주소를 공유
값을 직접 수정 가능
count 는 계속 증가해야 하는 변수이므로 참조 변수를 쓴다
*/
void dfs(const vector<int>& numbers, int index, int sum, 
        int target, int& count){
    
    /*
    모든 숫자를 사용한 경우
    dfs 는 숫자 하나씩 처리하면서 다음 숫자로 이동하기 때문에 index+1이 반복
    배열 끝까지 탐색하면 index == numbers.size()가 된다. 
    */
    if (index == numbers.size()){ 
        // 합한 결과가 타겟 숫자를 만들었다면 count 증가
        if(sum == target) {
            count++; 
        }
        return;
    }
    
    /*
    재귀함수 호출 
    현재 숫자를 더하는 경우
    index+1: 다음 숫자로 이동한다. 
    sum + numbers[index]: 현재까지의 합(sum)에 현재 숫자를 더함
    */
    dfs(numbers, index +1, sum +numbers[index], target, count);
    
    // 현재 숫자를 빼는 경우 
    dfs(numbers, index+1, sum-numbers[index], target, count);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    /*
    입력된 숫자 배열 그대로 전달
    타겟넘버도 그대로 전달 
    정답은 0부터 시작하므로 이 상태로 dfs 호출하는 것 
    */
    dfs(numbers, 0,0,target, answer);
    return answer;
}
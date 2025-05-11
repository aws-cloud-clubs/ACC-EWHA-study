#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 두 문자열을 비교하는 함수
bool compare(string a, string b) {
    return a + b > b + a;  // a+b가 b+a보다 크면 a가 앞에 와야 함
}

string solution(vector<int> numbers) {
    string answer = "";
    
    // 정수 배열을 문자열로 변환
    vector<string> str_numbers;
    for (int num : numbers) {
        str_numbers.push_back(to_string(num));
    }

    // 문자열 배열을 비교 함수에 따라 정렬
    sort(str_numbers.begin(), str_numbers.end(), compare);

    // 가장 큰 수가 "0"만 있을 경우 "0"을 반환
    if (str_numbers[0] == "0") {
        return "0";
    }

    // 정렬된 숫자들을 이어붙여서 결과 생성
    for (const string& num_str : str_numbers) {
        answer += num_str;
    }

    return answer;
}

# ACC-EWHA-study
ACC EWHA 코딩테스트 스터디를 위한 리포지토리입니다. 

## 250511
### 1. N으로 표현 
숫자 N을 최대 8번까지 사용해서 사칙연산과 숫자 이어 붙이기(5, 55, 555 등)를 조합하여, number를 만드는 최소 횟수를 구하는 문제.
- 동적 프로그래밍(DP): 여기선 N을 1번 쓴 경우부터 8번까지 쓴 경우를 모두 저장하면서 점점 확장.
- 언어를 Java로 바꾸면서 다시 자료구조를 공부하고 있습니다..
- `List<Set<Integer>>` 
  - 리스트 안에 Set 객체들을 넣은 구조로, 각 리스트 항목은 Set<Integer>이다. 
  - Set<Integer>에는 해당 i번 사용으로 만들 수 있는 수를 저장
- `new HashSet<>();`
  - HashSet은 Set 인터페이스를 구현한 클래스 중 하나로, 중복을 허용하지 않으며 순서를 보장하지 않는 자료구조
- `dp.add(new HastSet<>());`
  - dp.get(0) → N을 1번 사용해서 만들 수 있는 수들 
  - dp.get(1) → N을 2번 사용해서 만들 수 있는 수들
  - ......
  - dp.get(7) → N을 8번 사용해서 만들 수 있는 수들
- `num = num *10 + N;`: 이어붙이기 
  - N=5일 때 i=1~3까지 각각 5, 55, 555 이렇게 만드는 부분
  - 55= 50 + 5, 555= 500 + 55 라고 생각
- `for (int a : dp.get(j))`
  - j번으로 만든 숫자 a
- `for (int b : dp.get(i-j))`
  - (i-j)번으로 만든 숫자 b
- ConcurrentModificationException(동시 수정 예외) 를 방지하기 위해서 temp와 dp.get(i)를 나눠서 사용한다

## 250512
### 배열의_평균값
```
double answer = 0;
answer = Arrays.stream(numbers).average().orElse(0);
```
- `stream()`은 배열을 스트림(Stream) 객체로 변환하는 메서드
- 스트림은 데이터를  평균, 합계, 필터링, 매핑 같은 작업을 반복문 없이 간결하게 처리
- `average()`는 스트림의 모든 숫자들의 평균값을 계산해서 `OptionalDouble`로 리턴
- OptionalDouble은 결과가 없을 수도 있는 평균값을 담는 상자(객체)
- 만약 배열이 비어 있어서 평균을 구할 수 없다면, `orElse(0)`을 통해 기본값 0을 반환
### 뒤집힌_문자열
```dockerfile
StringBuilder sb = new StringBuilder(my_string);

String result = sb.reverse().toString();
```
- `StringBuilder`는 `java.lang` 패키지에 포함된 클래스로, 문자열을 수정하거나 조작할 수 있도록 설계된 가변(mutable) 객체로 사용된다.
- 문자열 수정 및 조작할 때 사용하는 메서드가 `append()`, `reverse()` 등이 있다. 
- `toString()`은 뒤집한 결과를 리턴 타입에 맞춰서 다시 문자열로 변환해서 반환한다. 
- 반면에, 자바의 `String`은 불변(immutable) 객체로, 수정할 수 없고 새로운 문자열이 만들어진다. 
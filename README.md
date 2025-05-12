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

### 짝수홀수_개수
```dockerfile
int[] answer = new int[2]
.
.
answer[0]=evenCount;
answer[1]=oddCount;
```
- 배열 선언 및 생성 먼저 해주어야 한다.
- 배열은 인덱스로 값을 넣어야 한다. 
#### 또다른 풀이 
```dockerfile
int[] answer = {}; // 필요없음. 길이가 0인 int 배열을 생성
        answer = IntStream.of(

                (int)Arrays.stream(numList)
                        .filter(i-> i%2 ==0)
                        .count(),
                (int)Arrays.stream(numList)
                        .filter(i->i%2 ==1)
                        .count()

        ).toArray();
```
- `numList` 배열을 Stream<Integer>로 변환
- 조건(짝수만 걸러냄) 만족하는 값들만 남기기 위한 필터 
- `.count()` 는 남은 요소들의 개수(짝수의 개수)
- `.count()`는 long 타입을 반환하므로, int로 형변환 필요 
- `IntStream.of(...)`는 IntStream 타입의 스트림 생성, `.toArray()`로 int 배열([])로 변환
  - `IntStream stream = IntStream.of(1, 2, 3, 4, 5, 6); //IntStream 타입의 스트림`
  - ```
    // 배열의 for문 
    // 이것보다 스트림에서 filter 적용한 것이 더 직관적이다. 
    int[] arr = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i : arr) {
    if (i % 2 == 0) sum += i;
    }```

### 아이스_아메리카노
```dockerfile
int[] answer = IntStream.of(
                        money / 5500,
                        money % 5500)
                .toArray();
```
- `IntStream은` `java.util.stream.IntStream`에 있으므로 import 해주어야 한다. 
- `IntStream.of(...)`는 여러 개의 int 값을 직접 스트림으로 만들 때 쓰는 것이다. 
- 여기서는 money / 5500 과 money % 5500은 그냥 int 값 2개이므로, `Arrays.stream(...)`은 쓸 필요가 없다. 

### 배열_뒤집기 
#### List 와 Collection
- List는 인터페이스이고, 자주 쓰는 대표 구현체는 ArrayList
- 선언: `List<Integer> list = new ArrayList<>();`
```dockerfile
List<String> list = new ArrayList<>();
list.add("hello");
list.add("world");

```
- Collection은 List, Set, Queue 등을 포함하는 **상위 개념(인터페이스)** 이다.  즉, List도 Collection의 일종
```dockerfile
// 이렇게도 쓸 수 있다. 
Collection<Integer> col = new ArrayList<>();
col.add(1);
col.add(2);

```
- List 같은 Collection들을 조작할 수 있는 유틸리티 클래스로, `Collections.reverse()`는 List를 뒤집을 때 자주 쓰는 유틸리티

```dockerfile
import java.util.*;

List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));
Collections.reverse(list); // 리스트가 뒤집힌다. 
System.out.println(list);  // 출력: [3, 2, 1]

```
- 자바는 List를 데이터 저장 구조로,
  Collections를 조작 도구 유틸리티 클래스로 역할을 분리해 놓았어요.
  그래서 .sort(), .reverse(), .shuffle() 같은 동작은 전부 Collections에서 처리하게 되어 있어요.

#### List vs Array
#### Array
- int[], String[], 고정됨 (생성 시 정해진 크기 변경 불가)
- 기본적인 요소 접근 (arr[i])만 가능
- 기본 타입 배열 가능 (int[])
#### List
- List<Integer>, ArrayList<String>, 유동적 (요소 추가/삭제 가능)
- 요소 추가, 삭제, 검색, 정렬 등 다양한 메서드 제공
- 객체 타입만 가능 (List<Integer>, List<String>)
```dockerfile
String[] arr = {"a", "b", "c"};
List<String> list = Arrays.asList(arr);  // 배열 → 리스트로 변환
Collections.reverse(list);               // 리스트 뒤집기

```
- reverse() 같은 기능은 배열에는 직접 지원되지 않아서, 배열을 List로 변환하고 나서 Collections.reverse()를 사용
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

#### 솔루션 1
```dockerfile
int[] answer = new int[num_list.length];
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[num_list.length - 1 - i];
        }
```
- 가장 기본, 배열로 풀기. 
- 인덱스를 `[.length-1-i]` 로 두어 거꾸로 채운다. 

#### 솔루션 2
- 자바에서 `.stream()`은 컬렉션(Collection) 또는 배열을 스트림(Stream)으로 바꿔주는 메서드
- 배열 또는 컬렉션의 데이터를 하나씩 처리
- 우선, num_list 은 기본형 배열(`int[]`)이므로, 이를 스트림 연산을 하면 `IntStream` 이 된다.
- 이유: `Arrays.stream(int[] array)` 메서드는 다음처럼 오버로딩되어 있다. 
```dockerfile
// 배열이 int[]일 경우
public static IntStream stream(int[] array)

```
- **즉, 기본형 배열인 `int[]`을 스트림으로 변환하면 `IntStream을` 리턴!** >> 중요 
#### 자바의 기본형과 객체형, 그리고 스트림 
- 자바는 기본형(`int`, `double`, `long`)과 객체형(`Integer`, `Double`, `Long`)을 구분한다. 
- `IntStream`: int 전용 스트림 (기본형 스트림) 
- `Stream<Integer>`: `Integer` 객체용 스트림 (객체 스트림)
- 그래서 `int[]` → `IntStream`
- `Integer[]` → `Stream<Integer>`

#### 기본형, 객체형 스트림 변환 
```dockerfile
Arrays.stream(num_list)     // int[] 배열 -> IntStream 배열을 스트림으로 
      .boxed()              // IntStream -> Stream<Integer> 기본형 스트림을 객체용 스트림으로 
      .collect(Collectors.toList()); // Stream<Integer>-> List<Integer> 리스트로 

```
- `IntStream을` `Stream<Integer>`로 바꾸고 싶을 때는 `.boxed()` 사용
- `.boxed()`는 말 그대로 int → Integer로 박싱(boxing) 해주는 메서드. 즉, 기본형 스트림을 객체 스트림으로 바꿔주는 역할
- 이유: `IntStream은` 기본형 int 값들만 다루는 스트림이에요. 반면 `List<Integer>`는 객체(Integer) 들로 구성된 리스트이므로,`IntStream` -> `List<Integer>`로 바로 변환 안됨! 
- `.collect(Collectors.toList())` 는 Stream의 결과를 List로 모으는 메서드(Stream -> List)

```dockerfile
int[] answer = list.stream() // List<Integer> -> Stream<Integer> 
            .mapToInt(Integer::intValue) // Stream<Integer> -> IntStream 
            .toArray(); // IntStream을 int[] 배열로
```
- list는 `List<Integer>` 이다. 
- `List<Integer>`에서 `stream()`을 쓰면 `Stream<Integer>`가 된다. 
- 즉, Integer 객체들이 순차적으로 처리될 수 있게 스트림을 여는 것. 
- 하지만 배열로 바꾸려면 `IntStream` 이어야 `toArray()`를 쓸 수 있기 때문에 `mapToInt()`를 쓴다. 
- `mapToInt(Integer::intValue)`는 `Stream<Integer`>를 `IntStream`으로 바꿔주는 메서드

#### import 
```dockerfile
import java.util.*;
import java.util.stream.*;
```
- `java.util `패키지는 컬렉션 클래스들을 포함: ArrayList, LinkedList, HashMap, HashSet 등
- `java.util.stream `패키지는 스트림 API 관련 클래스들이 포함되어 있는 패키지

### 약수_구하기 
```dockerfile
if(n % (i+1) ==0 ){
                list.add(i+1);
            }
```
- 약수란, 1부터 자기자신까지 나누었을 때 나누어 떨어지는 수
- n % i == 0 인 i는 모두 n의 약수

```dockerfile
answer = list.stream()
                // i->i 도 가능. 자동 언박싱
                .mapToInt(Integer::intValue)
                .toArray();
```
- 리턴 타입이 기본형 배열이므로, 그에 맞추어서 리스트를 배열로 변환해주어야 한다. 
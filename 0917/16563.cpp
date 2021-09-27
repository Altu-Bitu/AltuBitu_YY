#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

/*
1.n과 k를 입력 받음, 미리 최대크기까지이 소수 경로 저장
2.소인수 분해 while문을 통해 수행
- while문 
prime배열에 해당 숫자에 저장된 소수를 리턴하고
해당 소수로 나눈 값으로 다시 수행 (k가 1이 될 때까지 k가 1이하가 되면 while문 종료)

*prime배열 - isPrime함수의 에라토스테네스의 체를 통해 만들어진 소수 경로 저장한 배열

*isPrime함수 - 에라토스테네스의 체를 통해 소수 판별
일단 모든 수를 소수라고 가정 (prime[i]=i라고 초기 세팅)
2부터 소수가 나오면 해당 i의 배수를 모두 찾아가서 i로 값을 바꿔준다 -  이때 만약 이미 더 작은 소수가 존재 한다면 값을 갱신하지 않는다 (값이 자기 자신인 배수일때에만 갱신)
*/

const int SIZE = 5000000; //미리 최대 크기까지의 배열로 소수 경로 저장

//소수 경로 저장해서 리턴하는 함수
vector<int> isPrime() { //입력값은 없고 배열로 값을 리턴하는 함수
    vector<int> prime(SIZE + 1, 0);

    //먼저 모든 수를 소수라 가정하고, i번째 인덱스에 i값 저장
    for (int i = 2; i <= SIZE; i++)
        prime[i] = i;

    //소수 판별
    for (int i = 2; i <= sqrt(SIZE); i++) {
        if (prime[i] == i) { //소수라면
            for (int j = i * i; j <= SIZE; j += i) { //배수에 소수(i) 저장
                if (prime[j] == j) { //저장된 소수가 없을 경우만 - 이미 값이 있을 때에는 갱신하지 않는다
                    prime[j] = i; //소수 저장
                }
            }
        }
    }

    return prime;
}

int main() {
    //입출력 속도 향상
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;

    //입력
    cin >> n;

    //미리 최대 크기까지의 소수 경로 저장
    vector<int> prime = isPrime();

    //입력+연산+출력
    while (n--) {
        //소인수분해할 수 입력
        cin >> k;
        //소인수분해 결과 출력
        while (k > 1) {
            cout << prime[k] << ' '; //prime 배열에 저장된 소수 출력
            k = k / prime[k]; //소수로 나눈 수를 k로 변경하고 k가 1이 될때까지 같은 작업 수행
        }
        cout << '\n';
    }
    return 0;
}
#include <iostream>
#include <vector>

using namespace std;

//유클리드 호제법
int gcd(int a, int b) { //두개의 정수 입력값이 입력 한개의 정수로 출력
    if (b == 0) //b가 0이 되었을때의 a가 최대공약수
        return a;
    return gcd(b, a % b); //a,b의 최대공약수는 a%b,b의 최대공약수인 원리를 이용 다만 이때 a%b가 b보다 작으므로 순서를 바꿔서 입력해줌
}

//가능한 모든 쌍의 최대공약수의 합 구하는 함수
long long gcdSum(int n, vector<int> &v) { //배열로 입력을 받음
    long long ans = 0; //가능한 가장 큰 답의 경우의 수 때문에 long long 사용

    //가능한 모든 쌍의 최대공약수 구한 후 ans 에 더하기
    for (int i = 0; i < n; i++) { //n까지
        for (int j = i + 1; j < n; j++) { //i+1부터 n까지 - 가능한 모든 쌍을 구하기 위해서
            int g = gcd(max(v[i], v[j]), min(v[i], v[j])); //유클리드 호제법을 사용하여 최대공약수 출력- 함수 입력값으로 왼쪽이 더 큰수 오른쪽이 더 작은수로 입력
            ans += g; //함수 결과 나온 최대공약수를 현재 정답에 더한다
        }
    }

    return ans; //정답 리턴
}

/**
 * GCD 합 문제
 * 가능한 모든 쌍의 GCD의 합 구하기
 * n이 최대 100이고, 입력 수가 최대 1,000,000 이므로 가능한 합의 가장 큰 경우는 C(100,2) * 1,000,000 = 4,950,000,000
 * 따라서 정답을 long long 범위로 해야함
 */

int main() {
    int t, n;

    //입력
    cin >> t;

    //입력 + 연산
    while (t--) {
        cin >> n; //n에 변수 저장 - >배열의 크기

        vector<int> v(n, 0); //배열 선언
        for (int i = 0; i < n; i++) {
            cin >> v[i]; //배열에 차례로 변수 저장
        }

        //출력
        cout << gcdSum(n, v) << '\n';
    }
    return 0;
}
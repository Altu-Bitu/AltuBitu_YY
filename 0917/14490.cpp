#include <iostream>

using namespace std;

/*
1.문자로 일단 한 번에 입력 받음
2.입력으로 부터 n과 m을 추출 - :를 기준으로 이전의 문자와 이후의 문자를 숫자로 변경
3.재귀함수로 유클리도 호제법을 구현한 getRecursion함수를 통해서 최대공약수를 리턴받음
-getRecursion함수
a,b의 최대공약수가 a%b,b의 최대공약수와 같다는 원리를 활용
a%b는 b보다 작아지므로 둘의 순서를 바꾸어서 다시 getRecursion함수에 재귀적으로 넣어줌
b==0이 되면 a가 최대공약수이므로 a를 리턴
4.입력받은 최대공약수로 n과 m를 나눈 몫을 받아 이를 :와 함께 출력함 

*/


//재귀함수로 구현한 유클리드 호제법
int gcdRecursion(int a, int b) {
    if (b == 0) //b가 0이면 a가 최대공약수
        return a;
    //a%b구한 후 b와 자리 바꾸어서 호출
    return gcdRecursion(b, a % b);
}

int main() {
    string s; //문자열로 입력을 받아서 가공할 것

    //입력
    cin >> s;

    //연산(입력으로부터 n, m 추출하기)
    int index = s.find(':'); //':' 위치 찾기
    int n = stoi(s.substr(0, index)); //: 이전의 문자를 숫자로 변경
    int m = stoi(s.substr(index + 1, s.length())); //: 이후 문자를 숫자로 변경

    //최대공약수 구하기
    int g = gcdRecursion(max(n, m), min(n, m));

    //출력
    cout << n / g << ':' << m / g << '\n';

    return 0;
}
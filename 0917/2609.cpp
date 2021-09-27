#include <iostream>

using namespace std;

/*
1. 두 개의 정수를 입력받음
2. 입력받은 정수를 a>b가 되도록 순서대로 a,b를 재귀함수를 구하는 함수에 넣음  
-재귀함수를 구하는 함수 getRecursion 
    b(둘 중 작은수)가 0이라면 최대공약수는 a로 리턴
    아니라면 유클리드 호제법에 의해 a%b와 b의 최대공약수와 a,b의 최대공약수가 같으므로 a%b,b를 다시 재귀적으로 함수에 넣어줌 (이때 a%b가 b보다 작아지므로 순서 변경) - b가 0이될 때까지 반복
-gcdBad :그냥 반복문을 돌면서 두 수중 작은 수를 기준으로 하나씩 감소하면서 공약수가 있는지 판단, 공약수로 판별되면 바로 리턴, 이때 끝까지 없다면 최대공약수는 1
3.최소공배수는 A*B = G*L 공식을 이용해서 G로 나누어서 구함

*/





//O(n) 연산
int gcdBad(int a, int b) { //int형태로 출력하고 두 개의 int를 입력으로 받는 함수
    //두 수 중 더 작은거 기준으로 하나씩 감소하며 공약수 있는지 판단
    for (int i = min(a, b); i > 1; i--) {
        //공약수 존재하면 바로 리턴 -> 최대공약수
        if (a % i == 0 && b % i == 0) {
            return i;
        }
    }
    return 1; //끝까지 없다면 최대공약수 1
}

//재귀함수로 구현한 유클리드 호제법
int gcdRecursion(int a, int b) { //int형태로 출력하고 두 개의 int를 입력으로 받는 함수
    if (b == 0) //b가 0이면 a가 최대공약수
        return a;
    //a%b구한 후 b와 자리 바꾸어서 호출  -> a%b가 b보다 작아지기 때문에
    return gcdRecursion(b, a % b); //b가 영이 되기 전에는 계속 반복
}

int main() {
    int a, b; //정수로 입력받음

    //입력
    cin >> a >> b;

    //연산
    //int g = gcdBad(a, b); //O(n) 함수
    int g = gcdRecursion(max(a, b), min(a, b)); //a > b 가 되도록 함수 호출
    int l = (a * b) / g; //최소공배수는 A*B = G*L 공식을 이용해서 G로 나누어서 구함

    //출력
    cout << g << '\n' << l << '\n'; //최대공약수와 회소공배수 순으로 출력

    return 0;
}
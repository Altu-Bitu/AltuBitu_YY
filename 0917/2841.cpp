#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/**
 * 각 줄마다 외계인이 누르고 있는 프렛을 스택에 저장하기
 * 매 입력에 대해 이번에 누를 프렛이 해당 줄에서 가장 높은 프렛이어야 함
 *
 * 1. 이번에 눌러야 할 프렛보다 높은 프렛에서 손가락을 전부 떼기
 * 2. 만약 이번에 눌러야 할 프렛을 누르고 있지 않다면 누르기
 */
int main() {
    int n, p, guitar_string, fret, ans = 0; //ans 가 손을 움직인 횟수  n 음의 수 p 프랫 수 

    cin >> n >> p;
    vector<stack<int>> guitar(7); //1번 줄부터 6번줄 까지
    while (n--) {
        //입력
        cin >> guitar_string >> fret; //줄의 번호와 fret이라는 변수에 현재 프랫 저장

        //연산
        while (!guitar[guitar_string].empty() && guitar[guitar_string].top() > fret) { //프렛에서 손가락 떼기 - 현재 무엇인가 누른 상태인데 가장 높은 프랫이 fret보다 높을때
            ans++; //손가락을 움직인 횟수 +1
            guitar[guitar_string].pop(); //가장 높은 프랫 pop
        }
        if (guitar[guitar_string].empty() || guitar[guitar_string].top() != fret) { //프렛 누르기 - 비어있거나 가장 높은 프랫이 fret이 아닐때
            ans++; //손가락을 움직인 횟수 +1
            guitar[guitar_string].push(fret); //새로운 fret 입력
        }
    }

    //출력
    cout << ans;
}
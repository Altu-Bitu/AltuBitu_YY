#include <iostream>

using namespace std;

string maxNum(string s) {
    string ans = ""; //초기화된 정답
    string temp = ""; //k를 만나기 전까지 담는 변수
    for (int i = 0; i < s.length(); i++) {
        temp += '0';
        if (s[i] == 'K') { //K가 마지막으로 끝나는 십진수 변환
            temp[0] = '5'; //k로 끝났으므로 맨 앞에 수를 5로 바꿔줌
            ans += temp; //정답에 더해줌
            temp = ""; //초기화
        }
    }
    if (temp.length() >= 1) { //K로 끝나지 않았다면 마지막 M모두 1로 변환
        for (int i = 0; i < temp.length(); i++) //모든 temp를 1로 변환
            temp[i] = '1'; //1로 바꿔줌
        ans += temp; //정답에 더해줌 그냥 1000보다 1111 이 더 크므로 다 1로 변경
    }
    return ans; //정답 리턴
}

string minNum(string s) {
    string ans = ""; //초기화된 정답
    string temp = ""; //k만나기 전까지 저장하는 변수
    char first = '1'; //처음 1으로 미리 세팅
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'M') {
            temp += first; //처음이라면 1이 들어가고 그 이후 부터는 0이 들어감
            first = '0'; //first에 0대입
        } else { //'K' -> 그 전까지 M묶음 변환 더하고, K는 따로 변환
            ans += temp + '5'; //k로 인해서 5 대입
            temp = ""; //초기화
            first = '1'; //처음 다시 1로 바꾸어줌 그래야 뒤의 수가 000이 아닌 100 형태로 시작 가능
        }
    }
    if (temp.length() >= 1) //for문을 다 돌고 나온 후 임시 저장한 것이 존재하면
        ans += temp; //정답에 임시 저장한것을 더해줌
    return ans; //정답 반환
}

/**
 * [가장 큰 값]
 * 민겸수에서 마지막이 K일 때, K까지 포함하여 십진수로 변환한다
 * K로 끝나지 않는다면 각 M을 모두 하나로 처리한다 (ex. MMM -> 111)
 *
 * [가장 작은 값]
 * K는 무조건 단독으로 변환한다
 * 나머지 M묶음들은 같이 변환한다
 * ex. MMKMM -> 10510
 */

int main() {
    string s;

    //입력
    cin >> s;

    //출력
    cout << maxNum(s) << '\n' << minNum(s) << '\n';

    return 0;
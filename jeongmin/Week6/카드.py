"""

    [Baekjoon] https://www.acmicpc.net/problem/11652

    숫자 카드 N장을 가지고 있다.
    적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
    많이 가지고 있는 정수를 구하는 프로그램을 작성

"""
import sys
from collections import Counter

def count_card(info):
    """
        info = Counter
    """

    most = info.most_common()
    most.sort(key=lambda x: [x[1], -x[0]], reverse=True)
    return most[0][0]


if __name__ == '__main__':

    N = int(input())

    card_info = Counter()

    for _ in range(N):
        number = int(sys.stdin.readline())

        card_info[number] += 1

    number = count_card(card_info)

    print(number)

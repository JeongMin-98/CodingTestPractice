"""

    [Baekjoon] https://www.acmicpc.net/problem/1449

    가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.

    길이가 L인 테이프를 무한개

    적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.

    항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오.
    테이프를 자를 수 없고,
    테이프를 겹쳐서 붙이는 것도 가능하다.

    정수 1지점은 => pipe[2] 부분

"""

if __name__ == "__main__":
    pipe = [1] * 2001

    N, L = map(int, input().split())
    count = 0

    leak = list(map(int, input().split()))

    for l in leak:
        array_idx = 2 * l
        pipe[array_idx] = 0

    array_L = 2 * L

    if pipe[array_L] == 0:
        for i in range(0, 2 * array_L):
            pipe[i] = 1
        count += 1

    for i in range(2 * array_L, 2001):
        if pipe[i] == 0:
            for j in range()

    print(count)

# 알고리즘 연습 하기 (w Python)

## Leetcode

리트코드 문제풀이는 /leet 경로 아래 위치해요.  
새로 문제를 풀 때 copy_this_template.py를 복사해서 내부의 코드를 변경하세요.

```py
class Solution:
    # 아래 코드를 문제에 등장한 def를 복붙 해주세요.
    def copyFromLeetcodeDefLine(self, s: str) -> int:
        # 여기에 문제를 풀어주세요
        print('type your code')

if __name__ == "__main__":
    solution = Solution()

    # 테스트 케이스를 이곳에 기술합니다.
    # input이 여러개인경우 input을 튜플로 다시 묶어줍니다.
    test_cases = [
        # 튜플로 문제 / 답을 기술해주세요.
        ("QUEST", 'ANSWER'),
        # 제일 바깥 튜플 기준으로 왼쪽이 input 오른쪽이 output 입니다.
        ([1, 2, 3], 6),
        # inputs 인 경우 input 위치를 튜플로 다시 묶어주세요.
        (([1, 2, 3], [3, 4, 5]), [3])
    ]

    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    # 여기 solution.copyFromLeetcodeDefLine 을 복사해온 함수 명으로 변경해주세요.
    run_tests(solution.copyFromLeetcodeDefLine, test_cases)
```

### lib

리트코드에서 따로 규정해 둔 링크드리스트 같은것들이 여기에 구현되어 있어요.  
입력에 따라서 분기해주고 핸들링 해주는것도 leetcode_tester.py 안에 구현되어 있어요.  
input이 여러개인 경우나 output이 여러개일 때 에러가 발생할 수 있으니 코드를 적절히 수정해야할 수 있습니다.

> [!CAUTION]
> input을 테스트코드 바깥에서 참조하는 특이한 경우는 테스트가 어려워요. 그런 문제는 많지 않아서 우선 제출해보면서 대응하고 있습니다.

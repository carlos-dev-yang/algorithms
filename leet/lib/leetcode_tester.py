from typing import List, Tuple, Any, Callable, Optional
from lib.ListNode import ListNode, list_to_linked_list, linked_list_to_list, is_linked_list_input

def compare_outputs(output: Any, expected: Any) -> bool:
    if output is None and expected == []:
        return True
    if isinstance(output, ListNode):
        return linked_list_to_list(output) == expected
    elif isinstance(expected, ListNode):
        return output == linked_list_to_list(expected)
    else:
        return output == expected

def run_tests(solution_func: Callable, test_cases: List[Tuple[Any, Any]]):
    """
    주어진 해결 함수와 테스트 케이스로 테스트를 실행합니다.
    
    :param solution_func: 테스트할 해결 함수
    :param test_cases: (입력, 예상 출력) 형태의 튜플 리스트. 입력은 단일 값 또는 튜플일 수 있습니다.
    :return: (성공한 테스트 수, 전체 테스트 수)
    """
    passed = 0
    total = len(test_cases)
    
    # 함수가 연결 리스트를 입력으로 받는지 확인
    expects_linked_list = is_linked_list_input(solution_func)
    
    for i, (input_data, expected) in enumerate(test_cases, 1):
        try:
            if isinstance(input_data, tuple):
                # 여러 입력 매개변수 처리
                processed_inputs = []
                for inp in input_data:
                    if expects_linked_list and isinstance(inp, list) and all(isinstance(x, int) for x in inp):
                        processed_inputs.append(list_to_linked_list(inp))
                    else:
                        processed_inputs.append(inp)
                result = solution_func(*processed_inputs)
            else:
                # 단일 입력 매개변수 처리
                if expects_linked_list and isinstance(input_data, list) and all(isinstance(x, int) for x in input_data):
                    processed_input = list_to_linked_list(input_data)
                else:
                    processed_input = input_data
                result = solution_func(processed_input)

            status = "통과" if compare_outputs(result, expected) else "실패"
            print(f"테스트 케이스 {i}:")
            print(f"  입력 = {input_data}")
            print(f"  예상 출력 = {expected}")
            if isinstance(result, ListNode):
                print(f"  실제 출력 = {linked_list_to_list(result)}")
            else:
                print(f"  실제 출력 = {result}")
            print(f"  상태: {status}")
            
            if status == "통과":
                passed += 1
        except Exception as e:
            print(f"테스트 케이스 {i}: 오류 발생")
            print(f"  입력 = {input_data}")
            print(f"  예상 출력 = {expected}")
            print(f"  오류 메시지: {str(e)}")
    
    print(f"\n결과: {passed}/{total} 테스트 통과")
    return passed, total
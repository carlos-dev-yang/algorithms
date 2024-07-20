from typing import List, Tuple, Any, Callable
from lib.ListNode import ListNode, list_to_linked_list, linked_list_to_list, is_linked_list_input
from lib.TreeNode import TreeNode, list_to_tree, tree_to_list, is_tree_input
import copy

def compare_outputs(output: Any, expected: Any) -> bool:
    """출력과 예상 값을 비교. expected가 리스트인 경우 여러 답을 허용"""
    if isinstance(expected, list):
        return any(compare_single_output(output, exp) for exp in expected)
    return compare_single_output(output, expected)

def compare_single_output(output: Any, expected: Any) -> bool:
    """단일 출력과 예상 값을 비교"""
    if output is None and expected == []:
        return True
    if isinstance(output, ListNode):
        return linked_list_to_list(output) == expected
    elif isinstance(expected, ListNode):
        return output == linked_list_to_list(expected)
    elif isinstance(output, TreeNode):
        return tree_to_list(output) == expected
    elif isinstance(expected, TreeNode):
        return output == tree_to_list(expected)
    else:
        return output == expected

def process_input(input_data: Any, expects_linked_list: bool, expects_tree: bool) -> Any:
    """입력 데이터를 적절히 처리"""
    if isinstance(input_data, tuple):
        return tuple(process_input(item, expects_linked_list, expects_tree) for item in input_data)
    elif expects_linked_list and isinstance(input_data, list) and all(isinstance(x, int) for x in input_data):
        return list_to_linked_list(input_data)
    elif expects_tree and isinstance(input_data, list):
        return list_to_tree(input_data)
    elif isinstance(input_data, list):
        return [process_input(item, expects_linked_list, expects_tree) for item in input_data]
    else:
        return input_data

def run_tests(solution_func: Callable, test_cases: List[Tuple[Any, Any]]):
    """
    주어진 해결 함수와 테스트 케이스로 테스트를 실행합니다.
    
    :param solution_func: 테스트할 해결 함수
    :param test_cases: (입력, 예상 출력) 형태의 튜플 리스트. 입력은 단일 값 또는 튜플일 수 있습니다.
                       예상 출력은 단일 값 또는 허용 가능한 답변 리스트일 수 있습니다.
    :return: (성공한 테스트 수, 전체 테스트 수)
    """
    passed = 0
    total = len(test_cases)
    
    expects_linked_list = is_linked_list_input(solution_func)
    expects_tree = is_tree_input(solution_func)
    
    for i, (input_data, expected) in enumerate(test_cases, 1):
        try:
            input_copy = copy.deepcopy(input_data)
            processed_input = process_input(input_copy, expects_linked_list, expects_tree)
            
            if isinstance(processed_input, tuple):
                result = solution_func(*processed_input)
            else:
                result = solution_func(processed_input)

            status = "통과" if compare_outputs(result, expected) else "실패"
            print(f"테스트 케이스 {i}:")
            print(f"  입력 = {input_data}")
            print(f"  예상 출력 = {expected}")
            if isinstance(result, ListNode):
                print(f"  실제 출력 = {linked_list_to_list(result)}")
            elif isinstance(result, TreeNode):
                print(f"  실제 출력 = {tree_to_list(result)}")
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
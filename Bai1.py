import re
from typing import Dict

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression: str) -> bool:
    # Danh sách các ký hiệu hợp lệ
    valid_tokens = re.compile(r'[A-Z]|\(|\)|\s|\∧|\∨|\¬|\→|\↔')
    tokens = re.findall(valid_tokens, expression)
    reconstructed_expr = ''.join(tokens)
    return reconstructed_expr == expression

# Hàm chuyển đổi biểu thức logic từ ký hiệu sang dạng Python
def convert_to_python_expression(expression: str) -> str:
    expression = expression.replace("\u2227", " and ") 
    expression = expression.replace("\u2228", " or ")   
    expression = expression.replace("\u00ac", " not ") 
    expression = expression.replace("\u2192", " <= ")  
    expression = expression.replace("\u2194", " == ") 
    return expression

# Hàm tính giá trị của biểu thức logic
def evaluate_expression(expression: str, values: Dict[str, bool]) -> bool:
    # Thay thế các biến bằng giá trị True/False
    for variable, value in values.items():
        expression = expression.replace(variable, str(value))

    # Chuyển đổi biểu thức sang dạng Python
    expression = convert_to_python_expression(expression)

    # Tính giá trị biểu thức
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError("Biểu thức không hợp lệ hoặc có lỗi trong tính toán.")

# Ví dụ demo
if __name__ == "__main__":
    # Kịch bản 1
    expression1 = "(A ∧ B) → ¬C"
    values1 = {
        "A": True,
        "B": False,
        "C": True
    }
    print("Kịch bản 1:")
    if is_valid_expression(expression1):
        print("Biểu thức hợp lệ.")
        try:
            result = evaluate_expression(expression1, values1)
            print("Kết quả biểu thức:", result)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 2
    expression2 = "(A ∨ B) ∧ (C → A)"
    values2 = {
        "A": False,
        "B": True,
        "C": True
    }
    print("Kịch bản 2:")
    if is_valid_expression(expression2):
        print("Biểu thức hợp lệ.")
        try:
            result = evaluate_expression(expression2, values2)
            print("Kết quả biểu thức:", result)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 3
    expression3 = "¬(A → B)"
    values3 = {
        "A": True,
        "B": False
    }
    print("Kịch bản 3:")
    if is_valid_expression(expression3):
        print("Biểu thức hợp lệ.")
        try:
            result = evaluate_expression(expression3, values3)
            print("Kết quả biểu thức:", result)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 4
    expression4 = "(A ↔ B) ∨ C"
    values4 = {
        "A": True,
        "B": True,
        "C": False
    }
    print("Kịch bản 4:")
    if is_valid_expression(expression4):
        print("Biểu thức hợp lệ.")
        try:
            result = evaluate_expression(expression4, values4)
            print("Kết quả biểu thức:", result)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 5
    expression5 = "(A ∨ ¬B) ∧ (C → A)"
    values5 = {
        "A": True,
        "B": False,
        "C": True
    }
    print("Kịch bản 5:")
    if is_valid_expression(expression5):
        print("Biểu thức hợp lệ.")
        try:
            result = evaluate_expression(expression5, values5)
            print("Kết quả biểu thức:", result)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")

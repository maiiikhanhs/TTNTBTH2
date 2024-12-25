import re
from itertools import product
from typing import List, Dict

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression: str) -> bool:
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

# Hàm tạo bảng chân trị
def generate_truth_table(expression: str) -> List[Dict[str, bool]]:
    variables = sorted(set(re.findall(r'[A-Z]', expression))) 
    truth_table = []
    for combination in product([True, False], repeat=len(variables)): 
        values = dict(zip(variables, combination))
        try:
            python_expression = convert_to_python_expression(expression)
            eval_expression = python_expression
            for var, val in values.items():
                eval_expression = eval_expression.replace(var, str(val))
            result = eval(eval_expression)
            truth_table.append({**values, "Kết quả": result})
        except Exception as e:
            raise ValueError("Biểu thức không hợp lệ hoặc lỗi trong tính toán.")
    return truth_table

# Hàm hiển thị bảng chân trị
def display_truth_table(truth_table: List[Dict[str, bool]]):
    header = list(truth_table[0].keys())
    print(" \t".join(header))  
    print("-" * (8 * len(header)))  
    for row in truth_table: 
        print(" \t".join(["T" if row[col] else "F" for col in header]))

# Ví dụ demo
if __name__ == "__main__":
    # Kịch bản 1
    expression1 = "(A ∧ B) → ¬C"
    print("Kịch bản 1:")
    if is_valid_expression(expression1):
        print("Biểu thức hợp lệ.")
        try:
            truth_table = generate_truth_table(expression1)
            display_truth_table(truth_table)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 2
    expression2 = "(A ∨ B) ∧ (C → A)"
    print("Kịch bản 2:")
    if is_valid_expression(expression2):
        print("Biểu thức hợp lệ.")
        try:
            truth_table = generate_truth_table(expression2)
            display_truth_table(truth_table)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 3
    expression3 = "¬(A → B)"
    print("Kịch bản 3:")
    if is_valid_expression(expression3):
        print("Biểu thức hợp lệ.")
        try:
            truth_table = generate_truth_table(expression3)
            display_truth_table(truth_table)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 4
    expression4 = "(A ↔ B) ∨ C"
    print("Kịch bản 4:")
    if is_valid_expression(expression4):
        print("Biểu thức hợp lệ.")
        try:
            truth_table = generate_truth_table(expression4)
            display_truth_table(truth_table)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")
    print()

    # Kịch bản 5
    expression5 = "(A ∨ ¬B) ∧ (C → A)"
    print("Kịch bản 5:")
    if is_valid_expression(expression5):
        print("Biểu thức hợp lệ.")
        try:
            truth_table = generate_truth_table(expression5)
            display_truth_table(truth_table)
        except ValueError as e:
            print(e)
    else:
        print("Biểu thức không hợp lệ.")

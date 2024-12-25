import itertools

def evaluate_expression(expression, values):
    return eval(expression, {}, values)

def find_model(expression):
    # Tìm các biến trong biểu thức
    variables = sorted(set(c for c in expression if c.isalpha()))

    # Tạo tất cả các tổ hợp giá trị True/False cho các biến
    combinations = list(itertools.product([False, True], repeat=len(variables)))

    # Kiểm tra từng tổ hợp giá trị
    for combination in combinations:
        values = dict(zip(variables, combination))

        # Kiểm tra xem biểu thức có đúng với tổ hợp này không
        if evaluate_expression(expression, values):
            return values  # Trả về mẫu giá trị nếu biểu thức đúng

    return None  # Nếu không có mẫu giá trị nào, trả về None

# Các kịch bản demo
expressions = [
    "(A or B) and (not A or C)",        # Kịch bản 1
    "(A and B) or (C and not A)",       # Kịch bản 2
    "A or (B and C)",                   # Kịch bản 3
    "(A and B) and (not C)",            # Kịch bản 4
    "(A or B) and (not A or not C)"     # Kịch bản 5
]

# Thực thi từng kịch bản
for i, expression in enumerate(expressions, 1):
    print(f"Kịch bản {i}:")
    model = find_model(expression)
    if model:
        print(f"Mẫu giá trị tìm được: {model}")
    else:
        print("Không có mẫu giá trị nào làm biểu thức đúng.")
    print("-" * 50)

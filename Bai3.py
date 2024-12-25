def P(x):
    return x > 1

def Q(x):
    return x % 2 == 0

def check_for_all(domain, predicate):
    return all(predicate(x) for x in domain)

def check_exists(domain, predicate):
    return any(predicate(x) for x in domain)

def evaluate_formula(domain):
    # ∀x (P(x) → Q(x))
    forall_condition = check_for_all(domain, lambda x: not P(x) or Q(x))  # P(x) → Q(x) is equivalent to not P(x) or Q(x)
    
    # ∃y P(y)
    exists_condition = check_exists(domain, P)
    
    # Formula: (∀x (P(x) → Q(x))) ∧ (∃y P(y))
    result = forall_condition and exists_condition
    return result

# Kịch bản 1
domain1 = {1, 2, 3}
result1 = evaluate_formula(domain1)
print("Kịch bản 1: The formula is:", "True" if result1 else "False")

# Kịch bản 2
domain2 = {1, 2, 4}
result2 = evaluate_formula(domain2)
print("Kịch bản 2: The formula is:", "True" if result2 else "False")

# Kịch bản 3
domain3 = {2, 3, 4}
result3 = evaluate_formula(domain3)
print("Kịch bản 3: The formula is:", "True" if result3 else "False")

# Kịch bản 4
domain4 = {0, 1, 2}
result4 = evaluate_formula(domain4)
print("Kịch bản 4: The formula is:", "True" if result4 else "False")

# Kịch bản 5
domain5 = {1, 3, 5}
result5 = evaluate_formula(domain5)
print("Kịch bản 5: The formula is:", "True" if result5 else "False")

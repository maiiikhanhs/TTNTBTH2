import itertools

def evaluate_statement(statement, values):
    return statement.format(**values) == "True"

def truth_table(clauses, conclusion, variables):
    combinations = list(itertools.product([False, True], repeat=len(variables)))
    for combination in combinations:
        values = dict(zip(variables, combination))
        all_true = all(evaluate_statement(clause, values) for clause in clauses)
        conclusion_true = evaluate_statement(conclusion, values)
        
        if all_true and not conclusion_true:
            return False  
    return True  

# Kịch bản 1
clauses1 = ["P -> Q", "Q -> R"]
conclusion1 = "P -> R"
variables1 = ["P", "Q", "R"]
result1 = truth_table(clauses1, conclusion1, variables1)
print("Kịch bản 1: Chứng minh:", "Đúng" if result1 else "Sai")

# Kịch bản 2
clauses2 = ["P -> Q", "Q -> R"]
conclusion2 = "Q -> P"
variables2 = ["P", "Q", "R"]
result2 = truth_table(clauses2, conclusion2, variables2)
print("Kịch bản 2: Chứng minh:", "Đúng" if result2 else "Sai")

# Kịch bản 3
clauses3 = ["P -> Q", "Q -> R"]
conclusion3 = "R -> P"
variables3 = ["P", "Q", "R"]
result3 = truth_table(clauses3, conclusion3, variables3)
print("Kịch bản 3: Chứng minh:", "Đúng" if result3 else "Sai")

# Kịch bản 4
clauses4 = ["P -> Q", "Q -> R"]
conclusion4 = "P -> R"
variables4 = ["P", "Q", "R"]
result4 = truth_table(clauses4, conclusion4, variables4)
print("Kịch bản 4: Chứng minh:", "Đúng" if result4 else "Sai")

# Kịch bản 5
clauses5 = ["P -> Q", "R -> Q"]
conclusion5 = "P -> R"
variables5 = ["P", "Q", "R"]
result5 = truth_table(clauses5, conclusion5, variables5)
print("Kịch bản 5: Chứng minh:", "Đúng" if result5 else "Sai")

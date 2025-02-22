def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Validate the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_line = ""
    bottom_line = ""
    dashes_line = ""
    answers_line = ""
    
    for problem in problems:
        # Split the problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        left_operand, operator, right_operand = parts
        
        # Step 2: Validate operands and operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not left_operand.isdigit() or not right_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Step 3: Calculate the result if answers are needed
        if operator == '+':
            result = int(left_operand) + int(right_operand)
        else:
            result = int(left_operand) - int(right_operand)
        
        # Step 4: Format the current problem
        max_len = max(len(left_operand), len(right_operand)) + 2  # +2 for the operator and space
        top_line += f"{left_operand:>{max_len}}    "
        bottom_line += f"{operator} {right_operand:>{max_len-2}}    "
        dashes_line += "-" * max_len + "    "
        if show_answers:
            answers_line += f"{result:>{max_len}}    "
    
    # Step 5: Trim the last four spaces from each line and return the result
    result = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + dashes_line.rstrip()
    if show_answers:
        result += "\n" + answers_line.rstrip()
    
    return result

def main():
    # Accept input as a space-separated string and convert to a list
    problem_input = input("Enter your problems (separate them by a space): ")
    problems = problem_input.split("  ")  # Assumes double spaces between problems
    
    # Get the formatted result
    result = arithmetic_arranger(problems, True)
    
    print(result)

if __name__ == "__main__":
    main()
while True:
    expression = input(
        'Enter calculation:(e.g. 3+5 or q to quit): ').strip()
    if expression == 'q':
        break
    # Use regular expression to validate the input before calling eval.  need to define the input
    print(f"{expression} = {eval(expression)}")

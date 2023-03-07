# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        return f"You called {function.__name__}({args[0], args[1], args[2]})"
    return wrapper


# Use the decorator 👇
@logging_decorator
def Hi(name, age, surname):
    return f'{name},{age},{surname}'


Hi('Pradeep', 18, 'Kurapati')

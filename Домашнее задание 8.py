import re



# Задание 1.
def email_parse(email):
    # Неверное решение задания, не парсит точку и собаку
#    parsed_email = re.findall(r"([a-z0-9_.]+)@([a-z0-9._]+)\.([a-z.]{2,})", email)
#    print(parsed_email)

#    parsed_list = []
#    parsed_list.append(re.search(r"([a-z0-9_.]+)", email).group())
#    parsed_list.append(re.search(r"@([a-z0-9_]+)\.", email).group())
#    parsed_list.append(re.search(r"\.[a-z]+", email).group())

    parsed_email_dict = re.match(r"\w+\@\w+\.\w+", email)
    if parsed_email_dict:
        parse_split = re.split(r"@", email)
        print({"username": parse_split[0], "domain": parse_split[1]})
    else:
        raise ValueError(f'wrong email adress: {email}')

#    return print(parsed_list)

email_parse("maxevg72@gmail.com")

# Задание 3

def type_logger(func):

    def wrapper(*args):
        for num in args:
            result = func(num)
            print(f'[{result}, function name:{func.__name__},{num}: {type(num)}]', end=",")
    return wrapper

@type_logger
def calc_cube(n):
    return n**3

asd = calc_cube(16, 6.5) # Если вставить в args строку, тогда не будет куба
# Нажо убирать перемнную result, но тогда не будет возвращаться куб n

# Задание 4
from functools import wraps
def val_checker(l_func):
    def val_checker(func): # Маскировка работы декоратора
        @wraps(func) # этот метод маскирует работу декоратора
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f"wrong value {num}")

        return wrapper
    return val_checker

@val_checker(lambda m: m > 0)
def calc_cube(m):
    return m**3

calc_cube(5)
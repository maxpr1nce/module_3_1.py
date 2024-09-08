calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return any(item.lower() == string.lower() for item in list_to_search)

# Вызываем функции произвольное количество раз
print(string_info("UrbaN"))
print(is_contains("urban", ["URBAN", "city", "town"]))
print(string_info("Python"))
print(is_contains("Java", ["C#", "C++", "C"]))
print(is_contains("python", ["Java", "C++", "Python"]))

print(f"Количество вызовов: {calls}")
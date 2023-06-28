
def get_input_set():
    return set(input().split())

def is_strict_superset(original, new_set):
    return original.issuperset(new_set) and len(original) > len(new_set)

working_set = get_input_set()
comparison_count = int(input())

result = True
for _ in range(comparison_count):
    if not is_strict_superset(working_set, get_input_set()):
        result = False
        break
    
print(result)


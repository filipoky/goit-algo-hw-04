
# import shutil

# from pathlib import Path

# source_file = '/Users/Yuriy/Documents/Python/Probe/goit-algo-hw-04/zp.txt'

# def total_salary(path):
#     return 

# file_path = Path("zp.txt")

# content = file_path.read_text(encoding="utf-8")
# print(content)


# with open('zp.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# result = content.split(',')
# print(result)  

# obj_query = {}
# for el in content.split(','):
#     key, value = el.split(',')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)



from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропустити порожні рядки
                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"⚠️ Помилка при обробці рядка: {line}")
                    continue
        if count == 0:
            return (0, 0)
        average = total / count
        return (total, average)
    except FileNotFoundError:
        print("❌ Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")
        return (0, 0)

# Приклад використання функції
file_path = 'zp.txt'  # або вкажи повний шлях
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")






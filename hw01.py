
from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки
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
file_path = 'zp.txt'  # або можна вказати повний шлях, але він не буде працювати на GitHub
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



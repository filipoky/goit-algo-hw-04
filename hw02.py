
from pathlib import Path

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки
                try:
                    cat_id, name, age = line.split(',')
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"⚠️ Некоректний рядок: {line}")
                    continue
        return cats_list
    except FileNotFoundError:
        print("❌ Файл не знайдено.")
        return []
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")
        return []

# Приклад використання:
file_path = 'cats.txt'  # можна і абсолютний шлях до файлу, але він не буде працювати на GitHub
cats_info = get_cats_info(file_path)
print(cats_info)


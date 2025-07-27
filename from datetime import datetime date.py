# Імпортуємо необхідні модулі
from datetime import datetime
import random
import re

def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    
    Параметр:
    date (str): рядок з датою у форматі 'РРРР-ММ-ДД'
    
    Повертає:
    int: кількість днів від заданої дати до поточної
    """
    try:
        # Крок 1: Перетворюємо рядок дати у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Крок 2: Отримуємо поточну дату
        current_date = datetime.today()
        
        # Крок 3: Розраховуємо різницю між датами
        difference = current_date - given_date
        
        # Крок 4: Повертаємо різницю у днях як ціле число
        return difference.days
    
    except ValueError:
        # Обробляємо помилку неправильного формату дати
        print(f"Помилка: неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
        return None


def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї.
    
    Параметри:
    min (int): мінімальне число (не менше 1)
    max (int): максимальне число (не більше 1000) 
    quantity (int): кількість чисел для вибору
    
    Повертає:
    list: відсортований список унікальних чисел або пустий список
    """
    # Крок 1: Перевіряємо коректність параметрів
    if min < 1:
        return []
    if max > 1000:
        return []
    if min > max:
        return []
    if quantity < 1:
        return []
    if quantity > (max - min + 1):
        return []
    
    # Крок 2: Створюємо множину для унікальних чисел
    unique_numbers = set()
    
    # Крок 3: Генеруємо випадкові числа поки не наберемо потрібну кількість
    while len(unique_numbers) < quantity:
        random_number = random.randint(min, max)
        unique_numbers.add(random_number)
    
    # Крок 4: Перетворюємо множину у список і сортуємо
    result_list = list(unique_numbers)
    result_list.sort()
    
    return result_list


def normalize_phone(phone_number):
    """
    Нормалізує телефонні номери до стандартного формату.
    
    Параметр:
    phone_number (str): телефонний номер у будь-якому форматі
    
    Повертає:
    str: нормалізований номер у форматі +380XXXXXXXXX
    """
    # Крок 1: Видаляємо всі символи крім цифр та '+'
    clean_number = ""
    for char in phone_number:
        if char.isdigit() or char == '+':
            clean_number += char
    
    # Альтернативний спосіб через регулярні вирази (як у рекомендаціях)
    # clean_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Крок 2: Перевіряємо чи номер починається з '+' і виправляємо префікс
    
    # Якщо номер вже має правильний формат +380
    if clean_number.startswith('+380'):
        return clean_number
    
    # Якщо номер починається з 380, додаємо тільки '+'
    elif clean_number.startswith('380'):
        return '+' + clean_number
    
    # Якщо номер починається з 0 (місцевий український номер)
    elif clean_number.startswith('0'):
        return '+38' + clean_number
    
    # У всіх інших випадках додаємо '+38'
    else:
        return '+38' + clean_number


# Тестування функцій
if __name__ == "__main__":
    
    print("=== Тестування get_days_from_today ===")
    # Вибираємо різні дати для тестування функції
    # Дата в минулому - повинна дати позитивне число
    print(f"Дні від 2020-10-09: {get_days_from_today('2020-10-09')}")
    # Дата в недалекому минулому 
    print(f"Дні від 2024-12-25: {get_days_from_today('2024-12-25')}")
    # Дата в майбутньому - повинна дати від'ємне число
    print(f"Дні від 2026-01-01: {get_days_from_today('2026-01-01')}")
    
    # Тестуємо обробку помилок - вводимо дату в неправильному форматі
    print("Тест неправильного формату:")
    get_days_from_today('25.07.2024')
    
    print("\n=== Тестування get_numbers_ticket ===")
    # Тестуємо класичну лотерею: вибираємо 6 чисел від 1 до 49
    # Цей код викликає функцію з параметрами min=1, max=49, quantity=6
    print("Лотерея 6 з 49:", get_numbers_ticket(1, 49, 6))
    
    # Тестуємо іншу популярну лотерею: 5 чисел від 1 до 36
    # Параметри: min=1, max=36, quantity=5
    print("Лотерея 5 з 36:", get_numbers_ticket(1, 36, 5)) 
    
    # Тестуємо малу лотерею: 3 числа від 1 до 10
    # В результаті отримаємо список з 3 унікальними відсортованими числами
    print("Мала лотерея 3 з 10:", get_numbers_ticket(1, 10, 3))
    
    # Тестуємо некоректні параметри - функція повинна повернути пустий список
    print("Помилка - забагато чисел (quantity > можливих):", get_numbers_ticket(1, 5, 10))
    print("Помилка - min менше 1:", get_numbers_ticket(0, 10, 3))
    print("Помилка - max більше 1000:", get_numbers_ticket(1, 1500, 5))
    
    print("\n=== Тестування normalize_phone ===")
    # Вибираємо різні формати номерів для демонстрації роботи функції
    # Кожен номер показує окремий випадок нормалізації
    raw_numbers = [
        "067 123 45 67",      # номер з пробілами, починається з 0
        "(050) 987-65-43",    # номер з дужками та тире
        "+380 44 555 66 77",  # номер з правильним префіксом +380
        "380671234567",       # номер з префіксом 380 без +
        "0503334455",         # номер без пробілів, починається з 0
        "38050-777-88-99"     # номер з префіксом 38 та тире
    ]
    
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)








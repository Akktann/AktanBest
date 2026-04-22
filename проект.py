import re
import sys

def get_password_strength(password):
    """
    Анализирует пароль и возвращает словарь с результатами проверок.
    Чистота кода: четкое разделение логики и вывода.
    """
    checks = {
        "Длина (8+ символов)": len(password) >= 8,
        "Наличие цифр": bool(re.search(r"\d", password)),
        "Заглавные буквы (A-Z)": bool(re.search(r"[A-Z]", password)),
        "Строчные буквы (a-z)": bool(re.search(r"[a-z]", password)),
        "Спецсимволы (@#$%^&*)": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    score = sum(checks.values())
    return checks, score

def print_ui_box(text, width=40):
    """Красивый вывод (Улучшение 6)"""
    print(f"\n╔{'═' * (width-2)}╗")
    print(f"║ {text.center(width-4)} ║")
    print(f"╚{'═' * (width-2)}╝")

def main():
    print_ui_box("АНАЛИЗАТОР СЛОЖНОСТИ ПАРОЛЯ")

    while True:
        try:
            print("\nВведите пароль для проверки (или 'exit' для выхода):")
            user_input = input(">> ").strip()
            
            if not user_input:
                print("⚠️ Ошибка: Пароль не может быть пустым.")
                continue
                
            if user_input.lower() == 'exit':
                print("До свидания! 👋")
                break

            results, score = get_password_strength(user_input)
            
            
            print("\nРезультаты проверки:")
            for desc, passed in results.items():
                status = "✅" if passed else "❌"
                print(f"  {status} {desc}")
            
            print("-" * 30)
            if score == 5:
                print("ИТОГ: 🔥 Мощный пароль!")
            elif score >= 3:
                print("ИТОГ: ⚠️ Средний пароль. Можно улучшить.")
            else:
                print("ИТОГ: ❌ Слабый пароль. Небезопасно!")
            print("-" * 30)

        except KeyboardInterrupt:
           
            print("\n\nПрограмма завершена принудительно.")
            sys.exit()
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()

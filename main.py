easy = {"mother": "мама", "father": "папа", "aunt": "тетя", "uncle": "дядя", "cousin": "кузен"}
medium = {"good": "хорошо", "bad": "плохо", "fine": "нормально", "great": "великолепно", "excellent": "отлично"}
hard = {"table": "стол", "chair": "стул", "wall": "стена", "ceiling": "потолок", "floor": "пол"}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}

print("Выберите уровень сложности")
print("легкий, средний, сложный")

user_input = input().lower()

if user_input == "легкий":
    words = easy
elif user_input == "средний":
    words = medium
elif user_input == "сложный":
    words = hard

print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод")

for en, ru in words.items():
    print("Нажмите Enter")
    input()
    letter_count = len(ru)
    first_letter = ru[0]
    print(f"{en}, {letter_count} букв, начинается на {first_letter}")

    user_answer = input()

    if user_answer == ru:
        print(f"Верно, {en} это {ru}")
        answers[en] = True
    else:
        print(f"Неверно, {en} это {ru}")
        answers[en] = False

print()
print("Правильно отвеченные слова:")

correct_answer = 0

for en, is_correct in answers.items():
    if is_correct:
        correct_answer += 1
        print(en)

print()
print("Неправильно отвеченные слова:")

for en, is_correct in answers.items():
    if not is_correct:
        print(en)

print()
print("Ваш ранг:")
print(levels[correct_answer])

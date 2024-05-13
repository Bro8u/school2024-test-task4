import collections
import datetime

def is_valid_commit_line(line):
    """
    Проверяет валидность строки коммита.
    """
    parts = line.strip().split()

    if len(parts) != 3:
        return False
    username, commit_hash, commit_date = parts

    # Проверяем, что username начинается с буквы и содержит только буквы, цифры и символ '_'
    if not username.isidentifier():
        return False

    # Проверяем, что commit_hash состоит из 7 символов и содержит только буквы и цифры
    if not commit_hash.isalnum() or len(commit_hash) != 7:
        return False

    # Проверяем, что commit_date имеет правильный формат "YYYY-MM-ddTHH:mm:ss.f"
    try:
        datetime.datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return False

    return True


def get_top_contributors(input_file='commits.txt', output_file='result.txt'):
    """
    Формирует отчет о топ-3 контрибьютерах на основе данных о коммитах.
    """
    try:
        # Чтение данных из файла
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Подсчет количества коммитов для каждого пользователя
        commit_counts = collections.Counter()
        for line in lines:
            if is_valid_commit_line(line):
                username = line.split()[0]
                commit_counts[username] += 1
            else:
                raise ValueError("There is an invalid commit line")

        # Выбор топ-3 контрибьютеров
        top_contributors = [user for user, count in commit_counts.most_common(3)]

        # Запись результата в файл
        with open(output_file, 'w') as file:
            for contributor in top_contributors:
                file.write(f"{contributor}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_top_contributors()

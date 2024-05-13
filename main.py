import collections
import datetime
import logging
from typing import List, Counter

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_commit_line(line: str) -> bool:
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
    if not (commit_hash.isalnum() and len(commit_hash) == 7 and commit_hash.islower()):
        return False

    # Проверяем, что commit_date имеет правильный формат "YYYY-MM-ddTHH:mm:ss"
    try:
        datetime.datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return False

    return True

def read_commit_file(input_file: str) -> List[str]:
    """
    Читает данные из файла с коммитами.
    """
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        logging.info(f"Successfully read {len(lines)} lines from {input_file}")
        return lines
    except FileNotFoundError:
        logging.error(f"Input file {input_file} not found")
        return []

def count_commits(lines: List[str]) -> Counter[str]:
    """
    Подсчитывает количество коммитов для каждого пользователя.
    """
    commit_counts = collections.Counter()
    for line in lines:
        if is_valid_commit_line(line):
            username = line.split()[0]
            commit_counts[username] += 1
        else:
            logging.warning(f"Invalid commit line: {line.strip()}")
    logging.info(f"Counted commits for {len(commit_counts)} users")
    return commit_counts

def get_top_contributors(commit_counts: Counter[str], top_n: int = 3) -> List[str]:
    """
    Возвращает список топ-3 контрибьютеров.
    """
    top_contributors = [user for user, count in commit_counts.most_common(top_n)]
    logging.info(f"Top {top_n} contributors: {top_contributors}")
    return top_contributors

def write_top_contributors(output_file: str, top_contributors: List[str]) -> None:
    """
    Записывает топ-3 контрибьютеров в файл.
    """
    try:
        with open(output_file, 'w') as file:
            for contributor in top_contributors:
                file.write(f"{contributor}\n")
        logging.info(f"Top contributors written to {output_file}")
    except Exception as e:
        logging.error(f"An error occurred while writing to file: {e}")

def main(input_file: str = 'commits.txt', output_file: str = 'result.txt') -> None:
    """
    Основная функция для формирования топ-3 контрибьютера.
    """
    lines = read_commit_file(input_file)
    if not lines:
        return

    commit_counts = count_commits(lines)
    if not commit_counts:
        logging.error("No valid commit lines found")
        return

    top_contributors = get_top_contributors(commit_counts)
    write_top_contributors(output_file, top_contributors)

if __name__ == "__main__":
    main()

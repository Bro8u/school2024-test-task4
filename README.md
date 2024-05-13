# Тестовое задание для отбора на Летнюю ИТ-школу КРОК по разработке

## Условие задания
Будучи тимлидом команды разработки, вы получили от менеджера проекта задачу повысить скорость разработки. Звучит, как начало плохого анекдота, но, тем не менее, решение вам все же нужно найти. В ходе размышлений и изучений различного внешнего опыта других команд разработки вы решили попробовать инструменты геймификации. То есть применить техники и подходы игрового характера с целью повышения вовлеченности команды в решение задач.

Вами была придумана рейтинговая таблица самых активных контрибьютеров за спринт. Что это значит в теории: по окончании итерации (4 рабочие недели) выгружается список коммитов, сделанных в релизную ветку продукта, и на его основе вычисляются трое самых активных разработчиков, сделавших наибольшее количество коммитов. В зависимости от занятого места, разработчик получает определенное количество внутренней валюты вашей компании, которую он впоследствии может обменять на какие-то товары из внутреннего магазина.

На практике вы видите решение следующим образом: на следующий день после окончания спринта в 00:00 запускается автоматическая процедура, которая забирает файл с данными о коммитах в релизную ветку, сделанных в период спринта, после чего выполняется поиск 3-х самых активных контрибьютеров. Имена найденных разработчиков записываются в файл, который впоследствии отправляется вам на почту.

В рамках практической реализации данной задачи вам необходимо разработать процедуру формирование отчета “Топ-3 контрибьютера”. Данная процедура принимает на вход текстовый файл (commits.txt), содержащий данные о коммитах (построчно). Каждая строка содержит сведения о коммите в релизную ветку в формате: “_<Имя пользователя> <Сокращенный хэш коммита> <Дата и время коммита>_”.
Например: AIvanov 25ec001 2024-04-24T13:56:39.492

К данным предъявляются следующие требования:
- имя пользователя может содержать латинские символы в любом регистре, цифры (но не начинаться с них), а также символ "_";
- сокращенный хэш коммита представляет из себя строку в нижнем регистре, состояющую из 7 символов: букв латинского алфавита, а также цифр;
- дата и время коммита в формате YYYY-MM-ddTHH:mm:ss.

В результате работы процедура формирует новый файл (result.txt), содержащий информацию об именах 3-х самых активных пользователей по одному в каждой строке в порядке убывания места в рейтинге. Пример содержимого файла:
AIvanov
AKalinina
CodeKiller777

Ручной ввод пути к файлу (через консоль, через правку переменной в коде и т.д.) недопустим. Необходимость любых ручных действий с файлами в процессе работы программы будут обнулять решение.

## Автор решения
    Якунин Борис Николаевич

## Описание реализации
    Входные данные:
        Текстовый файл commits.txt, содержащий данные о коммитах. Каждая строка файла представляет собой информацию о коммите в следующем формате: <Имя пользователя> <Сокращенный хэш коммита> <Дата и время коммита>.
    
    Требования к данным:
        1.Имя пользователя может содержать латинские символы в любом регистре, цифры (но не начинаться с них), а также символ "_".
        2.Сокращенный хэш коммита представляет из себя строку в нижнем регистре, состоящую из 7 символов: букв латинского алфавита и цифр.
        3.Дата и время коммита должны быть в формате YYYY-MM-ddTHH:mm:ss.

    Цель:
        Процедура формирует новый файл (result.txt), содержащий информацию об именах 3-х самых активных пользователей по одному в каждой строке в порядке убывания места в рейтинге

    Описание реализации требований задачи:
        is_valid_commit_line(line: str) -> bool:
            Описание: Проверяет валидность строки коммита в соответствии с требованиями к данным.
            Возвращаемый тип: bool
            Логирование: Логирование не требуется, так как функция только проверяет строку и возвращает результат.
        read_commit_file(input_file: str) -> List[str]:
            Описание: Читает данные из указанного файла и возвращает список строк.
            Возвращаемый тип: List[str]
            Логирование:
                Успешное чтение файла: logging.info(f"Successfully read {len(lines)} lines from {input_file}")
                Ошибка при открытии файла: logging.error(f"Input file {input_file} not found")
        count_commits(lines: List[str]) -> Counter[str]:
            Описание: Подсчитывает количество коммитов для каждого пользователя, проверяя валидность каждой строки.
            Возвращаемый тип: Counter[str]
            Логирование:
                Невалидная строка: logging.warning(f"Invalid commit line: {line.strip()}")
                Количество пользователей с коммитами: logging.info(f"Counted commits for {len(commit_counts)} users")
        get_top_contributors(commit_counts: Counter[str], top_n: int = 3) -> List[str]:
            Описание: Возвращает список топ-3 контрибьютеров на основе количества коммитов.
            Возвращаемый тип: List[str]
            Логирование:
                Информация о топ-3 контрибьюторах: logging.info(f"Top {top_n} contributors: {top_contributors}")
        write_top_contributors(output_file: str, top_contributors: List[str]) -> None:
            Описание: Записывает список топ-3 контрибьютеров в указанный файл.
            Возвращаемый тип: None
            Логирование:
                Успешная запись: logging.info(f"Top contributors written to {output_file}")
                Ошибка при записи: logging.error(f"An error occurred while writing to file: {e}")
        main(input_file: str = 'commits.txt', output_file: str = 'result.txt') -> None:
            Описание: Выполняет весь процесс: чтение файла, подсчет коммитов, выбор топ-3 контрибьютеров и запись результата в файл.
            Возвращаемый тип: None
            Логирование:
                Ошибка при отсутствии валидных коммитов: logging.error("No valid commit lines found")

## Инструкция по сборке и запуску решения
    Установка всех зависимостей и библиотек:
        Обновите python до последней версии или установите последнюю версию python:
            https://www.python.org/downloads/
        Установите git, если не установлен:
            https://git-scm.com/
    Сборка и запуск:
        1.Откройте терминал, перейдите в любую удобную директорию: cd
        2.Скопируйте репозиторий c помощью команды: git clone "https://github.com/Bro8u/school2024-test-task4.git"
        3.Добавьте в текущую директорию текстовый файл commits.txt
        3.Запустите решение командой: python3 main.py
        4.Результат будет в текущей директории в файле result.txt
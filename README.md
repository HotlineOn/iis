# Описание проекта
Проект посвящен решеню задачи предсказания зарплаты дата сайентиста
Ссылка на исходную выборку данных: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023?resource=download

# Установка
Для запуска проекта необходимо выполнить команды:
```
git clone https://github.com/HotlineOn/iis.git
cd iis
установка окружения
активация окружения
установка зависимостей
```

# Датесет
*Data Science Job Salaries Dataset* содержит 11 столбцов:
1. work_year: Год когда была выплачена зарплата.
2. experience_level: Уровень опыта работы в течение года.
3. employment_type: Тип найма для должности.
4. job_title: Должность в течение года.
5. salary: Сумма выплаченных зарплат за год.
6. salary_currency: Валюта, в которой выплачена зарплата, как ISO 4217 код валюты.
7. salaryinusd: Сумма выплаченных зарплат за год в долларах.
8. employee_residence: Основное место жительства работника в течение года, как ISO 3166 код страны.
9. remote_ratio: Количество рабочего времени удалённой работы
10. company_location: Страна, в которой находится главный офис работадателя или филиал, где работает реципиент
11. company_size: Медианное количество людей, работавших в компании в течение года
* experience_level, employment_type, job_title, salary_currency, employee_residence, company_location, company_size 
переведены в категориальный тип
* work_year переведён uint16
* salary и salary_in_usd переведены в uint32
* remote_ratio переведён в uint8 \
В результате по сравнению с типами по умолчанию датасет занимает
100 КБ вместо 300 КБ


# Исследование данных

Находится в `./eda/eda.ipynb`. Основные результаты:

В ходе исследования были проведены действия:
* Удалены страны в столбце company_location, которые представлены 1 раз

Обработанная выборка сохранена в файл `./data/dataet.pkl`


# Настройка и обучение модели
На настройки модели используется MLFlow...

Для запуска выполнить....
```
Скрипты

```
Исследования находятся в файле `...ipynb`

Лучшая модель показывает такой-то результат, получена в 
`run_id = .....` 

# Создание сервисов
...



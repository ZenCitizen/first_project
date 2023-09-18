#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info">
# Привет! Меня зовут Светлана Чих и я буду проверять твой проект. Моя основная цель — не указать на совершенные тобою ошибки, а поделиться своим опытом и помочь тебе. Предлагаю общаться на «ты». Но если это не удобно - дай знать, и мы перейдем на «вы».
# 
# <div class="alert alert-success">
# <b>👍 Успех:</b> Зелёным цветом отмечены удачные и элегантные решения, на которые можно опираться в будущих проектах.
# </div>
# <div class="alert alert-warning">
# <b>🤔 Рекомендация:</b> Жёлтым цветом выделено то, что в следующий раз можно сделать по-другому. Ты можешь учесть эти комментарии при выполнении будущих заданий или доработать проект сейчас (однако это не обязательно).
# </div>
# <div class="alert alert-danger">
# <b>😔 Необходимо исправить:</b> Красным цветом выделены комментарии, без исправления которых, я не смогу принять проект :(
# </div>
# <div class="alert alert-info">
# <b>👂 Совет:</b> Какие-то дополнительные материалы
# </div>
# Давай работать над проектом в диалоге: если ты что-то меняешь в проекте по моим рекомендациям — пиши об этом.
# Мне будет легче отследить изменения, если ты выделишь свои комментарии:
# <div class="alert alert-info"> <b>🎓 Комментарий студента:</b> Например, вот так.</div>
# Пожалуйста, не перемещай, не изменяй и не удаляй мои комментарии. Всё это поможет выполнить повторную проверку твоего проекта быстрее.
#  </div>

# В этой части проекта вам нужно написать несколько SQL-запросов в Jupyter Notebook. Эти задания проверят вручную, и вы получите комментарии к составленным запросам. 
# 
# Необходимые данные находятся в таблицах схемы `stackoverflow`. Не забудьте подключиться к базе с помощью SQLAlchemy. Вспомните инструкцию из [урока про представление результатов](https://practicum.yandex.ru/learn/data-analyst-plus/courses/96ccbf7a-b65d-4f51-b5f3-18360ad1e301/sprints/6116/topics/27f7c9a7-a474-4a82-8392-b3f069b26f69/lessons/e12d84bb-ffa8-490c-8bde-0935d86ceccb/). Пример кода для подключения к базе и выгрузки результатов вы найдёте и в этой тетрадке. 
# 
# Некоторые задания включают дополнительные вопросы — не пропустите их. На часть вопросов можно ответить текстом, а для некоторых понадобится визуализация. Помните, что результат запроса можно выгрузить в датафрейм. 
# 
# Чтобы ожидаемый результат было легче представить, мы добавили к каждому заданию небольшой фрагмент итоговой таблицы. В запросах вы можете использовать любые подходящие названия полей.

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine 
import seaborn as sns


# ### Конфигурация для подключения к базе данных `data-analyst-advanced-sql`
# Эта база данных содержит схему `stackoverflow`, с которой вы будете работать в проекте

# In[23]:


db_config = {
    'user': 'praktikum_student', # имя пользователя
    'pwd': 'Sdf4$2;d-d30pp', # пароль
    'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
    'port': 6432, # порт подключения
    'db': 'data-analyst-advanced-sql' # название базы данных
}  

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
    db_config['user'],
    db_config['pwd'],
    db_config['host'],
    db_config['port'],
    db_config['db'],
)


# Создание подключения

# In[24]:


engine = create_engine(connection_string) 


# Пример запроса к базе данных
# 
# `sample_df` является pandas-датафреймом.

# In[25]:


query = '''
SELECT *
FROM stackoverflow.users
LIMIT 10;
'''

sample_df = pd.read_sql_query(query, con=engine) 


# In[26]:


sample_df


# <div class="alert alert-success">
# <b>👍 Успех:</b> Импортированы все нужные библиотеки, создано подключение к БД, проверена его работа на примере одной таблицы
# </div>

# # Задание 1

# Выведите общую сумму просмотров постов за каждый месяц 2008 года. Если данных за какой-либо месяц в базе нет, такой месяц можно пропустить. Результат отсортируйте по убыванию общего количества просмотров.

# | month_date  | total_views |
# | ------------- | ------------- |
# | 2008-09-01  | 452928568  |
# | 2008-10-01  | 365400138  |
# | ...         | ... |

# In[27]:


# напишите запрос
query = '''
SELECT cast(date_trunc('month', creation_date) AS date) month_date, 
	   sum(views_count) views_total
FROM stackoverflow.posts p 
WHERE EXTRACT (YEAR FROM creation_date) = '2008'
GROUP BY month_date
ORDER BY views_total DESC
'''

# выполните запрос
df_task1 = pd.read_sql_query(query, con=engine) 
df_task1


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно! Молодец, что пользуешься алиасами при группировке и сортировке, вместо  CAST(DATE_TRUNC('month', creation_date) AS date) можно использовать DATE_TRUNC('month', creation_date)::date
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Используйте функцию для усечения даты, а затем сгруппируйте и отсортируйте данные.
# </details>

# Проанализируйте итоговую таблицу. Отличаются ли данные за разные месяцы? С чем могут быть связаны отличия?

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
#     
# Для анализа были предоставлены данные за 6 месяцев 2008 года. Динамика показывает сильный прирост кол-ва просмотров в сентябре с дальнейшим снижением. Думаю эти колебания связаны с началом учебного года. Летом минимальное кол-во просмотров, а в сентябре все, кто начали учебный год по IT специальностям начинают искать материалы для решения своих задач
#         
# </div>

#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 2

# Выведите имена самых активных пользователей, которые в первый месяц после регистрации (включая день регистрации) дали больше 100 ответов. Вопросы, которые задавали пользователи, не учитывайте. Для каждого имени пользователя выведите количество уникальных значений `user_id`. Отсортируйте результат по полю с именами в лексикографическом порядке.

# | display_name | count |
# | ------------ | ----- |
# | 1800 INFORMATION | 1 |
# | Adam Bellaire | 1 |
# | Adam Davis | 1 |
# | ... | ... |

# In[28]:


# напишите запрос
query = '''
WITH raw AS 
	(SELECT u.id user_id, u.creation_date :: date, u.display_name,
		   p.id post_id, 
		   p.creation_date :: date post_dt
	FROM stackoverflow.posts p
	JOIN stackoverflow.users u ON u.id = p.user_id
	WHERE post_type_id IN (SELECT id 
							FROM stackoverflow.post_types 
							WHERE TYPE = 'Answer')
	AND p.creation_date BETWEEN u.creation_date AND u.creation_date + INTERVAL '30 days')
SELECT display_name, count(DISTINCT user_id) 
FROM raw
GROUP BY display_name
HAVING count(post_id) > 100
ORDER BY display_name

'''

# выполните запрос
df_task2 = pd.read_sql_query(query, con=engine) 
df_task2


#  <div class="alert alert-danger">
# <s> <b>😔 Необходимо исправить:</b> В разных месяцах разное количество дней, в октябре - 31, лучше использовать INTERVAL '1 month', и можно упростить запрос, не используя временные таблицы, а просто объединив сразу 3 и выбирая из них данные</s>
#  </div>

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
#     
# Принято, заменила интервал на календарный месяц, и убрала одну лишнюю конструкцию с временной таблицей))) 
# Спасибо за комментарий!
# </div>

# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Вам нужно присоединить несколько таблиц — изучите внимательнее описание базы. Чтобы добавить промежуток времени к дате, используйте ключевое слово INTERVAL, например, так: <дата> + INTERVAL '1 year 2 months 3 days'
# .</details>

# Какие аномалии наблюдаются в данных? О чём они говорят?

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
#     
# Скрипт выдал всего 74 уникальных display_name. 
# Судя по полученным данным при указании display_name нет никаких стандартов введения данных, где то юзеры указывают полные имена, где то только имя, где то просто набор букв и цифр. Так же display_name могут повторяться у нескольких юзеров.         
# </div>

#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 3

# Выведите количество постов за 2008 год по месяцам. Отберите посты от пользователей, которые зарегистрировались в сентябре 2008 года и сделали хотя бы один пост в декабре того же года. Отсортируйте таблицу по значению месяца по убыванию.

# | month | count |
# | ------|------ |
# | 2008-12-01 | 17641 |
# | 2008-11-01 | 18294 |
# | ... | ... |

# In[29]:


# напишите запрос
query = '''
-- users who registered 09/2008						
WITH users as
	(SELECT id user_id, creation_date :: date
	FROM stackoverflow.users
	WHERE DATE_TRUNC('month', creation_date) = '2008-09-01'),
-- users who had posts at 12/2008	
users_list AS 	
	(SELECT DISTINCT u.user_id
	FROM users u
	JOIN stackoverflow.posts p ON u.user_id = p.user_id 
	WHERE DATE_TRUNC('month', p.creation_date) = '2008-12-01')
-- count of posts by users_list
SELECT cast(date_trunc('month', p.creation_date) AS date) month_date, count(p.id)
FROM users_list u
JOIN stackoverflow.posts p ON u.user_id = p.user_id 
GROUP BY month_date
ORDER BY month_date DESC 
'''

# выполните запрос
df_task3 = pd.read_sql_query(query, con=engine) 
df_task3


# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Сначала найдите идентификаторы пользователей, которые зарегистрировались в сентябре 2008 года и оставили хотя бы один пост в декабре. Затем используйте результат для среза и посчитайте посты по месяцам.</details>

# Изучите данные: есть ли в них аномалии? Предположите, почему могли появиться аномальные значения.

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
# 
# По ТЗ мы выгружали юзеров, зарегистрировавшихся в базе в сентябре 2008 года, но по выгрузке получается что у них были посты уже в августе. Я не знакома с процедурой регистрации в stackoverflow, но предполагаю, что людям присваивается user_id при любом интерактиве с сайтом, а регистрация считается завершенной при заполнении рег данных. И изначально присвоенный user_id может сохраниться при регистрации.     
# </div>

# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 4

# Используя данные о постах, выведите несколько полей:
# 
# - идентификатор пользователя, который написал пост;
# - дата создания поста;
# - количество просмотров у текущего поста;
# - сумму просмотров постов автора с накоплением.
# 
# Данные в таблице должны быть отсортированы по возрастанию идентификаторов пользователей, а данные об одном и том же пользователе — по возрастанию даты создания поста.

# | user_id | creation_date | views_count | cumulative_count |
# | ------ | -------------- | ----------- | ---------------- |
# | 1 | 2008-07-31 23:41:00  | 480476   | 480476  |
# | 1 | 2008-07-31 23:55:38  | 136033 | 616509  | 
# | 1 | 2008-07-31 23:56:41  | 0 |  616509  |
# | ... | ... | ... | ... |
# | 2 | 2008-07-31 23:56:41 | 79087  | 79087 |
# | 2 | 2008-08-01 05:09:56 | 65443 | 144530 |
# | ... | ...  | ...  | ...  |

# In[30]:


# напишите запрос
query = '''
SELECT user_id, creation_date, views_count, 
	   sum(views_count) OVER (PARTITION BY user_id ORDER BY creation_date) cumulative_count
FROM stackoverflow.posts
ORDER BY user_id, creation_date
'''

# выполните запрос
df_task4 = pd.read_sql_query(query, con=engine) 
df_task4


# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно! С оконной функцией все отлично получается!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Для подсчёта суммы с накоплением используйте оконную функцию.
# </details>

# # Задание 5

# Найдите среднее количество постов пользователей в день за август 2008 года. Отберите данные о пользователях, которые опубликовали больше 120 постов за август. Дни без публикаций не учитывайте. 
# 
# Отсортируйте результат по возрастанию среднего количества постов. Значения можно не округлять.

# | user_id | avg_daily |
# | ------- | --------- |
# | 116     | 4.777778  |
# | 234     | 5.208333  |
# | ...     | ... |

# In[31]:


# напишите запрос
query = '''
WITH raw AS 
	(SELECT user_id, creation_date :: date, count(id) daily_count
	FROM stackoverflow.posts p 
	WHERE user_id IN (SELECT user_id
		FROM stackoverflow.posts
		WHERE DATE_TRUNC('month', creation_date) = '2008-08-01'
		GROUP BY user_id
		HAVING count(id) > 120)
	AND DATE_TRUNC('month', creation_date) = '2008-08-01'
	GROUP BY 1, 2)
SELECT user_id, avg(daily_count) avg_daily
FROM raw
GROUP BY user_id
ORDER BY avg_daily
'''

# выполните запрос
df_task5 = pd.read_sql_query(query, con=engine) 
df_task5


# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Сначала найдите идентификаторы пользователей, которые написали более 120 постов за август. Используя этот запрос в качестве подзапроса для среза, найдите и сохраните во временную таблицу идентификаторы нужных пользователей, дни августа и количество постов в день. В основном запросе сгруппируйте данные по пользователям и найдите для каждого из них среднее количество постов.
# </details>

# # Задание 6

# Сколько в среднем дней в период с 1 по 7 декабря 2008 года пользователи взаимодействовали с платформой? Для каждого пользователя отберите дни, в которые он или она опубликовали хотя бы один пост. Нужно получить одно целое число — не забудьте округлить результат. 

# | result |
# | -----  |
# | <целое число> |

# In[32]:


# напишите запрос
query = '''
SELECT round(avg(days))
FROM (WITH raw AS
		(SELECT DISTINCT user_id, creation_date :: date AS dt
		FROM stackoverflow.posts p 
		WHERE creation_date :: date BETWEEN to_date('01122008', 'ddmmyyyy') AND to_date('07122008', 'ddmmyyyy'))
	SELECT user_id, count(dt) days
	FROM raw
	GROUP BY user_id) x
'''

# выполните запрос
df_task6 = pd.read_sql_query(query, con=engine) 
df_task6


# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Посчитайте, сколько активных дней было у каждого пользователя. Добавьте данные во временную таблицу и используйте в основном запросе.
# </details>

# Проанализируйте итоговую таблицу — какие выводы можно сделать?

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
# 
# В среднем пользователи взаимодействовали 2 дня из 7 в указанном периоде. Учитывая что это не период пиковой активности для сайта (судя по данным, пользователи больше всего взаимодействуют с сайтом в сентябре) думаю неплохой показатель.
# </div>

# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 7

# Выведите историю активности каждого пользователя в таком виде: идентификатор пользователя, дата публикации поста. Отсортируйте вывод по возрастанию идентификаторов пользователей, а для каждого пользователя — по возрастанию даты публикации.
# 
# Добавьте в таблицу новое поле: для каждого поста в нём будет указано название месяца предпоследней публикации пользователя относительно текущей. Если такой публикации нет, укажите `NULL`.  Python автоматически поменяет `NULL` на `None`, но дополнительно преобразовывать значения `None` вам не нужно.
# 
# Посмотрите внимательно на образец таблицы: для первых двух постов предпоследней публикации нет, но, начиная с третьего поста, в новое поле входит нужный месяц. Для следующего пользователя в первые две записи поля `second_last_month` тоже войдёт `NULL`.

# | user_id | creation_date | second_last_month |
# | ------- | ------------- | ----------------- |
# | 1       | 2008-07-31 23:41:00 | None |
# | 1       | 2008-07-31 23:55:38 | None |
# | 1       | 2008-07-31 23:56:41 | July |
# | 1       | 2008-08-04 02:45:08 | July |
# | 1       | 2008-08-04 04:31:03 | July |
# | 1       | 2008-08-04 08:04:42 | August |
# | ... | ... | ... |

# In[33]:


# напишите запрос
query = '''
SELECT user_id, creation_date post_dt,
	   to_char(lag(creation_date, 2, NULL) OVER (PARTITION BY user_id ORDER BY creation_date), 'Month') second_last_month
FROM stackoverflow.posts p 
ORDER BY user_id
'''

# выполните запрос
df_task7 = pd.read_sql_query(query, con=engine) 
df_task7


#  <div class="alert alert-danger">
# <s> <b>😔 Необходимо исправить:</b> А зачем здесь временная таблица? Хорошая идея использовать to_char, но сделай одним запросом</s>
#  </div>

# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
# 
# В первый раз такая же конструкция не сработала, и я подумала что оконную функцию нельзя обернуть в to_char, но видимо была какая то синтаксическая ошибка. Исправила, убрала лишнюю конструкцию))) Спасибо за комментарии! 
# </div>

# <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно! Внимательно читай ошибки, иногда бывают лишние символы или путаница со скобками
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Преобразовать результат оконной функции в нужное значение вам поможет аналог условного оператора в SQL: CASE <поле> WHEN <старое значение> THEN <новое значение> END.
# </details>

# # Задание 8

# Рассчитайте аналог Retention Rate по месяцам для пользователей StackOverflow. Объедините пользователей в когорты по месяцу их первого поста. Возвращение определяйте по наличию поста в текущем месяце. 

# | cohort_dt | session_date | users_cnt | cohort_users_cnt | retention_rate |
# | --- | --- | --- | --- | --- |
# | 2008-07-01 00:00:00 | 2008-07-01 00:00:00 | 3 | 3 | 100 |
# | 2008-07-01 00:00:00 | 2008-08-01 00:00:00 | 2 | 3 | 66,67 |
# | 2008-07-01 00:00:00 | 2008-09-01 00:00:00 | 1 | 3 | 33,33 |
# | 2008-07-01 00:00:00 | 2008-10-01 00:00:00 | 2 | 3 | 66,67 |
# | 2008-07-01 00:00:00 | 2008-11-01 00:00:00 | 1 | 3 | 33,33 |
# | 2008-07-01 00:00:00 | 2008-12-01 00:00:00 | 2 | 3 | 66,67 |
# | 2008-08-01 00:00:00 | 2008-08-01 00:00:00 | 2151 | 2151 | 100 |
# | ... | ... | ... | ... | ... |

# In[34]:


# напишите запрос
query = '''
WITH cohorts as
	(SELECT x.*, count(user_id) OVER (PARTITION BY cohort_dt) cohort_users_cnt
	FROM (SELECT DISTINCT user_id, 
		   		 CAST(date_trunc('month', min(creation_date) OVER (PARTITION BY user_id ORDER BY creation_date)) AS date) cohort_dt
		  FROM stackoverflow.posts) x),
sessions as
	(SELECT user_id, cast(date_trunc('month', creation_date) AS date) session_dt
	FROM stackoverflow.posts 
	GROUP BY 1, 2)
SELECT c.cohort_dt, 
	   s.session_dt, 
	   count(c.user_id) users_cnt,
	   cohort_users_cnt, 
	   round(count(c.user_id) * 100.0 / cohort_users_cnt, 2) retention_rate 
FROM cohorts c
JOIN sessions s ON c.user_id = s.user_id
GROUP BY 1, 2, 4
'''

# выполните запрос
df_task8 = pd.read_sql_query(query, con=engine) 
df_task8


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Вспомните, как выглядел запрос для расчёта Retention Rate в теории. Создайте две временные таблицы: `profile` и `sessions` (в ней будет информация о публикациях), а затем используйте их в основном запросе.
# 
# Во временной таблице `profile` вам понадобятся три поля:
# 
# - идентификатор пользователя;
# - дата первого поста пользователя, усечённая до месяца (признак начала когорты);
# - количество пользователей этой когорты.
# </details>

# Постройте тепловую карту Retention Rate. Какие аномалии или другие необычные явления удалось выявить? Сформулируйте гипотезы о возможных причинах.

# In[35]:


# постройте тепловую карту Retention Rate
# создаём сводную таблицу с результатами
retention = df_task8.pivot('cohort_dt', 'session_dt', 'retention_rate')
retention.index = [str(x)[0:10] for x in retention.index]
retention.columns = [str(x)[0:10] for x in retention.columns]

# строим хитмэп
plt.figure(figsize=(10, 10)) # задаём размер графика
sns.heatmap(retention, # датафрейм с данными
            annot=True, # добавляем подписи
            fmt='') # задаём исходный формат
plt.title('Тепловая карта') # название графика
plt.show()


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# In[36]:


# опишите аномалии или другие необычные явления и сформулируйте гипотезы


# <div class="alert alert-block alert-info"><b> Комментарий студента</b> 
# 
# По хитмэпу активность июльских пользователей может показаться аномальной, но т.к. в июле у нас была небольшая выборка пользователей, эти отклонения можно не учитывать ввиду нерепрезентативности базы. 
#  
# По остальным данным видно снижение коэффициента удержания на второй месяц с августа по ноябрь, с 73% до 40% соотвественно. 
# </div>

#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 9
# 

# На сколько процентов менялось количество постов ежемесячно с 1 сентября по 31 декабря 2008 года? Отобразите таблицу со следующими полями:
# 
# - номер месяца;
# - количество постов за месяц;
# - процент, который показывает, насколько изменилось количество постов в текущем месяце по сравнению с предыдущим.
# 
# Если постов стало меньше, значение процента должно быть отрицательным, если больше — положительным. Округлите значение процента до двух знаков после запятой.
# 
# Напомним, что при делении одного целого числа на другое в PostgreSQL в результате получится целое число, округлённое до ближайшего целого вниз. Чтобы этого избежать, переведите делимое в тип `numeric`.

# | creation_month | posts_count | percentage |
# | -------------- | ----------- | ---------- |
# | 9 | 70731 | Nan |
# | 10 | 63102 | -10.33 |
# | ... | ... | ... |

# In[37]:


# напишите запрос
query = '''
SELECT month_number, posts_cnt, round((difference_perc * 100), 2) percentage
FROM 
	(WITH raw AS 
		(SELECT EXTRACT(MONTH FROM (cast(date_trunc('month', creation_date) AS date))) month_number, count(id) posts_cnt
		FROM stackoverflow.posts
		WHERE creation_date :: date BETWEEN to_date('01092008', 'ddmmyyyy') AND to_date('31122008', 'ddmmyyyy')
		GROUP BY 1
		ORDER BY 1)
	SELECT *, lag(posts_cnt) OVER (ORDER BY month_number),
		   (posts_cnt - lag(posts_cnt) OVER (ORDER BY month_number)) difference,
		   (posts_cnt - lag(posts_cnt) OVER (ORDER BY month_number)) :: numeric / lag(posts_cnt) OVER (ORDER BY month_number) difference_perc
	FROM raw) x
'''

# выполните запрос
df_task9 = pd.read_sql_query(query, con=engine) 
df_task9


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Эту задачу стоит декомпозировать. Сформируйте запрос, который отобразит номер месяца и количество постов. Затем можно использовать оконную функцию, которая вернёт значение за предыдущий месяц, и посчитать процент.
# </details>

# Постройте круговую диаграмму с количеством постов по месяцам.

# In[38]:


# постройте круговую диаграмму с количеством постов по месяцам

posts_cnt = df_task9['posts_cnt']
labels = df_task9['month_number']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# строим piechart
plt.figure(figsize=(8, 8)) # задаём размер графика
plt.title('Кол-во постов по месяцам') # название графика

plt.pie(posts_cnt, labels=labels, autopct=make_autopct(posts_cnt))
plt.show()


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# # Задание 10

# Выгрузите данные активности пользователя, который опубликовал больше всего постов за всё время. Выведите данные за октябрь 2008 года в таком виде:
# 
# - номер недели;
# - дата и время последнего поста, опубликованного на этой неделе.

# | week_creation | creation_date |
# | ------------- | ------------- |
# | 40 | 2008-10-05 09:00:58 |
# | 41 | 2008-10-12 21:22:23 |
# | ... | ... |

# In[39]:


# напишите запрос
query = '''
SELECT DISTINCT date_part('week', creation_date) week_num,
	   max(creation_date) OVER (PARTITION BY date_part('week', creation_date))
FROM stackoverflow.posts 
WHERE date_trunc('month', creation_date) = '2008-10-01' 
AND user_id IN (SELECT user_id
				FROM stackoverflow.posts
				GROUP BY user_id
				ORDER BY count(id) DESC
				LIMIT 1)

'''

# выполните запрос
df_task10 = pd.read_sql_query(query, con=engine) 
df_task10


#  <div class="alert alert-success">
#  <b>👍 Успех:</b> Все верно!
#  </div>

# <details>
# 
# <summary>Подсказка</summary>
# Декомпозируйте задачу:
# 1) Найдите пользователя, который опубликовал больше всего постов. 2) Найдите дату и время создания каждого поста этого пользователя и номер недели. 
# 3) Отобразите данные только о последних постах пользователя. Для этого можно использовать оконную функцию.
# </details>

#  <div class="alert alert-success">
#  <b>👍 Успех:</b> У тебя хорошо получается, молодец! Но старайся искать максимально простые решения и не использовать избыточных конструкций
#  </div>

# <div class="alert alert-success">
#  <b>👍 Успех:</b> Теперь все отлично, супер! У тебя очень хорошо получается. Постарайся все же оптимизировать запросы, учись понимать, сколько ресурсов может потребовать именно такое построение запроса, в реальной жизни приходится работать с разными таблицами, бывает и в триллионы строк, миллионы вообще обычное дело, и на таких объемах лишняя временная таблица или несколько проходов вместо одного могут быть критичными и требовать болше ресурсов, чем при оптимизации запроса. На это так же обращают внимание на собеседованиях, важно не просто получить верный результат, а получить его оптимально. Мы здесь как раз для того, что бы помочь тебе в этом разобраться))) И можешь посмотреть дополнительно материалы и потренироваться по SQL  <a href='https://sql-ex.ru'> тыц</a>, <a href='https://pgexercises.com'> тыц</a>, <a href='https://sql-academy.org'> тыц</a>, <a href='https://stepik.org/course/63054/info'> тыц</a>, <a href='https://Itresume.ru'> тыц</a>
#  </div>

# In[ ]:





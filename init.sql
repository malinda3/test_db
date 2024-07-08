-- Удаление существующих данных, если они есть
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS preferences;
DROP TABLE IF EXISTS goals;

-- Создание таблицы genders
CREATE TABLE genders (
    gender_id SERIAL PRIMARY KEY,
    gender VARCHAR(32) UNIQUE
);

-- Создание таблицы cities
CREATE TABLE cities (
    city_id SERIAL PRIMARY KEY,
    city VARCHAR(32) UNIQUE
);

-- Создание таблицы preferences
CREATE TABLE preferences (
    preference_id SERIAL PRIMARY KEY,
    preference VARCHAR(32) UNIQUE
);

-- Создание таблицы goals
CREATE TABLE goals (
    goal_id SERIAL PRIMARY KEY,
    goal VARCHAR(32) UNIQUE
);

-- Создание таблицы users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(32),
    age INTEGER CHECK (age > 11),
    gender_id INTEGER REFERENCES genders(gender_id),
    city_id INTEGER REFERENCES cities(city_id),
    preference_id INTEGER REFERENCES preferences(preference_id),
    goal_id INTEGER REFERENCES goals(goal_id),
    description VARCHAR(150)
);

-- Вставка данных в таблицы genders, preferences, cities, goals
INSERT INTO genders (gender) VALUES ('male'), ('female'), ('other');
INSERT INTO preferences (preference) VALUES ('male'), ('female'), ('any');
INSERT INTO cities (city) VALUES ('New York'), ('Los Angeles'), ('Chicago');
INSERT INTO goals (goal) VALUES ('Love'), ('Friendship'), ('Dontknow');

select * from goals;
select * from genders;

-- Вставка данных в таблицу users
INSERT INTO users (name, age, gender_id, city_id, preference_id, goal_id, description) VALUES
('John Doe', 25, 1, 1, 3, 1, 'Looking for like-minded individuals to hang out with.'),
('Jane Smith', 30, 2, 2, 1, 1, 'Interested in finding a long-term partner.'),
('Alex Johnson', 28, 3, 3, 2, 2, 'Open to meeting new people and having fun.'),
('Emily Davis', 22, 2, 1, 3, 3, 'Recently moved to the city and looking to expand my social circle.'),
('Michael Brown', 35, 1, 2, 2, 2, 'Ready to settle down and start a family.'),
('Sarah Wilson', 27, 2, 3, 1, 1, 'Enjoys spontaneous adventures and meeting new people.'),
('Chris Lee', 29, 1, 1, 3, 3, 'Just here to make new friends and have a good time.'),
('Anna Taylor', 24, 2, 2, 2, 2, 'Looking for someone who shares my values and interests.'),
('David Harris', 32, 1, 3, 1, 1, 'Enjoys outdoor activities and looking for someone to join me.'),
('Laura Martinez', 26, 2, 1, 3, 1, 'Interested in meeting new people and exploring the city together.');

select * from users;

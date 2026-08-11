# SQL - More Queries

This project is a continuation of SQL fundamentals, focused on MySQL user privileges, table constraints, and multi-table queries (joins and subqueries).

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- What's the difference between INNER, LEFT and RIGHT JOIN
- How to use NOT NULL and UNIQUE constraints
- How to write a subquery
- How to use GROUP BY and aggregate functions in MySQL

## Requirements

- All scripts run on Ubuntu 20.04 LTS using MySQL 8.0
- All files end with a new line
- All SQL keywords are in uppercase
- A `README.md` file at the root of the project is mandatory

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of MySQL users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates the MySQL user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and user `user_0d_2` with SELECT only |
| `3-force_name.sql` | Creates table `force_name` with a NOT NULL `name` column |
| `4-never_empty.sql` | Creates table `id_not_null` with a default `id` value |
| `5-unique_id.sql` | Creates table `unique_id` with a unique `id` column |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Creates table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists cities with their state name using a JOIN |
| `10-genre_id_by_show.sql` | Lists shows that have at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows with genre_id, NULL if none |
| `12-no_genre.sql` | Lists shows without any genre linked |
| `13-count_shows_by_genre.sql` | Counts the number of shows linked to each genre |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their linked genres |

## Author

ALU - Higher Level Programming

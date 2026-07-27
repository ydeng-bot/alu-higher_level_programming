# SQL_introduction

## Description
This project is an introduction to SQL and relational databases using MySQL. It covers basic database and table operations, including creating and deleting databases, creating tables, and performing simple `SELECT`, `INSERT`, `UPDATE`, and `DELETE` queries.

## Requirements
- All scripts will be run on Ubuntu, using MySQL
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.)
- A `README.md` file at the root of the project folder is mandatory

## Files

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't already exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates a table `first_table` with columns `id` and `name` |
| `5-full_table.sql` | Prints the full description of the table `first_table` |
| `6-list_values.sql` | Lists all rows of the table `first_table` |
| `7-insert_value.sql` | Inserts a new row into the table `first_table` |
| `8-count_89.sql` | Counts the number of records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts multiple rows |
| `10-top_score.sql` | Lists all records of `second_table` ordered by score (descending) |
| `11-best_score.sql` | Lists records of `second_table` with `score >= 10`, ordered by score |
| `12-no_cheating.sql` | Updates Bob's score to 10 in `second_table`, using only the `name` field |
| `13-change_class.sql` | Removes all records with `score <= 5` from `second_table` |
| `14-average.sql` | Computes the average score of all records in `second_table` |
| `15-groups.sql` | Lists the number of records grouped by score, ordered by count (descending) |
| `16-no_link.sql` | Lists all records of `second_table`, excluding rows with no name value |

## Usage
Each script can be run against the MySQL server like this:

```bash
cat <filename>.sql | mysql -hlocalhost -uroot -p [database_name]
```

## Author
Your Name

-- Creates a table second_table in the database hbtn_0c_0
-- second_table description: id INT,name VARCHAR(256),score INT
-- The database name will be passed as an argument
-- If the table second_table already exists, your script should not fail
-- Your script should create these records:
-- id (1,2,3,4), name ("John","Alex","Bob","George"), score(10,3,14,8)
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14),(4, 'George', 8);

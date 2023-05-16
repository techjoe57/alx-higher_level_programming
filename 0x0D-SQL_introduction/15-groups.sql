-- List the number of records with the same score 
-- in the table second_table of the database hbtn_0c_0
-- The result displays: the score and number of records 
-- with the label number
-- Sort the number of records (descending)
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;

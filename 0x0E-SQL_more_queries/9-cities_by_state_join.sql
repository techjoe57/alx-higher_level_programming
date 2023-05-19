-- list all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
select cities.id, cities.name, states.name from cities inner join states on cities.state_id=states.id;

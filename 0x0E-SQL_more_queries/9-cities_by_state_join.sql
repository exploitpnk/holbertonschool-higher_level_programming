-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s ON c.state_id=s.id ORDER BY c.id ASC;


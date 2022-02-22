INSERT INTO users (first_name, last_name, email) VALUES ("John", "Johnson", "john@email.com");
INSERT INTO users (first_name, last_name, email) VALUES ("Bill", "Williams", "bill@email.com");
INSERT INTO users (first_name, last_name, email) VALUES ("George", "Hall", "george@email.com");

SELECT * FROM users WHERE email = "john@email.com";

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id = 3;  -- --Check when done

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name ASC;

SELECT * FROM users ORDER BY first_name DESC;

-- SELECT * FROM users




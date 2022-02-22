INSERT INTO dojos (name) VALUES ("Chicago");
INSERT INTO dojos (name) VALUES ("Bellevue");
INSERT INTO dojos (name) VALUES ("Seattle");

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;

INSERT INTO dojos (name) VALUES ("Las Vegas");
INSERT INTO dojos (name) VALUES ("Miami");
INSERT INTO dojos (name) VALUES ("Houston");

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Joe", "Johnson", 21, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Brad", "Bradley", 23, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Mark", "Jackson", 25, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Mike", "Stanley", 27, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Bill", "Henley", 29, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Steven", "Thomas", 31, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Hank", "Roberts", 33, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Tyler", "May", 35, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Tony", "Wilson", 37, 6);

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT * FROM dojos WHERE id = 9;

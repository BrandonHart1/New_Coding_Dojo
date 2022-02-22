INSERT INTO authors (name) VALUES ("Jane Austen");
INSERT INTO authors (name) VALUES ("Emily Dickinson");
INSERT INTO authors (name) VALUES ("Fyador Dostoevsky");
INSERT INTO authors (name) VALUES ("William Shakespeare");
INSERT INTO authors (name) VALUES ("Lau Tzu");

INSERT INTO books (title, number_of_pages, author_id) VALUES ("C Sharp", "345", 1);
INSERT INTO books (title, number_of_pages, author_id) VALUES ("Java", "400", 2);
INSERT INTO books (title, number_of_pages, author_id) VALUES ("Python", "425", 3);
INSERT INTO books (title, number_of_pages, author_id) VALUES ("PHP", "540", 4);
INSERT INTO books (title, number_of_pages, author_id) VALUES ("Ruby", "515", 5);

UPDATE books SET title = "C#" WHERE author_id = 1;


INSERT INTO users(first_name, last_name, email, password)
VALUES("Larry", "David", "LDav1d@gmail.com", "LDav1d@gmail.com");

INSERT INTO priorities(text, level, user_id)
VALUES
("Finish Coursera class before auto-renew!", 3, 1),
("Reach out to Ed about back-end work in Chicago", 1, 1),
("Practice recursion algos", 0, 1),
("Ask Phil about clean energy books", 1, 1),
("React Native session Saturday", 1, 1),
("Compare iOS developer salaries/job market in Boston vs NYC vs Chicago", 1, 1),
("Start Andrew Ng machine learning course", 1, 1),
("Research ML in the energy industry", 1, 1),
("Email Natalie back", 2, 1),
("Ask Andie about Savannah/ self-taught design advice", 1, 1);

INSERT INTO tags(name)
VALUES('interviews');

INSERT INTO link_types(name)
VALUES
('Jobs'),
('Contacts'),
('Articles');

INSERT INTO categories(name)
VALUES
('Technologies'),
('Specializations'),
('Industries'),
('Companies'),
('Locations');

INSERT INTO links(text, url, description, link_type_id, user_id)
VALUES
("DataAnnotation AI Trainer - Remote", "https://www.indeed.com/jobs?q=software+developer&l=Remote&vjk=86b8607f1193a1a0&advn=7831672186689475", "Embedded systems", 1, 1),
("If you’d bought Apple shares instead of iPhones, you’d now have $147,000", "https://techcrunch.com/2023/09/15/one-meeeelion-dollars-muuhahahahaha/", "Apple stock", 3, 1),
("Robotics, LLMs: Exploring Consciousness, Sentience for AI Chatbots, and Bionics", "https://hackernoon.com/robotics-llms-exploring-consciousness-sentience-for-ai-chatbots-and-bionics", "Hackernoon on the furture of AI", 3, 1),
("Ed Pietrzak", "https://www.linkedin.com/in/edpietrzak/", "", 2, 1),
("Full Stack Developer, Digital", "https://www.indeed.com/jobs?q=software+developer&l=Remote&vjk=5a8405506b1fd4ab&advn=257105267871190", "Colgate-Palmolive - Develop UI", 1, 1),
('John Ryding', 'https://www.linkedin.com/in/johnryding/', 'Saying Yes And to Software Engineering', 2, 1),
('Anton Haugen', 'linkedin.com/in/anton-haugen-89478544', 'Date a scientist!', 2, 1),
('Jake Albaugh', 'https://www.linkedin.com/in/jak-e/', ' Design stuff, Figma, JavaScript, TypeScript', 2, 1),
('Mason Taylor', 'https://www.linkedin.com/in/mtaylor77/', 'transitioning from service industry to dev', 2, 1),
('James Tuttle', 'https://www.linkedin.com/in/jamesjtuttle/', 'Full stack AND Amazon and all around nice guy', 2, 1),
('Luke Yamasaki', 'linkedin.com/in/anton-haugen-89478544', 'His name is my name too', 2, 1),
('Joe Mizzi', 'https://www.linkedin.com/in/joemizzi/', 'Kaseys Tavern', 2, 1);


INSERT INTO tags(name, category_id)
VALUES
("Apple", 4),
("Amazon", 4),
("Microsoft", 4),
("Netflix", 4),
("Facebook", 4),
("Figma", 4),
("Sprout", 4),
("Tesla", 4),
("AI", 1),
("machine learning", 1),
("Python", 1),
("JavaScript", 1),
("Java", 1),
("TypeScript", 1),
("React Native", 1),
("TensorFlow", 1),
("MyPy", 1),
("clean energy", 3),
("biotech", 3),
("education", 3),
("Chicago", 5),
("Boston", 5),
("New York City", 5),
("Los Angeles", 5),
("Seattle", 5),
("mobile", 2),
("internet of things", 2),
("back end development", 2),
("front end development", 2),
("full stack development", 2);

INSERT INTO tag_links(link_id, tag_id)
VALUES
(1, 3),
(2, 2),
(3, 3),
(4, 5),
(4, 9),
(6, 1),
(7, 3),
(7, 2),
(8, 3),
(9, 4),
(10, 5),
(11, 6),
(12, 7),
(8, 8),
(9, 9);

INSERT INTO tag_priorities(priority_id, tag_id)
VALUES
(1, 6),
(2, 5),
(2, 9),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(3, 6);

SELECT * FROM users;
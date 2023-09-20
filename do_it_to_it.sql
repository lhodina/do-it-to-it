
UPDATE priorities
SET text = 'Laszlo Jamf',
level = 3
WHERE id = 4;

SELECT * FROM priorities;


-- INSERT INTO users(first_name, last_name, email, password)
-- VALUES("Larry", "David", "LDav1d@gmail.com", "LDav1d@gmail.com");

-- INSERT INTO priorities(text, level, user_id)
-- VALUES
-- ("Finish Coursera class before auto-renew!", 3, 1),
-- ("Reach out to Ed about back-end work in Chicago", 1, 1),
-- ("Practice recursion algos", 0, 1);

-- INSERT INTO tags(name)
-- VALUES('interviews');

-- INSERT INTO link_types(name)
-- VALUES
-- ('Jobs'),
-- ('Contacts'),
-- ('Articles');

-- INSERT INTO categories(name)
-- VALUES
-- ('Technologies'),
-- ('Specializations'),
-- ('Industries'),
-- ('Companies'),
-- ('Locations');

-- INSERT INTO links(text, url, description, link_type_id, user_id)
-- VALUES
-- ("DataAnnotation AI Trainer - Remote", "https://www.indeed.com/jobs?q=software+developer&l=Remote&vjk=86b8607f1193a1a0&advn=7831672186689475", "Embedded systems", 1, 1),
-- ("If you’d bought Apple shares instead of iPhones, you’d now have $147,000", "https://techcrunch.com/2023/09/15/one-meeeelion-dollars-muuhahahahaha/", "Apple stock", 3, 1),
-- ("Robotics, LLMs: Exploring Consciousness, Sentience for AI Chatbots, and Bionics", "https://hackernoon.com/robotics-llms-exploring-consciousness-sentience-for-ai-chatbots-and-bionics", "Hackernoon on the furture of AI", 3, 1),
-- ("Ed Pietrzak", "https://www.linkedin.com/in/edpietrzak/", "", 2, 1),
-- ("Full Stack Developer, Digital", "https://www.indeed.com/jobs?q=software+developer&l=Remote&vjk=5a8405506b1fd4ab&advn=257105267871190", "Colgate-Palmolive - Develop UI", 1, 1),
-- ('John Ryding', 'https://www.linkedin.com/in/johnryding/', 'Saying Yes And to Software Engineering', 2, 1),
-- ('Anton Haugen', 'linkedin.com/in/anton-haugen-89478544', 'You have not read Samuel Beckett', 2, 1);

-- INSERT INTO tags(name, category_id)
-- VALUES
-- ("apple", 4),
-- ("ai", 1),
-- ("clean energy", 3),
-- ("chicago", 5),
-- ("machine learning", 1),
-- ("mobile", 2),
-- ("internet of things", 2),
-- ("back end development", 2);

-- INSERT INTO tag_links(link_id, tag_id)
-- VALUES
-- (1, 3),
-- (2, 2),
-- (3, 3),
-- (4, 5),
-- (4, 9),
-- (6, 1),
-- (7, 3),
-- (6, 3);

-- INSERT INTO tag_priorities(priority_id, tag_id)
-- VALUES
-- (1, 6),
-- (2, 5),
-- (2, 9),
-- (3, 1);

-- SELECT * FROM users;
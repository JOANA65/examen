INSERT INTO category (name) VALUES ('Programación'), ('Diseño');

INSERT INTO course (name, category_id) VALUES
('Python Básico', 1),
('Flask API', 1),
('JavaScript', 1),
('HTML', 1),
('CSS', 1),
('UI Design', 2),
('UX Research', 2),
('Photoshop', 2),
('Illustrator', 2),
('Figma', 2);

INSERT INTO student (name) VALUES
('Juan Perez'),
('Maria Lopez'),
('Carlos Ruiz'),
('Ana Torres'),
('Luis Gomez');

INSERT INTO enrollments (student_id, course_id) VALUES
(1,1),(1,2),
(2,3),(2,4),
(3,5),(3,6),
(4,7),(4,8),
(5,9),(5,10);
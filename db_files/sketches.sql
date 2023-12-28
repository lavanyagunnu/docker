DROP TABLE IF EXISTS sketches_data;
CREATE TABLE sketches_data (
    Id INT,
    Date_created TIMESTAMP,
    Artist_name VARCHAR(255),
    Title VARCHAR(255),
    File_name VARCHAR(255)
);

INSERT INTO sketches_data (Id, Date_created, Artist_name, Title, File_name)
VALUES
    (1, '2022-09-12', 'Lavanya', 'Lord Ganesha', 'Picsart_22-09-13_15-32-23-709.jpg'),
    (2, '2022-12-30', 'Lavanya', 'Kailash Potrait', 'Picsart_22-12-30_14-18-57-746.jpg'),
    (3, '2022-09-22', 'Lavanya', 'Sita Ramam', 'Picsart_22-09-22_13-57-09-144~4.jpg'),
    (4, '2023-05-31', 'Lavanya', 'Gumpina Couple Potrait', 'Picsart_23-05-31_12-41-03-909.jpg');



create table holiday (
    holi_date date primary key,
    holi_text varchar(20)
);


DESCRIBE holiday;

INSERT INTO holiday (holi_date,holi_text) values
('2024-01-01','元旦'),
('2024-01-08','成人の日');
('2024-02-11','建国記念の日'),
('2024-02-12','振替休日'),
('2024-02-23','天皇誕生日');

SELECT * FROM holiday;
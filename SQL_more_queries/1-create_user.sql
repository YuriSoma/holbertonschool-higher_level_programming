-- SHOW privileges of some users

CREATE USER IF NO EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* FOR 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
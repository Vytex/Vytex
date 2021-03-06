CREATE TABLE IF NOT EXISTS app.USERS(
userID INT AUTO_INCREMENT PRIMARY KEY,
fName nvarchar(50) NOT NULL,
lName nvarchar(50) NOT NULL,
birthdate date NOT NULL,
email nvarchar(320) NOT NULL,
pass nvarchar(25) NOT NULL,
icon char(1) NOT NULL
);
CREATE TABLE IF NOT EXISTS app.venue(
venueID INT AUTO_INCREMENT PRIMARY KEY,
venue nvarchar(30) NOT NULL,
description nvarchar(500) NOT NULL,
mon time(4),
tue time(4),
wed time(4),
thu time(4),
fri time(4),
sat time(4),
sun time(4)
);
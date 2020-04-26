DROP TABLE IOT_TEST.DATA;
DROP TABLE IOT_TEST.NODES;
DROP TABLE IOT_TEST.USERS;


CREATE TABLE IOT_TEST.USERS (
		idPK INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50)  NOT NULL UNIQUE,
    pass VARCHAR(50)  NOT NULL,
		email VARCHAR(50)  NOT NULL
 );

 CREATE TABLE IOT_TEST.NODES (
		idNode INTEGER PRIMARY KEY AUTO_INCREMENT,
    nodeName VARCHAR(15) NOT NULL UNIQUE,
    plant VARCHAR(50)  NOT NULL,
    idUser INTEGER NOT NULL,
		tempMax FLOAT,
		tempMin FLOAT,
		phMax FLOAT,
		phMin FLOAT,
		humMax FLOAT,
		humMin FLOAT,
    FOREIGN KEY (idUser) REFERENCES USERS(idPK)
 );

CREATE TABLE IOT_TEST.DATA (
		idData INTEGER PRIMARY KEY AUTO_INCREMENT,
    ph FLOAT,
    temperature FLOAT,
		humidity FLOAT,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    times DATETIME NOT NULL,
    idNode INTEGER NOT NULL,
    FOREIGN KEY (idNode) REFERENCES NODES(idNode)
);

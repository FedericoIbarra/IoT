-------------------------------------------------------------------------------
----------------------------------Queries--------------------------------------
-------------------------------------------------------------------------------


--Login--
SELECT username FROM IOT_TEST.USERS u WHERE u.username = "username1" and u.pass = "pass";

--All data--
SELECT n.nodeName, n.plant, d.ph, d.temperature, d.humidity, d.day, d.month, d.year, d.times
FROM IOT_TEST.DATA d
JOIN IOT_TEST.NODES n ON d.idNode = n.idNode
JOIN IOT_TEST.USERS u ON u.idPK = n.idUser
WHERE u.username = "usr1"
ORDER BY d.times;

--Current by node--
SELECT n.nodeName, n.plant, d.ph, d.temperature, d.humidity, d.day, d.month, d.year, d.times
FROM IOT_TEST.DATA d
JOIN IOT_TEST.NODES n ON d.idNode = n.idNode
JOIN IOT_TEST.USERS u ON u.idPK = n.idUser
WHERE u.username = "usr1" and n.nodeName = "Mock 1"
ORDER BY d.times DESC
LIMIT 1;

--By week by node--
SELECT n.nodeName, n.plant, avg(d.ph) as ph, avg(d.temperature) as temp, avg(d.humidity) as hum, d.day, d.month, d.year, d.times
FROM IOT_TEST.DATA d
JOIN IOT_TEST.NODES n ON d.idNode = n.idNode
JOIN IOT_TEST.USERS u ON u.idPK = n.idUser
WHERE u.username = "usr1" and n.nodeName = "Mock 1"
GROUP BY d.day, d.month, d.year
ORDER BY d.times DESC
LIMIT 7;

--By year by node--
SELECT n.nodeName, n.plant, avg(d.ph) as ph, avg(d.temperature) as temp, avg(d.humidity) as hum, d.year, d.times
FROM IOT_TEST.DATA d
JOIN IOT_TEST.NODES n ON d.idNode = n.idNode
JOIN IOT_TEST.USERS u ON u.idPK = n.idUser
WHERE u.username = "usr1" and n.nodeName = "Mock 1"
GROUP BY d.year
ORDER BY d.times DESC
LIMIT 1;



-------------------------------------------------------------------------------
--------------------------------Mocks data-------------------------------------
-------------------------------------------------------------------------------

--Log up--
INSERT INTO IOT_TEST.USERS (username, pass, email) VALUES (
    "usr1",
    "pass1",
    "email1"
);

--New Nodes--
INSERT INTO  IOT_TEST.NODES (nodeName, plant, idUser, tempMax, tempMin, phMax, phMin, humMax, humMin)
  VALUES (
    "Mock 1",
    "Choyas",
    1,
    27.0,
    22.0,
    7.0,
    6.5,
    68,
    72
);

INSERT INTO  IOT_TEST.NODES (nodeName, plant, idUser, tempMax, tempMin, phMax, phMin, humMax, humMin)
  VALUES (
    "Mock 2",
    "Lechugas",
    1,
    27.0,
    22.0,
    7.0,
    6.5,
    68,
    72
);


--New data--
INSERT INTO IOT_TEST.DATA (idNode, ph, temperature, humidity, day, month, year, times)
  VALUES
   	 (1, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (1, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (1, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (1, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (1, 7.0, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (1, 7.0, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (1, 7.0, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (1, 7.0, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (1, 7.0, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (1, 7.0, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (1, 7.0, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (1, 7.0, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (1, 7.0, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (1, 7.0, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (1, 7.0, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (1, 7.0, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (1, 7.0, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (1, 7.0, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (1, 7.0, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (1, 7.0, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
   	 (2, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (2, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (2, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (2, 7.0, 22, 70, 18, 4, 2020, "2020-04-18 00:00:01"),
     (2, 7.1, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (2, 7.1, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (2, 7.1, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (2, 7.1, 22, 70, 19, 4, 2020, "2020-04-19 00:00:01"),
     (2, 7.2, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (2, 7.2, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (2, 7.2, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (2, 7.2, 22, 70, 20, 4, 2020, "2020-04-20 00:00:01"),
     (2, 7.3, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (2, 7.3, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (2, 7.3, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (2, 7.3, 22, 70, 21, 4, 2020, "2020-04-21 00:00:01"),
     (2, 6.9, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (2, 6.9, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (2, 6.9, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01"),
     (2, 6.9, 22, 70, 22, 4, 2020, "2020-04-22 00:00:01");

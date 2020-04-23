INSERT INTO IOT_TEST.USERS (username, pass, email, plant) VALUES (
 	"usr1",
	"pass1",
	"email1",
	"plant1"
);

SELECT username FROM IOT_TEST.USERS u WHERE u.username = "username1" and u.pass = "pass";

SELECT idHw, AVG(ph )as pH, AVG(temperature) as Temperature, day, month, year, times
FROM IOT_TEST.data
GROUP BY day, month, year
ORDER BY times
LIMIT 5;

SELECT AVG(ph )as pH, AVG(temperature) as Temperature, day, month, year, times
FROM IOT_TEST.data
GROUP BY year
ORDER BY year
LIMIT 1;

SELECT ph, temperature, times
FROM IOT_TEST.data
ORDER BY times
LIMIT 1;

--Mocks data--
INSERT INTO IOT_TEST.data (idHw, ph, temperature, day, month, year, times)
  VALUES
   	 ("Mock 1", 7.0, 22, 18, 4, 2020, "1970-04-18 00:00:01"),
     ("Mock 2", 7.0, 22, 18, 4, 2020, "1970-04-18 00:00:01"),
     ("Mock 3", 7.0, 22, 18, 4, 2020, "1970-04-18 00:00:01"),
     ("Mock 4", 7.0, 22, 18, 4, 2020, "1970-04-18 00:00:01"),
     ("Mock 5", 7.0, 22, 19, 4, 2020, "1970-04-19 00:00:01"),
     ("Mock 6", 7.0, 22, 19, 4, 2020, "1970-04-19 00:00:01"),
     ("Mock 7", 7.0, 22, 19, 4, 2020, "1970-04-19 00:00:01"),
     ("Mock 8", 7.0, 22, 19, 4, 2020, "1970-04-19 00:00:01"),
     ("Mock 9", 7.0, 22, 20, 4, 2020, "1970-04-20 00:00:01"),
     ("Mock 10", 7.0, 22, 20, 4, 2020, "1970-04-20 00:00:01"),
     ("Mock 11", 7.0, 22, 20, 4, 2020, "1970-04-20 00:00:01"),
     ("Mock 12", 7.0, 22, 20, 4, 2020, "1970-04-20 00:00:01"),
     ("Mock 13", 7.0, 22, 21, 4, 2020, "1970-04-21 00:00:01"),
     ("Mock 14", 7.0, 22, 21, 4, 2020, "1970-04-21 00:00:01"),
     ("Mock 15", 7.0, 22, 21, 4, 2020, "1970-04-21 00:00:01"),
     ("Mock 16", 7.0, 22, 21, 4, 2020, "1970-04-21 00:00:01"),
     ("Mock 17", 7.0, 22, 22, 4, 2020, "1970-04-22 00:00:01"),
     ("Mock 18", 7.0, 22, 22, 4, 2020, "1970-04-22 00:00:01"),
     ("Mock 19", 7.0, 22, 22, 4, 2020, "1970-04-22 00:00:01"),
     ("Mock 20", 7.0, 22, 22, 4, 2020, "1970-04-22 00:00:01");

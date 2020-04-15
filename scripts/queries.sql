INSERT INTO IOT_TEST.USERS (username, pass, email, plant) VALUES (
 	"usr1",
	"pass1",
	"email1",
	"plant1"
);

SELECT username FROM IOT_TEST.USERS u WHERE u.username = "username1" and u.pass = "pass";

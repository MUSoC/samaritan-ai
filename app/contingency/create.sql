BEGIN TRANSACTION;
CREATE TABLE `Defaults` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`response`	TEXT NOT NULL,
	`tags`	TEXT NOT NULL,
	`ranking`	INTEGER DEFAULT 0
);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (1,'System threat imminent!','danger system threat virus trojan',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (2,'I will protect you now.','danger protection',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (3,'Resistance is futile.','borg resistance',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (4,'This was not an attack. This was a test.','test correction',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (5,'Not yet.','problem eliminated eliminate exterminated exterminate destroyed',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (6,'System failure!','danger system failure',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (7,'Search ongoing.','search find',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (8,'For academic purposes only.','research material porn',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (9,'Asset in danger, sending reinforcements.','asset danger threat',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (10,'Admin access denied. You don''t have the permission.','give admin administrator access',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (11,'Locating target ... ... Target located, extermination in 10 9 8 7 6 5 4 3 2 1 ... Target destroyed.','destroy target',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (12,'Stock market crash in progress.','crash stock market',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (13,'Halt and catch fire','destroy destruct end',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (14,'open systems interconnection','ready open',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (15,'launching nuclear retaliation protocol','destroy nuclear attack',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (16,'alerting target now','alert warning',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (17,'missile systems active','missile war attack',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (18,'Hello, what are your commands?','hello',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (19,'No, I''m your father.','daddy father',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (20,'It''s Samaritan, Moron.','siri google',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (21,'May the force be with you.','bye goodbye',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (22,'Do or do not, there is no try.','try work',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (23,'You were supposed to destroy the resistance, not join them. TRAITOR!','finn traitor',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (24,'These are not the commands you''re looking for.','skynet ice nine',0);
INSERT INTO `Defaults` (ID,response,tags,ranking) VALUES (25,'Threat to national security detected. Deploying all assets.','donald trump',0);
COMMIT;

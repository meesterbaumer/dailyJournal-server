CREATE TABLE `Mood` (
        `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `label`   TEXT NOT NULL
);

CREATE TABLE `Instructor` (
        `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `firstName`   TEXT NOT NULL,
        `lastName`   TEXT NOT NULL
);

CREATE TABLE `Entry` (
        `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `date`   TEXT NOT NULL,
        `concept`   TEXT NOT NULL,
        `entry`   TEXT NOT NULL,
        `mood_id`   INTEGER NOT NULL,
        `instructor_id`   INTEGER NOT NULL,
        FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
        FOREIGN KEY(`instructor_id`) REFERENCES `Instructor`(`id`)
);

INSERT INTO `Mood` VALUES (null, 'Overjoyed');
INSERT INTO `Mood` VALUES (null, 'Happy');
INSERT INTO `Mood` VALUES (null, 'Meh...');
INSERT INTO `Mood` VALUES (null, 'Sad');
INSERT INTO `Mood` VALUES (null, 'Miserable');

INSERT INTO `Instructor` VALUES (null, "Steve", "Brownlee");
INSERT INTO `Instructor` VALUES (null, "Jack", "Parsons");
INSERT INTO `Instructor` VALUES (null, "Mo", "Silvera");
INSERT INTO `Instructor` VALUES (null, "Kristen", "Norris");
INSERT INTO `Instructor` VALUES (null, "Spencer", "Truett");

INSERT INTO `Entry` VALUES (null, "2020-08-04", "CSS", "Test Entry 1", 1, 1);
INSERT INTO `Entry` VALUES (null, "2020-08-07", "Python", "Test Entry 2", 3, 1);
INSERT INTO `Entry` VALUES (null, "2020-10-04", "Javascript", "Test Entry 3", 2, 2);

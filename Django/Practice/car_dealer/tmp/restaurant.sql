CREATE TABLE IF NOT EXISTS country (
    id int NOT NULL,
    country_name varchar(30) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS city (
    id int NOT NULL,
    name varchar(30) NOT NULL UNIQUE,
    country_id int NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country (id) ON DELETE CASCADE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS restaurant (
    id int NOT NULL,
    name varchar(30) NOT NULL,
    city int NOT NULL,
    FOREIGN KEY (city) REFERENCES city (id) ON DELETE SET NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS personnel (
    id int NOT NULL,
    position varchar(30) NOT NULL,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    restaurant int NOT NULL,
    FOREIGN KEY (restaurant) REFERENCES restaurant (id) ON DELETE CASCADE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS menu (
    id int NOT NULL,
    season int NOT NULL,
    restaurant int NOT NULL,
    FOREIGN KEY (restaurant) REFERENCES restaurant (id) ON DELETE CASCADE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS dish (
    id int NOT NULL,
    name varchar(35) NOT NULL,
    season int NOT NULL,
    menu int NOT NULL,
    FOREIGN KEY (menu) REFERENCES menu (id) ON DELETE CASCADE,
    PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS country_name ON country (country_name);
CREATE INDEX IF NOT EXISTS city_name ON city (name);
CREATE INDEX IF NOT EXISTS city_name ON restaurant (city);

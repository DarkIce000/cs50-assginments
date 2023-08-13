CREATE TABLE buy (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id  TEXT NOT NULL,
    shares INTEGER,
    transaction_time TEXT NOT NULL
);

CREATE TABLE sell (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id  TEXT NOT NULL,
    shares INTEGER,
    transaction_time TEXT NOT NULL
);


--------------------------------------
CREATE TABLE transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    transaction_type TEXT,
    symbols TEXT,
    shares INTEGER,
    price INTEGER,
    transaction_time TEXT
);
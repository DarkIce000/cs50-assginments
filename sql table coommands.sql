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
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    symbols TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price INTEGER NOT NULL,
    transaction_time TEXT NOT NULL
);
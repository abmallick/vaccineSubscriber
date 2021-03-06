DROP TABLE IF EXISTS requests;

CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pin_code TEXT NOT NULL,
    email_id TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
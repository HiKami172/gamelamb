DROP TABLE IF EXISTS SessionPlayers;
DROP TABLE IF EXISTS GameSession;
DROP TABLE IF EXISTS Games;


CREATE TABLE Games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    min_players INTEGER NOT NULL DEFAULT 1,
    max_players INTEGER NOT NULL DEFAULT 2
);

CREATE TABLE GameSession (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id TEXT NOT NULL,
    session_url TEXT NOT NULL,
    room_name TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'waiting',
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

CREATE TABLE SessionPlayers (
    player_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL,
    session_id INTEGER NOT NULL,
    is_host BOOLEAN NOT NULL default FALSE,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES GameSession(session_id)
);
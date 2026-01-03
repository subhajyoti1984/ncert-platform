CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sessions (
    token TEXT PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    expires_at TIMESTAMP NOT NULL
);

CREATE TABLE concept_progress (
    user_id UUID,
    concept_id TEXT,
    status TEXT,
    attempts INT DEFAULT 0,
    dominant_mistake TEXT,
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (user_id, concept_id)
);

CREATE TABLE section_progress (
    user_id UUID,
    section_id TEXT,
    completion_percentage FLOAT,
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (user_id, section_id)
);

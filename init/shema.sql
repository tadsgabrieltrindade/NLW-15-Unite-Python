-- Tabela nlw_events.events
CREATE TABLE nlw_events.events (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    details NVARCHAR(MAX) NULL,
    slug NVARCHAR(255) NOT NULL,
    maximum_attendees INT NULL
);

-- Tabela nlw_events.attendees
CREATE TABLE nlw_events.attendees (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) NOT NULL,
    event_id INT NOT NULL,
    created_at DATETIME2 NOT NULL DEFAULT GETDATE(),
    CONSTRAINT attendees_event_id_fkey FOREIGN KEY (event_id) REFERENCES nlw_events.events (id) ON DELETE NO ACTION ON UPDATE CASCADE
);

-- Tabela nlw_events.check_ins
CREATE TABLE nlw_events.check_ins (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    created_at DATETIME2 NOT NULL DEFAULT GETDATE(),
    attendeeId INT NOT NULL,
    CONSTRAINT check_ins_attendeeId_fkey FOREIGN KEY (attendeeId) REFERENCES nlw_events.attendees (id) ON DELETE NO ACTION ON UPDATE CASCADE
);

-- Índices exclusivos
CREATE UNIQUE INDEX events_slug_key ON nlw_events.events(slug);
CREATE UNIQUE INDEX attendees_event_id_email_key ON nlw_events.attendees(event_id, email);
CREATE UNIQUE INDEX check_ins_attendeeId_key ON nlw_events.check_ins(attendeeId);

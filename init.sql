-- Create the User table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- Use SERIAL instead of INTEGER AUTOINCREMENT
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    full_name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    doc_number INTEGER UNIQUE NOT NULL,
    cash REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Service table
CREATE TABLE services (
    id SERIAL PRIMARY KEY,  -- Use SERIAL instead of INTEGER AUTOINCREMENT
    service_name TEXT UNIQUE NOT NULL,
    service_type TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Debt table
CREATE TABLE debts (
    id SERIAL PRIMARY KEY,  -- Use SERIAL instead of INTEGER AUTOINCREMENT
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    total_debt REAL NOT NULL,
    remaining_debt REAL NOT NULL,
    due_date TIMESTAMP NOT NULL,
    status TEXT CHECK(status IN ('PAID', 'IN_PROGRESS')) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),  -- Use correct table name (users)
    FOREIGN KEY (service_id) REFERENCES services(id)  -- Use correct table name (services)
);

-- Create the Payment table
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,  -- Use SERIAL instead of INTEGER AUTOINCREMENT
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    reference TEXT NOT NULL,
    total_debt INTEGER NOT NULL,
    amount_paid INTEGER NOT NULL,
    proof TEXT NOT NULL,  -- Assume this is a hash stored as a string
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    additional_info JSON,
    FOREIGN KEY (user_id) REFERENCES users(id),  -- Use correct table name (users)
    FOREIGN KEY (service_id) REFERENCES services(id)  -- Use correct table name (services)
);

-- Add indexes
CREATE INDEX idx_user_full_name ON users (full_name);
CREATE INDEX idx_service_service_type ON services (service_type);

-- Insert some example services
INSERT INTO services (service_name, service_type) VALUES
('ANDE', 'Electricidad'),
('TIGO', 'Telecom'),
('PERSONAL', 'Telecom'),
('CASA ELECTRODOMESTICOS', 'Comercio'),
('CUOTA PRESTAMOS', 'Finanzas');

-- Example of inserting a user (Note: passwords should be hashed in practice)
INSERT INTO users (fname, lname, full_name, email, doc_number, password, cash) VALUES
('John', 'Doe', 'Doe, John', 'john.doe@example.com', 1234567, '$2b$12$LLokJqTENpLBy62r0G1H/OBQbCWueppt.c9PfsLbgygNN4aGmHv6S', 500);

-- Example of inserting a debt (with an initial debt amount and due date)
INSERT INTO debts (user_id, service_id, total_debt, remaining_debt, due_date, status) VALUES
(1, 1, 100.00, 100.00, '2024-12-31 00:00:00', 'PAID'),
(1, 2, 50.00, 10.00, '2024-12-31 00:00:00', 'IN_PROGRESS');

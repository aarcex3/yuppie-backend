-- Create users table to store user registration and login details
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    doc_number VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Store hashed passwords
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create services table to store service providers like ANDE, TIGO, etc.
CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some example services
INSERT INTO services (service_name) VALUES
('ANDE'),
('TIGO'),
('PERSONAL'),
('CASA ELECTRODOMESTICOS'),
('CUOTA PRESTAMOS');

-- Create payments table to store user payments
CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    service_id INT REFERENCES services(id) ON DELETE CASCADE,
    reference_number VARCHAR(50) NOT NULL,
    total_debt NUMERIC(10, 2) NOT NULL,
    amount_paid NUMERIC(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    additional_info JSONB DEFAULT '{}'  -- Store additional parameters in JSON format
);

-- Create reports table to store user-generated reports for payment history
CREATE TABLE IF NOT EXISTS reports (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    report_data JSONB NOT NULL,  -- Store report data in JSON format
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- Example of inserting a user (Note: passwords should be hashed in practice)
INSERT INTO users (email, name, doc_number, password_hash) VALUES
('john.doe@example.com', 'John Doe', '12345678', 'hashed_password_here');

-- Example payment insertion
INSERT INTO payments (user_id, service_id, reference_number, total_debt, amount_paid, additional_info) VALUES
(1, 1, 'NIS123456', 100.00, 100.00, '{"note": "Paid in full"}'),
(1, 2, '12345678', 50.00, 50.00, '{"note": "Paid in full"}');

-- Example report insertion
INSERT INTO reports (user_id, report_data, start_date, end_date) VALUES
(1, '{"payments": [{"service": "ANDE", "amount": 100.00}, {"service": "TIGO", "amount": 50.00}]}', '2024-01-01', '2024-01-31');

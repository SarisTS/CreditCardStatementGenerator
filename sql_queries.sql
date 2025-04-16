-- Create the Customer table
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address TEXT NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    Country VARCHAR(20) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(254) NOT NULL,
    IdentificationNumber VARCHAR(50) NOT NULL,
    RegistrationDate DATE NOT NULL,
    Status VARCHAR(10) NOT NULL DEFAULT 'active' CHECK (Status IN ('active', 'inactive', 'pending', 'blocked'))
);

-- Create the CreditCardAccount table
CREATE TABLE CreditCardAccount (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_id INT NOT NULL,
    CardNumber VARCHAR(20) NOT NULL,
    CardType VARCHAR(20) NOT NULL,
    CreditLimit DECIMAL(10, 2) NOT NULL,
    CurrentBalance DECIMAL(10, 2) NOT NULL,
    AvailableCredit DECIMAL(10, 2) NOT NULL,
    ExpiryDate DATE NOT NULL,
    IssueDate DATE NOT NULL,
    PaymentDueDate DATE NOT NULL,
    MinimumPaymentPercentage VARCHAR(50) NOT NULL,
    InterestRate VARCHAR(50) NOT NULL,
    Status VARCHAR(10) NOT NULL DEFAULT 'active' CHECK (Status IN ('active', 'inactive', 'pending', 'blocked')),
    PreviousBalance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    TotalPayment DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    NewPurchases DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    MinDue DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    TotalDue DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    CashLimit DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    AvailableCash DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (Customer_id) REFERENCES Customer(CustomerID) ON DELETE CASCADE
);

-- Create the Transaction table
CREATE TABLE Transaction (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    Account_id INT NOT NULL,
    TransactionDate DATE NOT NULL,
    MerchantName VARCHAR(100) NOT NULL,
    MerchantLocation VARCHAR(100) NOT NULL,
    MerchantCategory VARCHAR(100) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    TransactionType VARCHAR(20) NOT NULL,
    FOREIGN KEY (Account_id) REFERENCES CreditCardAccount(AccountID) ON DELETE CASCADE
);

-- Create the RewardPoint table
CREATE TABLE RewardPoint (
    RewardID INT AUTO_INCREMENT PRIMARY KEY,
    Account_id INT NOT NULL,
    PointsEarned INT NOT NULL DEFAULT 0,
    PointsRedeemed INT NOT NULL DEFAULT 0,
    FOREIGN KEY (Account_id) REFERENCES CreditCardAccount(AccountID) ON DELETE CASCADE
);



-- Sample data for Customer table
INSERT INTO Customer (FirstName, LastName, DateOfBirth, Address, City, State, PostalCode, Country, PhoneNumber, Email, IdentificationNumber, RegistrationDate, Status) VALUES
('John', 'Smith', '1985-03-15', '123 Main St', 'Boston', 'Massachusetts', '02108', 'USA', '+1-555-123-4567', 'john.smith@email.com', 'SSN-123-45-6789', '2023-01-10', 'active'),
('Emily', 'Johnson', '1990-07-22', '456 Oak Avenue', 'Chicago', 'Illinois', '60601', 'USA', '+1-555-234-5678', 'emily.j@email.com', 'SSN-234-56-7890', '2023-02-15', 'active'),
('Michael', 'Williams', '1978-11-30', '789 Pine Road', 'San Francisco', 'California', '94105', 'USA', '+1-555-345-6789', 'mwilliams@email.com', 'SSN-345-67-8901', '2023-03-05', 'inactive'),
('Sarah', 'Brown', '1992-05-18', '101 Maple Drive', 'New York', 'New York', '10007', 'USA', '+1-555-456-7890', 'sarahb@email.com', 'SSN-456-78-9012', '2023-04-20', 'active'),
('David', 'Garcia', '1983-09-12', '234 Cedar Lane', 'Miami', 'Florida', '33101', 'USA', '+1-555-567-8901', 'dgarcia@email.com', 'SSN-567-89-0123', '2023-05-12', 'pending');

-- Sample data for CreditCardAccount table
INSERT INTO CreditCardAccount (Customer_id, CardNumber, CardType, CreditLimit, CurrentBalance, AvailableCredit, ExpiryDate, IssueDate, PaymentDueDate, MinimumPaymentPercentage, InterestRate, Status, PreviousBalance, TotalPayment, NewPurchases, MinDue, TotalDue, CashLimit, AvailableCash) VALUES
(1, '4111-1111-1111-1111', 'Visa', 5000.00, 1250.75, 3749.25, '2027-04-30', '2023-05-01', '2025-05-15', '2.5%', '18.99%', 'active', 1100.50, 300.00, 450.25, 125.00, 1250.75, 1000.00, 1000.00),
(2, '5555-5555-5555-4444', 'MasterCard', 8000.00, 3200.50, 4799.50, '2026-08-31', '2022-09-01', '2025-05-20', '3%', '19.99%', 'active', 2800.25, 500.00, 900.25, 160.00, 3200.50, 1600.00, 1600.00),
(3, '3782-8224-6310-005', 'American Express', 12000.00, 0.00, 12000.00, '2026-11-30', '2022-12-01', '2025-05-25', '2%', '17.99%', 'inactive', 0.00, 0.00, 0.00, 0.00, 0.00, 2400.00, 2400.00),
(4, '6011-1111-1111-1117', 'Discover', 7500.00, 5200.80, 2299.20, '2027-03-31', '2023-04-01', '2025-05-15', '3%', '20.99%', 'active', 4800.30, 600.00, 1000.50, 260.00, 5200.80, 1500.00, 0.00),
(1, '4123-4567-8901-2345', 'Visa', 6000.00, 500.25, 5499.75, '2028-02-28', '2024-03-01', '2025-05-10', '2.5%', '18.99%', 'active', 350.75, 200.00, 349.50, 25.00, 500.25, 1200.00, 1200.00);

-- Sample data for Transaction table
INSERT INTO Transaction (Account_id, TransactionDate, MerchantName, MerchantLocation, MerchantCategory, Amount, TransactionType) VALUES
(1, '2025-04-01', 'Amazon', 'Online', 'Retail', 129.99, 'Purchase'),
(1, '2025-04-03', 'Starbucks', 'Boston, MA', 'Food & Beverage', 8.75, 'Purchase'),
(1, '2025-04-07', 'Shell', 'Boston, MA', 'Gas & Fuel', 45.50, 'Purchase'),
(1, '2025-04-10', 'Payment', 'Online Banking', 'Payment', 300.00, 'Payment'),
(2, '2025-04-02', 'Target', 'Chicago, IL', 'Retail', 215.67, 'Purchase'),
(2, '2025-04-05', 'Uber', 'Chicago, IL', 'Transportation', 32.50, 'Purchase'),
(2, '2025-04-08', 'Whole Foods', 'Chicago, IL', 'Groceries', 187.34, 'Purchase'),
(2, '2025-04-12', 'Payment', 'Online Banking', 'Payment', 500.00, 'Payment'),
(4, '2025-04-03', 'Best Buy', 'New York, NY', 'Electronics', 899.99, 'Purchase'),
(4, '2025-04-06', 'Netflix', 'Online', 'Entertainment', 14.99, 'Purchase'),
(4, '2025-04-09', 'Delta Airlines', 'Online', 'Travel', 450.00, 'Purchase'),
(4, '2025-04-15', 'Payment', 'Online Banking', 'Payment', 600.00, 'Payment'),
(5, '2025-04-05', 'Apple Store', 'Boston, MA', 'Electronics', 349.50, 'Purchase'),
(5, '2025-04-14', 'Payment', 'Online Banking', 'Payment', 200.00, 'Payment');

-- Sample data for RewardPoint table
INSERT INTO RewardPoint (Account_id, PointsEarned, PointsRedeemed) VALUES
(1, 1250, 500),
(2, 3200, 1000),
(3, 0, 0),
(4, 5200, 2500),
(5, 500, 0);
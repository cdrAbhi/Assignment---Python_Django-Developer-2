# **Distributed System Simulation with SQLite**

This project demonstrates a simple distributed system where different types of data—**Users**, **Products**, and **Orders**—are stored in separate SQLite databases. The system uses Python and threading to perform simultaneous data insertion operations, simulating a distributed environment.

## **Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup and Usage](#setup-and-usage)
- [Example Output](#example-output)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## **Introduction**

This project is designed to showcase how a distributed system can manage concurrent operations across multiple databases. Each database holds different types of information:
- **Users**: Stores user details such as name and email.
- **Products**: Stores product details such as name and price.
- **Orders**: Stores order details linking users and products with quantities.

Using Python’s threading module, the program inserts data into these databases simultaneously, ensuring efficiency and concurrency.

---

## **Features**

- Simulates a distributed system with **three independent SQLite databases**.
- Supports **simultaneous operations** using Python threads.
- Performs **data validation** before insertion (e.g., checks email format, positive prices, valid quantities).
- Logs all operations, warnings, and errors for easy debugging.
- Provides a lightweight and easy-to-understand solution for distributed systems.

---

## **Technologies Used**

- **Python**: Programming language for logic and threading.
- **SQLite**: Lightweight database for managing data storage.
- **Threading**: Python module for parallel execution.
- **DB Browser for SQLite**: Tool for visually inspecting the databases.

---

## **How It Works**

1. **Database Setup**:
   - Three SQLite databases are created: `users.db`, `products.db`, and `orders.db`.
   - Each database has a corresponding table (`users`, `products`, `orders`).

2. **Data Insertion**:
   - Separate Python threads handle inserting data into each database.
   - Data is validated to ensure correctness (e.g., valid email format, positive prices).

3. **Concurrency**:
   - Threads run independently, simulating simultaneous operations in a distributed system.

4. **Logging**:
   - All activities (insertions, warnings, and errors) are logged to `app.log`.

---

## **Setup and Usage**

### **Prerequisites**
- Python 3.x installed on your system.

### **Steps to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/distributed-sqlite-simulation.git
   cd distributed-sqlite-simulation
   ```

2. **Run the Program**:
   Execute the Python script to simulate the distributed system:
   ```bash
   python distributed_system.py
   ```

3. **Inspect the Databases**:
   Use **DB Browser for SQLite** or a similar tool to open and inspect `users.db`, `products.db`, and `orders.db`.

4. **View Logs**:
   Check `app.log` for detailed logs of all operations:
   ```plaintext
   2024-12-05 14:00:01 - Inserted User: (1, 'Alice', 'alice@example.com')
   2024-12-05 14:00:02 - Inserted Product: (1, 'Laptop', 1000.0)
   2024-12-05 14:00:02 - Inserted Order: (1, 1, 1, 2)
   ```

---

## **Example Output**

When you run the program, you will see output like this in the console:
```plaintext
Inserted User: (1, 'Alice', 'alice@example.com')
Inserted Product: (1, 'Laptop', 1000.0)
Inserted Order: (1, 1, 1, 2)
All data insertion completed. Check 'app.log' for details.
```

Each database will contain the inserted records.

---

## **Contributing**

Contributions are welcome! Follow these steps to contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a Pull Request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### **Acknowledgments**
This project serves as a hands-on example for learning about distributed systems, SQLite databases, and Python threading.



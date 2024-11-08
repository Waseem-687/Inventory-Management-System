
### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Waseem-687/Inventory-Management-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Inventory-Management-System/inventory_management_system
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Final Project: Inventory Management System (IMS)

### Project Title:

**Inventory Management System (IMS)**

### Objective:

Build a console-based system that manages inventory for a small business. The system should allow admins to create, update, view, and delete products in the inventory while keeping track of stock levels and handling multiple users with role-based permissions.

### Requirements & Functionalities:

1. **User Authentication and Role Management**
   - Support different roles like “Admin” and “User.”
   - Admins can add, edit, and delete products, whereas Users can only view inventory details.
   - Implement a basic login system with username and password validation.

2. **Product Management (OOP Concepts)**
   - Create a `Product` class with attributes like `product_id`, `name`, `category`, `price`, and `stock_quantity`.
   - Create methods for adding, editing, and deleting products.
   - Store product information using lists or dictionaries.

3. **Inventory Operations**
   - Track stock levels: when stock reaches a low threshold, prompt a restocking message.
   - Implement methods for viewing all products, searching by product name or category, and filtering by stock levels.
   - Allow stock adjustments for existing products (e.g., restock or reduce inventory based on sales).

4. **Error Handling**
   - Ensure proper error handling for invalid inputs, such as incorrect login details or attempts to update non-existent products.
   - Use exceptions to handle potential issues, ensuring smooth flow.

### Learning Outcomes

- **OOP principles**: Implement classes, encapsulation, and methods for CRUD operations.
- **Data Structures**: Use dictionaries and lists for data storage and manipulation.
- **Logic Building**: Develop functions for role-based access, transaction handling, and inventory management.
- **Error Handling**: Practice exception handling for robust code.


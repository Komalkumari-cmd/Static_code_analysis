import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item: The item name (must be a string)
        qty: Quantity to add (must be a non-negative integer)
        logs: Optional list to append log messages

    Returns:
        bool: True if successful, False otherwise
    """
    if logs is None:
        logs = []

    # Input validation
    if not item or not isinstance(item, str):
        logging.warning("Invalid item name: %s", item)
        return False

    if not isinstance(qty, int) or qty < 0:
        logging.warning("Invalid quantity: %s", qty)
        return False

    stock_data[item] = stock_data.get(item, 0) + qty
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    logging.info(log_message)
    return True


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item: The item name to remove
        qty: Quantity to remove

    Returns:
        bool: True if successful, False otherwise
    """
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for remove_item")
        return False

    if qty < 0:
        logging.warning("Cannot remove negative quantity")
        return False

    try:
        if item not in stock_data:
            logging.warning("Item '%s' not found in inventory", item)
            return False

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Item '%s' removed from inventory (quantity reached 0)", item)
        return True
    except (KeyError, TypeError) as error:
        logging.error("Error removing item: %s", error)
        return False


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item: The item name

    Returns:
        int: Quantity of the item, or 0 if not found
    """
    if item not in stock_data:
        logging.warning("Item '%s' not found in inventory", item)
        return 0
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as file_handle:
            stock_data = json.load(file_handle)
        logging.info("Data loaded from %s", file)
        return True
    except FileNotFoundError:
        logging.warning("File '%s' not found", file)
        return False
    except json.JSONDecodeError as error:
        logging.error("Error decoding JSON: %s", error)
        return False


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file: Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file, "w", encoding="utf-8") as file_handle:
            json.dump(stock_data, file_handle, indent=2)
        logging.info("Data saved to %s", file)
        return True
    except IOError as error:
        logging.error("Error saving data: %s", error)
        return False


def print_data():
    """Print the current inventory report."""
    print("\n=== Items Report ===")
    if not stock_data:
        print("No items in inventory")
        return

    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("=" * 20)


def check_low_items(threshold=5):
    """
    Check for items below a certain threshold.

    Args:
        threshold: The quantity threshold (default: 5)

    Returns:
        list: List of items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system functionality."""
    logging.info("Starting inventory system")

    # Add items with validation
    add_item("apple", 10)
    add_item("banana", 5)

    # These will fail validation
    add_item("banana", -2)  # Negative quantity
    add_item(123, "ten")  # Invalid types

    # Remove items
    remove_item("apple", 3)
    remove_item("orange", 1)  # Item doesn't exist

    # Query and report
    print(f"\nApple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    # Save and load data
    save_data()
    load_data()
    print_data()

    # Removed dangerous eval() call - was: eval("print('eval used')")
    logging.info("Inventory operations completed")


if __name__ == "__main__":
    main()
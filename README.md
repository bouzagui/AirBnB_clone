# AirBnB Clone - The Console

## Project Description
This project is part of the Holberton School's AirBnB clone series. The goal of this part of the project is to create a command interpreter (console) that will manage the objects of our application. The console allows us to create, update, delete, and retrieve instances of our data model, which are serialized and deserialized to and from JSON files.

The project is structured as follows:
- `base_model.py`: Contains the BaseModel class, which is the base class for all other models.
- `file_storage.py`: Contains the FileStorage class, which handles serialization and deserialization of instances to and from a JSON file.
- `console.py`: Contains the HBNBCommand class, which is the command interpreter.
- `__init__.py`: Initializes the FileStorage instance.
- Model files (`user.py`, `state.py`, `city.py`, `amenity.py`, `place.py`, `review.py`): Define specific models inheriting from BaseModel.

## Command Interpreter

### How to Start the Command Interpreter
To start the command interpreter, follow these steps:
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the command:
    ```bash
    ./console.py
    ```
4. You should see the prompt `(hbnb)` indicating that the command interpreter is running.

### How to Use the Command Interpreter
The command interpreter supports the following commands:
- `quit` or `EOF`: Exit the command interpreter.
- `create <class name>`: Creates a new instance of the specified class and prints the id.
- `show <class name> <id>`: Prints the string representation of the specified instance.
- `destroy <class name> <id>`: Deletes the specified instance.
- `all [<class name>]`: Prints the string representation of all instances, optionally filtered by class.
- `update <class name> <id> <attribute name> <attribute value>`: Updates the specified instance by adding or updating an attribute.

### Command Examples

#### Creating a New Instance
```bash
(hbnb) create User
<newly created User id>
```
## Authors
- badr bouzagui: <badrbouzagui@gmail.com>
- zouhair bajdouri: <zouhairbajdouri19@gmail.com>

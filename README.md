# AirBnB Clone - The Console

## Project Description

This project is part of the AirBnB clone series, where we are building a simplified version of the AirBnB web application. The main goal of this part of the project is to create a command interpreter (console) that will manage the objects of our application. The console is the core element of the project as it allows us to create, update, delete, and retrieve various instances of our data model.

The project is structured as follows

  - base_model.py: Contains the BaseModel class, which is the base class for all other models.

  - file_storage.py: Contains the FileStorage class, which handles serialization and deserialization of instances to and from a JSON file.
  
  - console.py: Contains the HBNBCommand class, which is the command interpreter.

  - __init__.py: Initializes the FileStorage instance.

  - Model files (user.py, state.py, city.py, amenity.py, place.py, review.py): Define specific models inheriting from BaseModel.

## Command Interpreter

## How to start the command interpreter
To start the command interpreter, follow there steps:
 - 1 Open your terminal or command prompt.
 - 2  
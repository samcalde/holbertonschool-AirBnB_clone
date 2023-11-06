# AirBnb Clone - Console

The project is a console whose main utility is to manipulate data for an AirBnb clone database.
It can create, store and retrieve diverse kinds of classes (BaseModel, User, State, Place, City, Amenity and Review) that are used to store the objects used in AirBnB. 

The program interaction is a command interpreter that implements the cmd module

# Command Interpreter

HOW TO START THE COMMAND INTERPRETER:

To start the Airbnb clone, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the project's directory.

4. Execute the file 'console.py'


HOW TO USE THE COMMAND INTERPRETER:

Once the file is executed, you will see a prompt '(hbnb)' on your terminal. From here,
you should enter the desired command with no initial space. Here is a list of the available ones, and their respective description:

- quit: 
Exit the program

- EOF: 
Exit the program

- help: 
Provides assistance related to the use of commands

- create: 
Creates an instance of the desired class, and returns the new instance's ID.
The class must exist in order to be created. (Ex: create Anything will return an error)
USE: 'create <class name>'

- show:
Prints the string representation of an instance based on the class name and id
USE: 'show <class name> <instance id>'

- destroy:
Deletes an instance based on the class name and id. 
USE: 'destroy <class name> <instance id>'

- all:
Prints string representation of all instances saved, or of a specific class
USE: 'all <class name>' / 'all'

- update:
Updates an instance based on the class name and id by adding or updating attribute.
Mind that id, created_at and updated_at attributes cant’ be updated
USE: 'update <class name> <id> <attribute name> <attribute value>'


# Examples

(hbnb) all MyModel
** class doesn't exist **

(hbnb) show BaseModel
** instance id missing **

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

(hbnb) create User
2dd6ef5c-467c-4f82-9521-a772ea7d84e9

(hbnb) all
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[User] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

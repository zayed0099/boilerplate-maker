import os

dir_input = str(input("Enter the directory for your boilerplate: "))
file_name = str(input("Enter the project name: "))
project_dir = os.chdir(dir_input)

os.mkdir(file_name)
os.chdir(file_name)

parent = "app"
children = ["core", "database", "routers", "schemas"]

for child in children:
    child_path = os.path.join(parent, child)

    os.makedirs(child_path, exist_ok=True)

    with open(os.path.join(child_path, "__init__.py"), "w") as file:
        pass

    if child == "core":
        

os.chdir("app")    
app_files = ["__init__.py", "main.py", "utils.py"]

for file in app_files:
    with open(file, "w") as f:
        f.write(f"# {f}")
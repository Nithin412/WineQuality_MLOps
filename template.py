import os


#creating a list of directories which are needed for the project
directory_names = [
                  os.path.join("Data","raw"),
                  os.path.join("Data", "processed" )
                  ,"Saved_Models",
                  "Notebooks",
                  "src",
                  "Data_Given"]

#iterating through the list and creating the directory using os.makedirs
for directory in directory_names:
    os.makedirs(directory, exist_ok = True)
    with open(os.path.join(directory,".gitkeep"), "w") as file:
        pass


files = ["dvc.yaml","params.yaml","gitignore", os.path.join("src", "__init__.py")]

for file in files:
    with open( file, "w") as x:
        pass


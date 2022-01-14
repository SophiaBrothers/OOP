
# creating an object called pipeline

class pipeline:
    p1 = "importer"
    
    def info(self):
        print("Use me to import files into Python")


    def locate(self):
        import os
        os.chdir('C:/Users/snfra/OneDrive/Documents/CREATED DATASETS')
        print("Path to file created")



#creating instances of pipeline

csv_pipe = pipeline()
json_pipe  = pipeline()

# accessing attribute
print(csv_pipe.p1)

# calling a method
csv_pipe.info()



# will later create a method for each type of instance
# ex.
#   def pull(self):
 #      import pandas as pd
        

# (if the instance object is {} , then do this,
#  else if, the instance object is {} , then do this,
#  else, pass)

This is a grocery store inventory system built by a group of 5 members, for assignment purpose.  
To run, please ensure Python 3.9 or above is installed. Run using the command below:  
```
python main.py
```

<b>Workflow</b>  
![workflow](src/PWP_workflow.png =300x)  
  
---  
  
<b>Guide to read txt files using Python</b>  
"column" refers to vertical, "row" refers to horizontal.   

`inventory.txt`  
column 0 : Code  
column 1 : Description  
column 2 : Category  
column 3 : Unit   
column 4 : Price  
column 5: Quantity  
column 6 : Minimum    


`userdata.txt`  
column 0 : Numbering  
column 1 : username  
column 2 : password  
column 3 : role   

---

To read data in a file, get every line of the file into an array, and split each element with "\t". Example code:  
```py
with open(file_dir, "r") as inventory_file:
    data_ls=inventory_file.readlines()
for ind, data in enumerate(data_ls):
    data_ls[ind]=data.rstrip().split("\t")
```

After getting all lines of data into an array, to call an element, call using the format `data_ls[row][column]` . Example:
```py
data_ls[0][1]
# To get 1st row 2nd column data
```
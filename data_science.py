import numpy as np

data_type = [('name','S15'), ('class',int),('height',float), ]
student_details = [('James', 5, 48.5),
                   ('Jules', 6, 52.0),
                   ('Arthur', 5, 45.0),
                   ('Nicole', 7, 60.5),
                   ('Isabelle', 6, 53.0),
                   ('Diana', 5, 47.5),
                   ('Paul', 6, 51.0),
                   ('Laura', 7, 59.0),]
students = np.array(student_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height:")
print(np.sort(students, order='height'))
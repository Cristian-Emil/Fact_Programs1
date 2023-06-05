class My_C_Manager(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with My_C_Manager("../Fisiere/Data.txt", "x") as f:
    f.write("Salut din fisierul My_C_Manager")

# ----------------------------------------------------------------------------------------------------------------------

# with MyCtxManager('./data.txt', 'r+') as f:
#     f.write('ceva')
#     f.write(' altceva')
#     f.seek(0)
#     data = f.read()
#     print(data)
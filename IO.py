import pickle

def Deserialize (path):
    binary_file = open(path, mode='rb')
    return pickle.load(binary_file)

def openCSV(path:str):
    file = open(path, "r")
    content = []
    for line in file.read().split('\n'):
        l = []
        for elem in line.split(','):
            try:
                l.append(eval(elem))
            except:
                l.append(elem)
        content.append(l)

    return content

def CSVToDataSet (csv:list):
    dataSet = []
    for elem in csv[1:]:
        dataSet.append([elem[:-1], elem[-1]])

    return dataSet

def showDataSet(dataset:list):
    for inputs, output in dataset:
        print(inputs, output)

def listToMaxIndice(l) -> int:
    return l.index(max(l))


if __name__ == "__main__":
    a = openCSV("StrikerDataSet.csv")
    [print(x) for x in a]
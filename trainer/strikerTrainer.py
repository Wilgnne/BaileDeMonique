
from NeuralNetwork import Brain, np
from trainerUtils import openCSV, CSVToDataSet, showDataSet, listToMaxIndice

inputs = 3
outputs = 5

class Avaliation:
    def __init__(self, brains:list, lenTest: int):
        self.brains = brains
        self.lenTest = lenTest
        self.points = [0 for i in range(len(brains))]
        self.attTest = 0
    
    def start (self):
        dataSet = CSVToDataSet(openCSV("/home/wilgnne/Data/Projects/Python/ANN-View/BaileDeMonique/trainer/StrikerDataSet.csv"))

        for inputs, output in dataSet:
            for i, brain in enumerate(self.brains):
                out = brain.think(np.array(inputs)).tolist()
                normalized = listToMaxIndice(out)

                if output == normalized:
                    self.points[i] += 1
            self.attTest += 1

        
        return self.points

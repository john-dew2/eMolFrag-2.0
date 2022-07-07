#That molecule class will contain the rdkit object, the name of the file it came from, as well as a list of 'equal other fragments'.
class Molecule:
    def __init__(self, rdkit_object, file_name):
        self.rdkit = rdkit_object
        self.filename = file_name
        self.equalFragments = []
    def getRDKitObject(self):
        return self.rdkit
    
    def getFileName(self):
        return self.filename
    
    def getEqualFragments(self):
        return self.equalFragments
        
    def setEqualFragments(self, listOfFragments):
        self.equalFragments = listOfFragments
        
    def toString(self):
        print(self.filename)
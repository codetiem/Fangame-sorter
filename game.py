class Game:
    def __init__(self, path):
        self.exe_path = path
        self.name : str = ""
        self.creator :str = ""
        self.rating : float = -1.0
        self.difficulty : float = -1.0
        self.tags : list = []

    def __str__(self):
        display = "="*20 + "\n" + "="*20
        display += f"\nName: {self.name}"
        display += f"\nCreator: {self.creator}"
        display += f"\nPath: {self.exe_path}"
        return display
    

class Game:
    def __init__(self, path):
        self.exe_path = path
        self.name : str = ""
        self.creator :set = set()
        self.rating : float = -1.0
        self.difficulty : float = -1.0
        self.tags : set = set()

    def __str__(self):
        creator_string = ""
        for creator in self.creator:
            creator_string += creator + ", "

        tags_string = ""
        for tags in self.tags:
            tags_string += tags + ", "

        creator_string = creator_string[:-2]
        tags_string = tags_string[:-2]

        display = "="*20
        display += f"\nName: {self.name}"
        display += f"\nCreator: {creator_string}"
        display += f"\nTags: {tags_string}"
        display += f"\nPath: {self.exe_path}"
        return display
    

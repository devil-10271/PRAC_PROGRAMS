class person:
    name=None
    position=None
    salary=None
    def info(self):
        print(f"{self.name} is a {self.position} with {self.salary} rupees")

per=person()
per.name='sahil'.capitalize()
per.position='malware developer'.title()
per.salary=100000
per.info()
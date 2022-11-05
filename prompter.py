import random
import yaml

# imports the yaml context
class config:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class prompter:

    def __init__(self):
 
        # imports the yaml content
        with open("config.yaml", 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        self.s = config(**data_loaded)
        self.d = {}

        # imports k wordlists as a dict in the format {file1:[word1, ..., wordn], ..., filek:[...]}
        self.word_lists = [i.strip() for i in list(self.s.inputfiles.split(","))]
        for wl in self.word_lists:
            with open(wl, 'r') as inputlist:
                self.d[wl]=[line.rstrip() for line in inputlist]

    def prompt(self):
        # joins a random word from each list and prints space delimited
        return " ".join([random.choice(v) for k,v in self.d.items()])

    def jsify(self):
        # prints a copy-pasteable js Object which defines the current state of the inputlists
        s = "var dict = " + str(self.d) + ";"
        s += "\nvar order = [" + str(", ".join(["\""+i.strip()+"\"" for i in list(self.s.inputfiles.split(","))]))+"];"
        print(s)


p = prompter()
print(p.prompt())
p.jsify()

    
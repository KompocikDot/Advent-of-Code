class Submarine:
    def __init__(self):
        self.depth = 0
        self.width = 0
        self.aim = 0
        self.read()
        self.calculate()
        self.cnt()

    def forward(self, numb: int) -> None:
        self.width += numb
        self.depth += self.aim * numb 

    def down(self, numb: int) -> None:
        self.aim += numb
    
    def up(self, numb: int) -> None:
        self.aim -= numb

    def cnt(self) -> None:
        print(self.depth * self.width)

    def read(self):
        with open("adventofcode\input.txt") as f:
            vals = f.readlines()
            self.instructions = [val.split(" ") for val in vals]
        
    def calculate(self):
        for tabl in self.instructions:
            if tabl[0] == "forward":
                self.forward(int(tabl[1]))
            elif tabl[0] == "down":
                self.down(int(tabl[1]))
            else:
                self.up(int(tabl[1]))

        self.cnt()
    
Submarine()
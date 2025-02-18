class Talking:
    def __init__(self, name):
        self.name = name
        self._count = 0    
        self._yes = 0        
        self._no = 0        

    def to_answer(self):
        if self._count % 2 == 0:
            self._yes += 1
            answer = "moore-moore"
        else:
            self._no += 1
            answer = "meow-meow"
        self._count += 1
        return answer

    def number_yes(self):
        return self._yes

    def number_no(self):
        return self._no



tk = Talking('Pussy')
print(tk.to_answer())  
print(tk.to_answer()) 
print(tk.to_answer())  
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')



tk = Talking('Pussy')
tkl = Talking('Barsik')
print(tk.to_answer())   
print(tkl.to_answer()) 
print(tkl.to_answer())  
print(tkl.to_answer())  
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tkl.name} says "yes" {tkl.number_yes()} times, "no" {tkl.number_no()} times')


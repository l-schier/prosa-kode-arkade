from abc import abstractmethod
import random


all_characters = []
current_characters = []

def main():
    global all_characters, current_characters
    all_characters = [Doc(), Grumpy(), Happy(), Sneezy()]
    #random.shuffle(all_characters)
    current_characters = [all_characters.pop(0), all_characters.pop()]
    
    
    running = True
    num_reacted = 0
    while running:
        anyReacted = False
        str = 'Current Characters: '
        for c in current_characters:
            str += c.name + " "
        print(str)
        #print('')
        if len(current_characters) == 0 or num_reacted >= 10:
            running = False

        for c in current_characters:
            if not c.reacted:
                print(f'char {c.name} is reacting')
                anyReacted = True
                print(c.react())
                break
        if not anyReacted:
            for c in current_characters:
                c.reacted = False
        num_reacted += 1


        
        
        
        

class dwarf():
    global all_characters, current_characters, running 
    name = ''
    reacted = False
    react_text = ''
    def __init__(self) -> None:
        pass
    
    def remove_self(self):
        running = False
        current_characters.remove(self)

    @abstractmethod
    def react(self):
        self.reacted = True

class Doc(dwarf):
    def __init__(self) -> None:
        self.name = 'Doc'
        super().__init__()
    def react(self):
        switch={
            'Grumpy': 'leaves because he cant stand Grumpy.',
            'Happy': 'takes Happy with him to bed.',
            'Sneezy': 'gets scared of Sneezy sneezing.'
        }
        self.reacted = True
        for c in current_characters:
            if c.name in switch:
                if len(all_characters) == 0:
                    self.react_text = f'{self.name} {switch.get(c.name)}'
                    if c.name != 'Sneezy':
                        c.remove_self()
                    self.remove_self()
                else:
                    current_characters.append(all_characters.pop())
                    self.react_text = f'Doc starts operating on {c.name} and calls {current_characters[-1].name} for help. \nUnfortunately {c.name} dies due to complications ;(('
                    c.remove_self()
                return self.react_text
        self.react_text = f'{self.name} is feeling lonely and goes to bed. leaving the room. The End'
        self.remove_self()
        return self.react_text

class Grumpy(dwarf):
    def __init__(self) -> None:
        self.name = 'Grumpy'
        super().__init__()
    def react(self):
        switch={
            'Doc': 'murders Doc.',
            'Happy': 'takes Happy with him to bed.',
            'Sneezy': 'screams loudly at Sneezy for sneezing'
        }
        self.reacted = True
        for c in current_characters:
            if c.name in switch:
                if len(all_characters) == 0:
                    self.react_text = f'{self.name} {switch.get(c.name)}'
                    if c.name != 'Sneezy' or c.name !=:
                        c.remove_self()
                    self.remove_self()
                else:
                    current_characters.append(all_characters.pop())
                    self.react_text = f'{self.name} calls  '
                    c.remove_self()
                return self.react_text
        self.react_text = f'{self.name} is feeling lonely and goes to bed. leaving the room. The End'
        self.remove_self()
        return self.react_text

class Happy(dwarf):
    def __init__(self) -> None:
        self.name = 'Happy'
        super().__init__()
    def react(self):
        return super().react()

class Sneezy(dwarf):
    def __init__(self) -> None:
        self.name = 'Sneezy'
        super().__init__()
    def react(self):
        return super().react()


    

if __name__ == '__main__':
    main()
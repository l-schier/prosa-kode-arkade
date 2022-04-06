from abc import abstractmethod
import random


all_characters = []
current_characters = []

def main():
    global all_characters, current_characters
    all_characters = [Doc(), Grumpy(), Happy(), Sneezy()]
    random.shuffle(all_characters)
    current_characters = [all_characters.pop(), all_characters.pop()]
    
    running = True
    num_reacted = 0
    while running:
        anyReacted = False
        if len(current_characters) == 0 or num_reacted >= 10:
            running = False
        str = 'Current Characters: '
        for c in current_characters:
            str += f'{c.name}'
        print(str)
        #print('')
        

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
    global all_characters, current_characters 
    name = ''
    reacted = False
    react_text = ''
    def __init__(self) -> None:
        pass
    
    def remove_self(self):
        current_characters.remove(self)

    @abstractmethod
    def react(self):
        self.reacted = True

class Doc(dwarf):
    def __init__(self) -> None:
        self.name = 'Doc'
        super().__init__()
    def react(self):
        global all_characters, current_characters
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
        self.react_text = f'{self.name} is feeling lonely and goes to bed. leaving the room. \nThe End'
        self.remove_self()
        return self.react_text

class Grumpy(dwarf):
    def __init__(self) -> None:
        self.name = 'Grumpy'
        super().__init__()
    def react(self):
        global all_characters, current_characters
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
                    if c.name == 'Happy':
                        c.remove_self()
                        self.remove_self()
                    if c.name == 'Doc':
                        c.remove_self()                    
                else:
                    if c.name == 'Sneezy':
                        current_characters.append(all_characters.pop())
                        self.react_text = f'{current_characters[-1].name} hears {c.name} screaming and comes running to see what is happening.'
                    if c.name == 'Doc':
                        self.react_text = f'{self.name} {switch.get(c.name)}'
                        c.remove_self()
                    if c.name == 'Happy':
                        self.react_text = f'{self.name} {switch.get(c.name)}'
                        c.remove_self()
                        self.remove_self()
                return self.react_text
        self.react_text = f'{self.name} is feeling lonely and goes to bed. leaving the room. \nThe End'
        self.remove_self()
        return self.react_text

class Happy(dwarf):
    def __init__(self) -> None:
        self.name = 'Happy'
        super().__init__()
    def react(self):
        global all_characters, current_characters
        switch={
            'Grumpy': 'Takes Grumpy to bed.',
            'Doc': 'Takes Doc to bed.',
            'Sneezy': 'tries to help Sneezy with stopping sneezing. to no end.'
        }
        self.reacted = True
        
        for c in current_characters:
            if c.name in switch:
                if len(all_characters) == 0:
                    self.react_text = f'{self.name} brings everyone to bed! and is very happy to do so!. \nThe End'
                    current_characters = []
                    return self.react_text
                else:
                    self.react_text = f'{self.name} {switch.get(c.name)}'
                    if c.name == 'Sneezy':
                        for ca in all_characters:
                            if ca.name == 'Doc':
                                self.react_text = f'{self.name} calls {ca.name} to help with fixing {c.name}\'s sneezing.'
                                current_characters.append(ca)
                                all_characters.remove(ca)
                                return self.react_text
                            
                        self.react_text = f'{self.name} {switch.get(c.name)}'
                    return self.react_text
        
        self.react_text = f'{self.name} is not really so happy, and now he is lonely too. So he decides to end this... \nThe end.'
        self.remove_self()
        return self.react_text

class Sneezy(dwarf):
    def __init__(self) -> None:
        self.name = 'Sneezy'
        super().__init__()
    def react(self):
        global all_characters, current_characters
        switch={
            'Grumpy': '',
            'Happy': '',
            'Doc': ''
        }
        self.reacted = True
        
        for c in current_characters:
            if c.name in switch:
                if len(all_characters) == 0:
                    self.react_text = f'{self.name} sneezes so hard he blows the house up. \nThe End'
                    current_characters = []
                    return self.react_text
                else:
                    self.react_text = f'{self.name} sneezes so hard he blows the house up. \n{c.name} is the last one alive'
                    current_characters = [c]
                    return self.react_text

        self.react_text = f'{self.name} sneezes so hard he flies hight up into the sky, and falling down breaking his neck. \nThe End'
        self.remove_self()
        return self.react_text
 

if __name__ == '__main__':
    num_times = int(input(f'Input amount of times to run the story: '))
    print('====================================================')
    for i in range(num_times):
        main()
    print('====================================================')
    print(f'Finished running {num_times} times.')

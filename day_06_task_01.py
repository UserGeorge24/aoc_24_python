import re
class lcl_guard:
    
    file = list()
    guard_vertical   = int()
    guard_horizontal = int()
    find_obstacle = re.compile('[\#]')

    @staticmethod
    def count_x():
        find_x = re.compile('[X]')
        sum_of_x = int()
        for i in lcl_guard.file:
            if guard_location := find_x.findall(i):
                sum_of_x += len(guard_location)  
        return sum_of_x

    @staticmethod
    def set_initial_coord():
        find_guard = re.compile('[\^]')
        for index, i in enumerate(lcl_guard.file):
            if guard_location := find_guard.search(i):
                lcl_guard.guard_vertical = index
                lcl_guard.guard_horizontal = guard_location.start()
                break        
    
    @staticmethod
    def search_right():
        
        new_line = str()
        
        curr_line = lcl_guard.file[lcl_guard.guard_vertical]
        
        for index, i in enumerate(curr_line[lcl_guard.guard_horizontal:]):
            
            if i != '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical]
                new_line = new_line[:lcl_guard.guard_horizontal+index] + 'X' + new_line[lcl_guard.guard_horizontal+index+1:]
                lcl_guard.file[lcl_guard.guard_vertical] = new_line
            elif i == '#':
                lcl_guard.guard_horizontal += index - 1
                return

        raise('EndOfStory')    
    
    @staticmethod
    def search_left():
        
        new_line = str()
        
        curr_line = lcl_guard.file[lcl_guard.guard_vertical]
        
        for index, i in enumerate(curr_line[lcl_guard.guard_horizontal::-1]):
            
            if i != '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical]
                new_line = new_line[:lcl_guard.guard_horizontal-index] + 'X' + new_line[lcl_guard.guard_horizontal-index+1:]
                lcl_guard.file[lcl_guard.guard_vertical] = new_line
            elif i == '#':
                lcl_guard.guard_horizontal -= index - 1
                return

        raise('EndOfStory')
    
    @staticmethod
    def down_mod_line(index):
        new_line = lcl_guard.file[lcl_guard.guard_vertical+index]
        new_line = new_line[:lcl_guard.guard_horizontal] + 'X' + new_line[lcl_guard.guard_horizontal+1:]
        lcl_guard.file[lcl_guard.guard_vertical+index] = new_line
    
    @staticmethod
    def search_down():
        
        for index, i in enumerate(lcl_guard.file[lcl_guard.guard_vertical:]):
            
            if i[lcl_guard.guard_horizontal:lcl_guard.guard_horizontal+1] == '#':
                lcl_guard.guard_vertical   += index - 1
                return
            else:
                lcl_guard.down_mod_line(index)                
        raise('EndOfStory')
    
    @staticmethod
    def up_mod_line(index):
        
        new_line = str()
        new_line = lcl_guard.file[lcl_guard.guard_vertical - index]               
        new_line = new_line[:lcl_guard.guard_horizontal] + 'X' + new_line[lcl_guard.guard_horizontal+1:]
        lcl_guard.file[lcl_guard.guard_vertical - index] = new_line        
    
    @staticmethod
    def search_up():
        
        for index, i in enumerate(lcl_guard.file[lcl_guard.guard_vertical-1::-1]):

            lcl_guard.up_mod_line(index)
            
            if i[lcl_guard.guard_horizontal:lcl_guard.guard_horizontal+1] == '#': 
                lcl_guard.guard_vertical   -= index
                return
        raise('EndOfStory')
    
start_time = time.time()

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_06.txt"
lcl_guard.file = [ line.strip() for line in open(file_path,'r').readlines() ]
lcl_guard.set_initial_coord()

while True:
    try:    
        lcl_guard.search_up() 
        lcl_guard.search_right()  
        lcl_guard.search_down()
        lcl_guard.search_left()
    except: break

print(lcl_guard.count_x())

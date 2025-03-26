import re

class EndOfStory(Exception):
    pass
class DoFrombegin(Exception):
    pass

class lcl_guard:
    
    file                 = list()
    guard_vertical       = int()
    guard_horizontal     = int()
    guard_vertical_ori   = int()
    guard_horizontal_ori = int()
    find_obstacle        = re.compile('[\#]')
    loop_active          = bool()
    loop_counter = int()
    right_coords = list()
    visited_obstacles = list()
        
    @staticmethod
    def set_initial_coord():
        find_guard = re.compile('[\^]')
        for index, i in enumerate(lcl_guard.file):
            if guard_location := find_guard.search(i):
                lcl_guard.guard_vertical   = lcl_guard.guard_vertical_ori   = index
                lcl_guard.guard_horizontal = lcl_guard.guard_horizontal_ori = guard_location.start()
                break        
    
    @staticmethod
    def right_mod_line(index, value):
        new_line = str()

        result = [item for item in lcl_guard.visited_obstacles if item == tuple((str(int(lcl_guard.guard_horizontal+index)),str(lcl_guard.guard_vertical))) ]
        
        if result and value != '.':
            return False
        else:
            if value == '.':
                lcl_guard.remove_last_obstacle()
            elif value == '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical]
                new_line = new_line[:lcl_guard.guard_horizontal+index] + value + new_line[lcl_guard.guard_horizontal+index+1:]
                lcl_guard.file[lcl_guard.guard_vertical] = new_line
                lcl_guard.visited_obstacles.append( tuple((str(int(lcl_guard.guard_horizontal+index)),str(lcl_guard.guard_vertical))))
            return True
            
    @staticmethod
    def search_right():
        
        curr_line = lcl_guard.file[lcl_guard.guard_vertical]
        
        lcl_guard.right_coords.append(str(lcl_guard.guard_horizontal)+str(lcl_guard.guard_vertical))
                
        for i in curr_line[lcl_guard.guard_horizontal+1:]:
            
            if i != '#' and lcl_guard.loop_active == False and curr_line[lcl_guard.guard_horizontal+1] != '#':
                if lcl_guard.right_mod_line(1,'#'):
                    lcl_guard.find_loop('down')
            elif i == '#':
                return
            lcl_guard.guard_horizontal += 1
            
        raise EndOfStory()
    
    @staticmethod
    def left_mod_line(index,value):

        new_line = str()

        result = [item for item in lcl_guard.visited_obstacles if item == tuple((str(int(lcl_guard.guard_horizontal-index)),str(lcl_guard.guard_vertical))) ]
        
        if result and value != '.':
            return False
        else:
            if value == '.':
                lcl_guard.remove_last_obstacle()
            elif value == '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical]
                new_line = new_line[:lcl_guard.guard_horizontal-index] + value + new_line[lcl_guard.guard_horizontal-index+1:]
                lcl_guard.file[lcl_guard.guard_vertical] = new_line
                lcl_guard.visited_obstacles.append( tuple((str(int(lcl_guard.guard_horizontal-index)),str(lcl_guard.guard_vertical))))
        return True
    
    @staticmethod
    def search_left():
        
        curr_line = lcl_guard.file[lcl_guard.guard_vertical]

        for i in curr_line[lcl_guard.guard_horizontal-1::-1]:
            
            if i != '#' and lcl_guard.loop_active == False:
                if lcl_guard.left_mod_line(1,'#'):
                    lcl_guard.find_loop('up')
            elif i == '#':
                return
            lcl_guard.guard_horizontal -= 1

        raise EndOfStory()
    
    @staticmethod
    def down_mod_line(index,value):

        result = [item for item in lcl_guard.visited_obstacles if item == tuple((str(lcl_guard.guard_horizontal),str(int(lcl_guard.guard_vertical+index)))) ]
        
        if result and value != '.': 
            return False
        else:            
            if value == '.':
                lcl_guard.remove_last_obstacle()
            elif value == '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical+index]
                new_line = new_line[:lcl_guard.guard_horizontal] + value + new_line[lcl_guard.guard_horizontal+1:]
                lcl_guard.file[lcl_guard.guard_vertical+index] = new_line
                lcl_guard.visited_obstacles.append(tuple((str(lcl_guard.guard_horizontal),str(int(lcl_guard.guard_vertical+index)))))
            return True
            
    @staticmethod
    def search_down():

        pass
        
        for i in lcl_guard.file[lcl_guard.guard_vertical+1:]:
            
            if i[lcl_guard.guard_horizontal:lcl_guard.guard_horizontal+1] == '#':
                return
            elif lcl_guard.loop_active == False:
                if lcl_guard.down_mod_line(1,'#'):
                    lcl_guard.find_loop('left')
            lcl_guard.guard_vertical += 1
            
        raise EndOfStory()
    
    @staticmethod
    def up_mod_line(index,value):
        
        new_line = str()
        
        result = [item for item in lcl_guard.visited_obstacles if item == tuple((str(lcl_guard.guard_horizontal),str(int(lcl_guard.guard_vertical - index)))) ]
        
        if result and value != '.': 
            return False
        else:    
            if value == '.':
                lcl_guard.remove_last_obstacle()
            elif value == '#':
                new_line = lcl_guard.file[lcl_guard.guard_vertical - index]
                new_line = new_line[:lcl_guard.guard_horizontal] + value + new_line[lcl_guard.guard_horizontal+1:]
                lcl_guard.file[lcl_guard.guard_vertical - index] = new_line      
                lcl_guard.visited_obstacles.append( tuple((str(lcl_guard.guard_horizontal),str(int(lcl_guard.guard_vertical - index))) ))
            
            return True 

    @staticmethod
    def remove_last_obstacle():
        length = len(lcl_guard.visited_obstacles) - 1
        obstacle_col = int(lcl_guard.visited_obstacles[length][0])
        obstacle_row = int(lcl_guard.visited_obstacles[length][1])
        new_line = lcl_guard.file[obstacle_row]
        new_line = new_line[:obstacle_col] + '.' + new_line[obstacle_col+1:]
        lcl_guard.file[obstacle_row] = new_line
    
    @staticmethod
    def search_up():

        pass

        for i in lcl_guard.file[lcl_guard.guard_vertical-1::-1]:
                       
            if i[lcl_guard.guard_horizontal:lcl_guard.guard_horizontal+1] == '#': 
                return
            elif lcl_guard.loop_active == False:
                if lcl_guard.up_mod_line(1,'#'):
                    lcl_guard.find_loop('right')
#                    lcl_guard.up_mod_line(1,'.')
            lcl_guard.guard_vertical -= 1
        
        raise EndOfStory()
    
    @staticmethod
    def find_loop(direction):
        lcl_guard.loop_active = True
        
        try:        
            if direction == 'up':
                while True:
                    lcl_guard.search_up() 
                    if str(lcl_guard.guard_horizontal)+str(lcl_guard.guard_vertical) in lcl_guard.right_coords:
                        lcl_guard.loop_counter += 1  
                        print(lcl_guard.loop_counter)  
                        break                    
                    lcl_guard.search_right()  
                    lcl_guard.search_down()
                    lcl_guard.search_left()        

            elif direction == 'right':
                while True:
                    if str(lcl_guard.guard_horizontal)+str(lcl_guard.guard_vertical) in lcl_guard.right_coords:
                        lcl_guard.loop_counter += 1  
                        print(lcl_guard.loop_counter)  
                        break
                    lcl_guard.search_right()  
                    lcl_guard.search_down()
                    lcl_guard.search_left()
                    lcl_guard.search_up() 
            elif direction == 'down':
                while True:
                    lcl_guard.search_down()
                    lcl_guard.search_left()
                    lcl_guard.search_up()
                    if str(lcl_guard.guard_horizontal)+str(lcl_guard.guard_vertical) in lcl_guard.right_coords:
                        lcl_guard.loop_counter += 1  
                        print(lcl_guard.loop_counter)  
                        break
                    lcl_guard.search_right()
            else:
                while True:
                    lcl_guard.search_left()
                    lcl_guard.search_up()
                    if str(lcl_guard.guard_horizontal)+str(lcl_guard.guard_vertical) in lcl_guard.right_coords:
                        lcl_guard.loop_counter += 1  
                        print(lcl_guard.loop_counter)  
                        break
                    lcl_guard.search_right()
                    lcl_guard.search_down()
        except EndOfStory: pass

        if direction == 'right':
            lcl_guard.up_mod_line(1,'.')
        elif direction == 'left':
            lcl_guard.down_mod_line(1,'.')
        elif direction == 'up':
            lcl_guard.left_mod_line(1,'.')
        elif direction == 'down':
            lcl_guard.right_mod_line(1,'.')

        lcl_guard.guard_horizontal = lcl_guard.guard_horizontal_ori
        lcl_guard.guard_vertical   = lcl_guard.guard_vertical_ori
        lcl_guard.loop_active = False
        lcl_guard.right_coords = []
            
        raise DoFrombegin()
    
file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_06.txt"
lcl_guard.file = [ line.strip() for line in open(file_path,'r').readlines() ]
lcl_guard.set_initial_coord()

while True:
    try:    
        lcl_guard.search_up() 
        lcl_guard.search_right()  
        lcl_guard.search_down()
        lcl_guard.search_left()
    except DoFrombegin: continue
    except EndOfStory: break
    
print('Number of loops ' + str(lcl_guard.loop_counter))

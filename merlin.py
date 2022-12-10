
row_1 = '~ * ~'
row_2 = '~ ~ ~'
row_3 = '~ * ~'
all_buttons_pressed = '884'
"""
row_1 = input()
row_2 = input()
row_3 = input()
all_buttons_pressed = input()
"""

class Merlin:
    __grid = list()
    __SOLVED_GRID = [['1', '1', '1'], 
                     ['1', '0', '1'],
                     ['1', '1', '1']]

    def find_button_to_solve(self):
        button_to_solve = ''
        for b in '123456789':
            self.__press_button(b)
            if self.__grid == self.__SOLVED_GRID:
                button_to_solve = b
                break
            else: self.__press_button(b)
        return button_to_solve

    def press_buttons(self, buttons):
        for b in buttons:
            self.__press_button(b)

    # Not supported in Codingame. Needs Python 3.10
    """def __press_button(self, button):
        match button:
            case '1': self.__invert_cells('1245')
            case '2': self.__invert_cells('123')
            case '3': self.__invert_cells('2356')
            case '4': self.__invert_cells('147')
            case '5': self.__invert_cells('24568')
            case '6': self.__invert_cells('369')
            case '7': self.__invert_cells('4578')
            case '8': self.__invert_cells('789')
            case '9': self.__invert_cells('5689')"""
    
    def __press_button(self, button):
        if button == '1': self.__invert_cells('1245')
        elif button == '2': self.__invert_cells('123')
        elif button == '3': self.__invert_cells('2356')
        elif button == '4': self.__invert_cells('147')
        elif button == '5': self.__invert_cells('24568')
        elif button == '6': self.__invert_cells('369')
        elif button == '7': self.__invert_cells('4578')
        elif button == '8': self.__invert_cells('789')
        elif button == '9': self.__invert_cells('5689')    

    def __invert_cells(self, cells):
        for cell in cells:
            x = 0
            if cell in '123': x = 0
            elif cell in '456': x = 1
            elif cell in '789': x = 2

            y = 0
            if cell in '147': y = 0
            elif cell in '258': y = 1
            elif cell in '369': y = 2

            self.__invert_cell(x, y)

    def __invert_cell(self, row, col):
        self.__grid[row][col] = '1' if self.__grid[row][col] == '0' else '0'

    def __init__(self, *rows):
        for row in rows:
            row = row.replace('*', '1').replace('~', '0').split()
            self.__grid.append(row)

    def __str__(self):
        sgrid = ''
        for row in self.__grid:
            for cell in row: sgrid += cell + ' '
            sgrid += '\n'
        return sgrid

m = Merlin(row_1, row_2, row_3)
m.press_buttons(all_buttons_pressed)
print(m.find_button_to_solve())

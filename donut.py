import curses
import random
import time

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%&*"

class HackerMatrix:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.init_screen()
        self.run()
    
    def init_screen(self):
        curses.curs_set(0)
        self.stdscr.nodelay(1)
        self.stdscr.timeout(50)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.sh, self.sw = self.stdscr.getmaxyx()
        self.columns = [random.randint(-self.sh, 0) for _ in range(self.sw)]
    
    def run(self):
        while True:
            self.stdscr.clear()
            for i in range(self.sw):
                if self.columns[i] < self.sh and random.random() > 0.97:
                    self.columns[i] += 1
                elif self.columns[i] > 0 and random.random() > 0.98:
                    self.columns[i] -= 1
                
                for j in range(self.columns[i]):
                    char = random.choice(chars)
                    attr = curses.color_pair(1) | (curses.A_BOLD if j == self.columns[i] - 1 else 0)
                    self.stdscr.addstr(j, i, char, attr)
            
            self.stdscr.refresh()
            if self.stdscr.getch() == 27: 
                break

def main():
    curses.wrapper(HackerMatrix)

if __name__ == "__main__":
    main()

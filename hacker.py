import curses
import random
import time

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%&*"
commands = [
    "ACCESS GRANTED...",
    "DECRYPTING DATA...",
    "FINDING BACKDOOR...",
    "HACKING MAINFRAME...",
    "DISABLING FIREWALL...",
    "OVERRIDING SECURITY PROTOCOL..."
]

class HackerSimulator:
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
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.sh, self.sw = self.stdscr.getmaxyx()
        self.columns = [random.randint(-self.sh, 0) for _ in range(self.sw)]
    
    def draw_matrix_effect(self):
        for i in range(self.sw):
            if self.columns[i] < self.sh and random.random() > 0.95:
                self.columns[i] += 1
            elif self.columns[i] > 0 and random.random() > 0.98:
                self.columns[i] -= 1
            
            for j in range(self.columns[i]):
                char = random.choice(chars)
                color = random.choice([1, 2, 3])  # Màu sắc ngẫu nhiên
                attr = curses.color_pair(color) | (curses.A_BOLD if j == self.columns[i] - 1 else 0)
                self.stdscr.addstr(j, i, char, attr)
    
    def draw_hacker_commands(self):
        if random.random() > 0.98:
            cmd = random.choice(commands)
            x = random.randint(0, self.sw - len(cmd) - 1)
            y = random.randint(0, self.sh - 1)
            self.stdscr.addstr(y, x, cmd, curses.color_pair(2) | curses.A_BOLD)
    
    def run(self):
        while True:
            self.stdscr.clear()
            self.draw_matrix_effect()
            self.draw_hacker_commands()
            self.stdscr.refresh()
            if self.stdscr.getch() == 27:  # ESC để thoát
                break

def main():
    curses.wrapper(HackerSimulator)

if __name__ == "__main__":
    main()

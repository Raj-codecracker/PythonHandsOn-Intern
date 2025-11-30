import pygame
import sys
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 700
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My X O Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (200, 30, 30) 
size = 200  
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
player = "X"
cell_font = pygame.font.Font(None, 100)
status_font = pygame.font.Font(None, 40)
winner_font = pygame.font.Font(None, 72)
run = True
def find_winner_and_line(bd):
    for r in range(3):
        if bd[r][0] == bd[r][1] == bd[r][2] != "":
            winner = bd[r][0]
            start = (0 * size + size // 2, r * size + size // 2)
            end   = (2 * size + size // 2, r * size + size // 2)
            return winner, start, end
    for c in range(3):
        if bd[0][c] == bd[1][c] == bd[2][c] != "":
            winner = bd[0][c]
            start = (c * size + size // 2, 0 * size + size // 2)
            end   = (c * size + size // 2, 2 * size + size // 2)
            return winner, start, end
    if bd[0][0] == bd[1][1] == bd[2][2] != "":
        winner = bd[0][0]
        start = (0 * size + size // 2, 0 * size + size // 2)
        end   = (2 * size + size // 2, 2 * size + size // 2)
        return winner, start, end
    if bd[0][2] == bd[1][1] == bd[2][0] != "":
        winner = bd[0][2]
        start = (2 * size + size // 2, 0 * size + size // 2)
        end   = (0 * size + size // 2, 2 * size + size // 2)
        return winner, start, end
    if all(all(cell != "" for cell in row) for row in bd):
        return "Draw", None, None
    return None, None, None
winner = None
win_line = None 
while run:
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (size, 0), (size, size * 3), 5)
    pygame.draw.line(screen, BLACK, (size * 2, 0), (size * 2, size * 3), 5)
    pygame.draw.line(screen, BLACK, (0, size), (size * 3, size), 5)
    pygame.draw.line(screen, BLACK, (0, size * 2), (size * 3, size * 2), 5)
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = cell_font.render(board[row][col], True, BLACK)
                text_rect = text.get_rect(center=(col * size + size // 2, row * size + size // 2))
                screen.blit(text, text_rect)
    if not winner:
        winner, start_pos, end_pos = find_winner_and_line(board)
        if winner and winner != "Draw":
            win_line = (start_pos, end_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not winner:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < size*3 and mouse_y < size*3:
                row = mouse_y // size
                col = mouse_x // size
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
    if win_line:
        s, e = win_line
        pygame.draw.line(screen, WHITE, s, e, 26) 
        pygame.draw.line(screen, HIGHLIGHT, s, e, 10)
    if winner:
        if winner == "Draw":
            status_text = "Game Draw!"
            status_surface = status_font.render(status_text, True, BLACK)
            screen.blit(status_surface, (10, size*3 + 10))
            center_surf = winner_font.render("Game Draw!", True, BLACK)
            center_rect = center_surf.get_rect(center=(size*3//2, size*3//2))
            screen.blit(center_surf, center_rect)
        else:
            status_text = f"Player {winner} Wins!"
            status_surface = status_font.render(status_text, True, HIGHLIGHT)
            screen.blit(status_surface, (10, size*3 + 10))
            winner_surface = winner_font.render(f"Player {winner} Won!", True, HIGHLIGHT)
            winner_rect = winner_surface.get_rect(center=(size*3//2, size*3//2))
            padding_x, padding_y = 20, 10
            bg_rect = pygame.Rect(
                winner_rect.left - padding_x,
                winner_rect.top - padding_y,
                winner_rect.width + padding_x*2,
                winner_rect.height + padding_y*2
            )
            pygame.draw.rect(screen, WHITE, bg_rect)
            screen.blit(winner_surface, winner_rect)
    else:
        status_text = f"Player {player}'s turn"
        status_surface = status_font.render(status_text, True, BLACK)
        status_rect = status_surface.get_rect(center=(size*3//2, size*3 + 30))
        screen.blit(status_surface, status_rect)
    pygame.display.update()
pygame.quit()
sys.exit()

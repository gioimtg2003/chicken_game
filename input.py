import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cấu hình cửa sổ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Input Text')

# Font
font = pygame.font.Font(None, 32)

# Hàm vẽ văn bản
def draw_text(surface, text, x, y):
    text_surface = font.render(text, True, BLACK)
    surface.blit(text_surface, (x, y))

# Hàm vẽ button
def draw_button(surface, text, x, y, width, height, color):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(surface, text, x + 10, y + 10)

# Kiểm tra xem điểm có nằm trong button không
def is_mouse_over_button(mouse_pos, button_rect):
    return button_rect.collidepoint(mouse_pos)

# Biến lưu trữ văn bản đầu vào
input_text_value = ""

# Xử lý sự kiện khi nhấn nút
def handle_button_click():
    print("Button clicked! Entered text:", input_text_value)

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if is_mouse_over_button(mouse_pos, button_rect):
                handle_button_click()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text_value = input_text_value[:-1]
            elif event.key == pygame.K_RETURN:
                handle_button_click()
            else:
                input_text_value += event.unicode

    # Vẽ ô nhập văn bản
    pygame.draw.rect(screen, BLACK, (300, 200, 200, 40), 2)
    draw_text(screen, input_text_value, 305, 205)

    # Vẽ button
    button_rect = pygame.Rect(300, 300, 200, 50)
    draw_button(screen, "Click Me", 300, 300, 200, 50, BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()

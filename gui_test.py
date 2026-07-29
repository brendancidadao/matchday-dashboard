# gui_test.py
import sys
import pygame
from mock_data import MOCK_MATCH

# Initialize Pygame engine
pygame.init()

# Target screen resolution (2.8" SPI display target)
WIDTH, HEIGHT = 320, 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MatchDay Pi Dashboard - Preview")

# Color Palette (RGB)
BG_COLOR = (18, 18, 18)        # Dark mode base
TEXT_WHITE = (240, 240, 240)
ACCENT_GREEN = (0, 230, 118)   # Live badge color
CARD_BG = (30, 30, 30)        # Scorecard box

# Fonts
font_large = pygame.font.SysFont("Arial", 36, bold=True)
font_small = pygame.font.SysFont("Arial", 16)

clock = pygame.time.Clock()

# --- MAIN RENDER LOOP ---
running = True
while running:
    # 1. Input Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls simulate physical rotary/button inputs
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:         # Home team goal
                MOCK_MATCH["home_score"] += 1
            elif event.key == pygame.K_DOWN:     # Away team goal
                MOCK_MATCH["away_score"] += 1
            elif event.key == pygame.K_RIGHT:    # Advance match minute
                MOCK_MATCH["minute"] += 1

    # 2. Render Background
    screen.fill(BG_COLOR)

    # 3. Draw Header (Competition)
    comp_text = font_small.render(
        MOCK_MATCH["competition"].upper(), True, (150, 150, 150)
    )
    screen.blit(comp_text, (WIDTH // 2 - comp_text.get_width() // 2, 15))

    # 4. Draw Scorecard Container
    pygame.draw.rect(screen, CARD_BG, (20, 45, 280, 120), border_radius=10)

    # 5. Render Score ("ARS   2 - 1   MCI")
    score_str = f"{MOCK_MATCH['home_team']}   {MOCK_MATCH['home_score']} - {MOCK_MATCH['away_score']}   {MOCK_MATCH['away_team']}"
    score_surface = font_large.render(score_str, True, TEXT_WHITE)
    screen.blit(
        score_surface, (WIDTH // 2 - score_surface.get_width() // 2, 80)
    )

    # 6. Render Live Minute Badge
    minute_str = f"● {MOCK_MATCH['minute']}' LIVE"
    minute_surface = font_small.render(minute_str, True, ACCENT_GREEN)
    screen.blit(
        minute_surface, (WIDTH // 2 - minute_surface.get_width() // 2, 130)
    )

    # 7. Render Navigation Hint
    hint_text = font_small.render(
        "[UP/DOWN: Goal]  [RIGHT: +1 Min]", True, (100, 100, 100)
    )
    screen.blit(
        hint_text, (WIDTH // 2 - hint_text.get_width() // 2, 200)
    )

    # 8. Refresh Display & Cap Framerate to 30 FPS
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
import pygame
import sys
import time
import random

pygame.init()
pygame.mixer.init()

# ================= MUSIC =================
pygame.mixer.music.load("assets/vecna_clock.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# ================= FULLSCREEN =================
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Personality Quiz")

clock = pygame.time.Clock()

# ================= COLORS =================
BLACK = (10, 10, 10)
RED = (200, 0, 0)
WHITE = (240, 240, 240)

# ================= FONTS =================
title_font = pygame.font.Font("assets/st_font.ttf", int(HEIGHT * 0.08))
text_font = pygame.font.Font("assets/st_font.ttf", int(HEIGHT * 0.036))
small_font = pygame.font.Font("assets/st_font.ttf", int(HEIGHT * 0.03))

# ================= QUESTIONS =================
questions = [
    {"q": "How do you usually make decisions?", "L": "Based on feelings", "R": "Based on logic"},
    {"q": "In a group project, you prefer to…", "L": "Lead the work", "R": "Support quietly"},
    {"q": "When stressed, you usually…", "L": "Talk it out", "R": "Keep it to yourself"},
    {"q": "You learn best by…", "L": "Trying things hands-on", "R": "Observing and thinking"},
    {"q": "People describe you as…", "L": "Bold", "R": "Thoughtful"},
    {"q": "You trust people who are…", "L": "Emotionally open", "R": "Consistent and reliable"},
    {"q": "When plans fail, you…", "L": "Adapt instantly", "R": "Recalculate carefully"},
    {"q": "Your biggest strength is your…", "L": "Confidence", "R": "Awareness"},
    {"q": "You prefer working…", "L": "With people", "R": "Alone"},
    {"q": "You feel fulfilled when you…", "L": "Help others", "R": "Achieve goals"}
]

# ================= CHARACTERS =================
characters = ["Eleven","Mike","Dustin","Lucas","Will","Max","Steve","Nancy","Jonathan","Erica","Vecna"]
scores = {c: 0 for c in characters}

option_map = [
    {"L": ["Eleven","Max"], "R": ["Nancy","Jonathan"]},
    {"L": ["Steve","Erica"], "R": ["Will","Jonathan"]},
    {"L": ["Mike","Steve"], "R": ["Will","Jonathan"]},
    {"L": ["Eleven","Max"], "R": ["Dustin","Nancy"]},
    {"L": ["Erica","Lucas"], "R": ["Will","Jonathan"]},
    {"L": ["Mike","Steve"], "R": ["Nancy"]},
    {"L": ["Max","Eleven"], "R": ["Will","Jonathan"]},
    {"L": ["Erica","Max"], "R": ["Will"]},
    {"L": ["Dustin","Mike"], "R": ["Jonathan"]},
    {"L": ["Mike","Steve"], "R": ["Vecna","Nancy"]}
]

descriptions = {
    "Eleven": "Fierce, loyal, and strong from within.",
    "Mike": "Determined, compassionate and courageous.",
    "Dustin": "Curious, intelligent, and wholesome.",
    "Lucas": "Practical, brave, and logical.",
    "Will": "Sensitive, intuitive, and observant.",
    "Max": "Independent, tough, resilient and sarcastic.",
    "Steve": "Protective, confident, and reliable.",
    "Nancy": "Focused, intelligent, and determined.",
    "Jonathan": "Thoughtful, creative and enthusiastic.",
    "Erica": "Bold, fearless, and sharp.",
    "Vecna": "Strategic, intense, and powerful."
}


# ================= STATE =================
q_index = 0
show_result = False
result_char = ""
lightning_alpha = 0
game_started = False

# ================= LOOP =================
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # START SCREEN
        if not game_started and event.type == pygame.KEYDOWN:
            game_started = True

        # ANSWER USING LEFT / RIGHT KEYS
        if game_started and not show_result and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for c in option_map[q_index]["L"]:
                    scores[c] += 1
                q_index += 1
                time.sleep(0.2)

            elif event.key == pygame.K_RIGHT:
                for c in option_map[q_index]["R"]:
                    scores[c] += 1
                q_index += 1
                time.sleep(0.2)

            if q_index >= len(questions):
                show_result = True
                result_char = max(scores, key=scores.get)

        if show_result and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # ================= START PAGE =================
    if not game_started:
        title = title_font.render("STRANGER THINGS", True, RED)
        sub = text_font.render("Personality Test", True, WHITE)
        hint = small_font.render("Press ANY key to start", True, RED)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT*0.35))
        screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT*0.48))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT*0.62))

        pygame.display.update()
        continue

    # ================= LIGHTNING EFFECT =================
    if random.randint(0, 90) == 0:
        lightning_alpha = random.randint(140, 220)

    if lightning_alpha > 0:
        flash = pygame.Surface((WIDTH, HEIGHT))
        flash.set_alpha(lightning_alpha)
        flash.fill(RED)
        screen.blit(flash, (0, 0))
        lightning_alpha -= 12

    # ================= DRAW =================
    if not show_result:
        title = title_font.render("PERSONALITY TEST", True, RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT*0.1))

        q = questions[q_index]
        qt = text_font.render(q["q"], True, WHITE)
        screen.blit(qt, (WIDTH//2 - qt.get_width()//2, HEIGHT*0.35))

        y = HEIGHT * 0.72

        left_text = text_font.render(q["L"], True, RED)
        screen.blit(left_text, (WIDTH*0.05, y))

        right_text = text_font.render(q["R"], True, RED)
        screen.blit(right_text, (WIDTH*0.95 - right_text.get_width(), y))

    else:
        t = title_font.render("YOU ARE", True, WHITE)
        n = title_font.render(result_char.upper(), True, RED)
        d = small_font.render(descriptions[result_char], True, WHITE)
        e = small_font.render("Press ESC to exit", True, RED)

        screen.blit(t, (WIDTH//2 - t.get_width()//2, HEIGHT*0.25))
        screen.blit(n, (WIDTH//2 - n.get_width()//2, HEIGHT*0.38))
        screen.blit(d, (WIDTH//2 - d.get_width()//2, HEIGHT*0.55))
        screen.blit(e, (WIDTH//2 - e.get_width()//2, HEIGHT*0.75))

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
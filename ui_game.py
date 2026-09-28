import pygame
import sys
import time
import random
from head_tilt import detect_head_tilt

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

    # Q1
    {"L": ["Eleven","Steve","Erica"],
     "R": ["Nancy","Jonathan","Vecna"]},

    # Q2
    {"L": ["Mike","Lucas","Max"],
     "R": ["Will","Dustin","Nancy"]},

    # Q3
    {"L": ["Steve","Max","Erica"],
     "R": ["Jonathan","Will","Vecna"]},

    # Q4
    {"L": ["Eleven","Lucas","Mike"],
     "R": ["Dustin","Nancy","Jonathan"]},

    # Q5
    {"L": ["Erica","Steve","Max"],
     "R": ["Will","Jonathan","Vecna"]},

    # Q6
    {"L": ["Mike","Eleven","Dustin"],
     "R": ["Nancy","Lucas","Vecna"]},

    # Q7
    {"L": ["Max","Lucas","Steve"],
     "R": ["Jonathan","Nancy","Will"]},

    # Q8
    {"L": ["Erica","Eleven","Mike"],
     "R": ["Vecna","Will","Dustin"]},

    # Q9
    {"L": ["Steve","Dustin","Lucas"],
     "R": ["Jonathan","Nancy","Max"]},

    # Q10
    {"L": ["Eleven","Mike","Erica"],
     "R": ["Vecna","Will","Jonathan"]}
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

tilt_start = None
current_tilt = "C"
TILT_HOLD = 0.4

lightning_alpha = 0

# ================= START PAGE =================
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

        if show_result and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # ================= START PAGE DRAW =================
    if not game_started:
        title = title_font.render("STRANGER THINGS", True, RED)
        sub = text_font.render("Personality Test", True, WHITE)
        hint = small_font.render("Press ANY key to start", True, RED)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT*0.35))
        screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT*0.48))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT*0.62))

        pygame.display.update()
        continue

    # ================= LIGHTNING =================
    if random.randint(0, 90) == 0:
        lightning_alpha = random.randint(140, 220)

    if lightning_alpha > 0:
        flash = pygame.Surface((WIDTH, HEIGHT))
        flash.set_alpha(lightning_alpha)
        flash.fill(RED)
        screen.blit(flash, (0, 0))
        lightning_alpha -= 12

    # ================= HEAD TILT =================
    if not show_result:
        tilt = detect_head_tilt()

        if tilt == "C":
            tilt_start = None
            current_tilt = "C"

        if tilt in ["L", "R"]:
            if tilt != current_tilt:
                current_tilt = tilt
                tilt_start = time.time()

            if tilt_start and time.time() - tilt_start >= TILT_HOLD:
                for c in option_map[q_index][tilt]:
                    scores[c] += 1

                q_index += 1
                tilt_start = None
                current_tilt = "C"
                time.sleep(0.25)

                if q_index >= len(questions):
                    show_result = True
                    result_char = max(scores, key=scores.get)

    # ================= DRAW =================
    if not show_result:
        title = title_font.render("PERSONALITY TEST", True, RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT*0.1))
 
       
        q = questions[q_index]
        qt = text_font.render(q["q"], True, WHITE)
        screen.blit(qt, (WIDTH//2 - qt.get_width()//2, HEIGHT*0.35))

        y = HEIGHT * 0.72

        # LEFT OPTION (no bullet)
        left_text = text_font.render(q["L"], True, RED)
        screen.blit(left_text, (WIDTH*0.05, y))

        # RIGHT OPTION (no bullet)
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

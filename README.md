# 🚀 Gone in 60 Parsecs — Space Heist | Hack or Be Hacked

> A console-based cybersecurity quiz game built in Python. You're a space pirate. You have a hack ship. You have a mission. **Steal the fleet.**

---

## 🎮 About

*Gone in 60 Parsecs* is an interactive, story-driven quiz game set in deep space. You pilot **The Phantom Byte**, a hack ship docked at Dottie's Homebase near Pluto. Your goal: hunt down four enemy spacecraft and breach their defenses by answering cybersecurity questions correctly.

Each target ship is protected by a different cybersecurity domain. Answer fast and answer well — wrong answers damage your own hull.

---

## ✨ Features

- Console-based RPG-style gameplay with animated text output
- Four unique enemy ships, each guarding a different cybersecurity topic
- Timed question responses — hesitate and you lose ground
- Dynamic win/lose conditions based on hull and defense percentages
- Persistent enemy ship defense status in a draw or loss condition
- Mission timer tracking how long each hack takes
- A growing fleet that tracks every ship you've captured
- Replayable — attempt multiple missions per session

---

## 🛸 Gameplay Loop

1. Your homebase (Dottie) and your ship (The Phantom Byte) are initialized
2. A list of active target ships is displayed
3. You select a target and a hack mission begins
4. You answer 6 multiple-choice cybersecurity questions
   - ✅ Correct answer → target's defenses drop 25%
   - ❌ Wrong answer → your hull takes 25% damage
5. **Win condition:** 4 correct answers = 0% defenses remaining — the ship joins your fleet
6. **Lose condition:** your hull reaches 0% — return to Dottie for repairs
7. Repeat until all ships are captured or you quit

---

## 🧠 Cybersecurity Topics Covered

| Ship | Codename | Location | Topic |
|---|---|---|---|
| Enterprise | Top Gun | Planet Vulcan | Network Security |
| Eleanor | ANDROMEDA | Planet Vega | Encryption |
| Tardis | Tesla | Jupiter's Moon: Io | Social Engineering |
| Serenity | Firefly | Saturn's Moon: Titan | Malware & Intrusion |

---

## 🗂 Project Structure

```
SpaceProjectTm1_Quiz/
├── main.py          # Entry point; game loop and setup
├── mission.py       # Core hack mission logic and quiz runner
├── quiz.py          # Question bank organized by cybersecurity topic
├── hackship.py      # Player ship class (HackShip)
├── enemySS.py       # Enemy ship class (EnemySpaceShip)
├── homebase.py      # Homebase class (Homebase)
├── fleet.py         # Fleet tracker for captured ships
├── animation.py     # Animated text output helpers
├── intro.py         # Intro scroll sequence
└── timer.py         # Mission timer and timed input handler
```

---

## ⚙️ Setup & Running

**Requirements:** Python 3.x (no external libraries needed)

```bash
# 1. Clone the repository
git clone https://github.com/sgoudy/SpaceProjectTm1_Quiz.git
cd SpaceProjectTm1_Quiz

# 2. Run the game
python main.py
or 
.\run.bat
```

With 'python main.py' the game runs entirely in your terminal, in color.
With .\run.bat, the game runs in a new console window in black and white for a more retro feel.

---

## 👥 Authors

Charles, Jordan, Jon, Robert, Shelby — April Cohort 2026
# 🤖 NAO Robot Ball Throwing Game

This project controls a NAO humanoid robot to play a simple ball-throwing game using tactile input and arm movement. The robot asks the user to place a ball in its hand, throws it toward a target, and tracks successful shots based on user feedback.

---

## 🎯 Project Objective

- Use NAO's **touch sensors** and **speech output** to interact with users
- Control arm joints using **ALMotion API**
- Perform a **throwing gesture** with coordinated joint angles
- Track performance across multiple attempts

---

## ⚙️ Features

- 🤝 Waits for user to touch the head before throwing
- 🗣️ Uses `ALTextToSpeech` to guide the user
- 💪 Moves left arm through 3 stages: ready, receive ball, throw
- 🔁 Loops until 7 successful throws are confirmed

---

## 🧠 How It Works

1. NAO greets the user and asks them to place a ball in its left hand.
2. The user triggers the action by **touching the head sensor**.
3. NAO **closes its hand**, raises the arm, and **throws** the ball.
4. After each throw, it asks the user: _"Did I score?"_
5. The user replies in the terminal, and NAO repeats until it scores 7 times.

---

## 🧩 Tech Stack

| Component       | Description                                  |
|------------------|----------------------------------------------|
| `naoqi`          | Python SDK for NAO robot                     |
| `ALMotion`       | Controls NAO's joints and movement           |
| `ALTextToSpeech` | Makes NAO talk to the user                   |
| `ALMemory`       | Subscribes to head touch events              |
| `ALBroker`       | Communication interface with NAO             |

---

## 📍 Requirements

- NAO Robot connected to the same network
- Python 2.7 (for `raw_input`)
- `naoqi` Python SDK installed
- IP address of the robot (`nao_ip`) configured

---


## 🚀 How to Run

1. Set the correct IP address in the script:
   ```python
   nao_ip = "10.1.95.107"  # replace with your NAO's IP

---


https://github.com/user-attachments/assets/f1b1263d-b374-4b58-9c5c-c4596802dece


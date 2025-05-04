# -Peer-Ping-Pong-project
In the Peer Ping Pong project, a NAO humanoid robot plays a simplified ping‑pong game with a human partner:

It prompts the user to place a ball in its hand by speaking and waiting for a head‑touch sensor event.

Once the ball is in place, it closes its hand, raises its arm, and “serves” the ball by opening the hand and performing a throw motion.

After each serve, it asks the user whether the shot was successful (yes/no) via text‑to‑speech and console input, tracking the number of successful hits until a target is reached.

The implementation covers:

Connecting to NAO’s motion, speech, and memory services.

Subscribing to the TouchChanged event for head‑touch detection.

Defining helper functions for arm‑raising presets and the throwing sequence.

A main loop that repeats until a predefined number of successful shots is achieved, with real‑time spoken prompts and user feedback.

This project demonstrates event‑driven robotics interaction, basic sensor integration, and synchronized motion plus speech control on the NAO platform.










import pyautogui
import time

# Parse qa.txt
pairs = []
with open("qa.txt", "r") as f:
    title = f.readline().strip()

    while ((line := f.readline())):
        line = line.strip()

        if len(line) < 1: # Empty line
            continue

        if line[0] == "#": # Explicit comment
            continue

        if not ";" in line: # Not a pair
            continue

        pairs.append(line.split(";"));

# Give time to user
print("### Click on the \"Title\" field in WordMint! ###")
for i in range(3):
    print(f"\r{3 - i}...", end="");
    time.sleep(1)

print("")

# Input title
with pyautogui.hold("ctrl"):
    pyautogui.press("a")

print("Added title")
pyautogui.typewrite(title, _pause = False)
pyautogui.press(["tab" for i in range(4)])

# Input QA pairs
for (q, a) in pairs:
    q = q.strip()
    a = a.strip()

    pyautogui.typewrite(q)
    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.typewrite(a)
    pyautogui.press(["tab", "enter"])

    print(f"Added {q} => {a}")

    time.sleep(0.5) # Give time to process
    with pyautogui.hold("shift"): # Go back to "question"
        pyautogui.press(["tab", "tab"])

print("Done!")

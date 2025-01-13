# Epic Russian Roulette

This project is a Python-based simulation of [Russian Roulette](https://en.wikipedia.org/wiki/Russian_roulette) with a digital twist.

## About
This project introduces a Python-based simulation of Russian Roulette, reimagined with a modern, digital twist that leverages the virtual realm to create a high-stakes and potentially catastrophic gaming experience. Instead of physical harm, players face the ominous risk of jeopardizing their operating system's functionality. The game operates by randomly loading and spinning a virtual chamber, challenging players to match their choice with the spin result. If their selection aligns with the randomized chamber, the script escalates the stakes by attempting to delete the critical System32 directory on a Windows machine, an action that could render the system inoperable. Combining dark humor with a sobering lesson on the dangers of executing untrusted code, this project serves as both a cautionary tale and a provocative experiment. Play at your own risk!

## Features
- **Randomized Chamber Loading**: The program simulates the randomness of a spinning revolver chamber.
- **High Stakes Gameplay**: Players risk their system's functionality with each round.
- **Replay Options**: Players can choose to spin again, proceed cautiously, or exit the game.
## Disclaimer
**WARNING**: This script is designed for educational purposes to highlight the risks of executing untrusted code. Running it on your system could result in irreversible damage. Do not execute this script on a system you care about. The creator is not responsible for any harm caused by running this program.

## How It Works
1. How It Works
2. The game loads a "chamber" by selecting a random number between 1 and 6.
3. The player spins the chamber, which generates a new random number.
4. Player can either proceed to "shoot" or choose to spin again.
5. If the player's chamber matches the spin result, the script attempts to delete the `System32` directory.
Players can replay or exit the game after each round.

# Code Overview
## Key Functions:
- **spin()**: Randomly generates a number between 1 and 6 to simulate spinning the revolver's chamber.
## Critical Code Snippets:
```Python
    if chamber == spin_res:
       os.rmdir("C:\Windows\System32")
```
This line attempts to delete the `System32` directory if the player loses. On most modern systems, permissions and safeguards should prevent this, but the potential for catastrophic consequences remains.
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for details.

## Contributing

Contributions to improve the educational value of this script are welcome.

---

**Play at your own risk and learn responsibly!**

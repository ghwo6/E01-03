from mac_simulation import Simulation
import sys


simulation = Simulation()
if __name__ == "__main__":
    try:
        while not simulation.exit_key_press:
            simulation.menu()
    except KeyboardInterrupt:
        print("ctrl + c 키가 입력되었습니다.")
        sys.exit(1)
    except EOFError:
        print("ctrl + D 키가 입력되었습니다.")
        sys.exit(1)

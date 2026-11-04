import logging
from logic_function import (
    add_match_result,
    add_team,
    best_attacking_team,
    check_championship_potential,
    leading_team,
    show_standings,
    show_teams,
    team_success_rate,
    teams_without_wins,
    tournament_summary,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def print_menu():
    print("\n=== TOURNAMENT MANAGER ==========")
    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10. Check championship potential")
    print("0. Exit")

def main():
    logging.info("System started")
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_team()
        elif choice == "2":
            show_teams()
        elif choice == "3":
            add_match_result()
        elif choice == "4":
            show_standings()
        elif choice == "5":
            leading_team()
        elif choice == "6":
            best_attacking_team()
        elif choice == "7":
            team_success_rate()
        elif choice == "8":
            teams_without_wins()
        elif choice == "9":
            tournament_summary()
        elif choice == "10":
            check_championship_potential()
        elif choice == "0":
            logging.info("System closed")
            print("Goodbye!")
            break
        else:
            logging.warning("Invalid choice. Please choose a valid option (0-10).")


if __name__ == "__main__":
    main()
import sys


def ft_score_analytics():
    """Analyzes player scores from command-line arguments
    and displays statistics."""

    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    list_args = []

    for arg in sys.argv[1:]:
        try:
            list_args.append(int(arg))
        except ValueError:
            print(f"Error: Invalid score '{arg}' detected.")

    print(f"Scores processed: {list_args}")
    print(f"Total players: {len(list_args)}")
    total_score = sum(list_args)
    print(f"Total score: {total_score}")
    average_score = total_score / len(list_args)
    print(f"Average score: {average_score}")
    print(f"High score: {max(list_args)}")
    print(f"Low score: {min(list_args)}")
    print(f"Score range: {max(list_args) - min(list_args)}")

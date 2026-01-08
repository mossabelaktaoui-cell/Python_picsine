data = {'alice': ['first_blood', 'pixel_perfect', 'speed_runner', 'first_blood', 'first_blood'],
        'bob': ['level_master', 'boss_hunter', 'treasure_seeker', 'level_master', 'level_master'],
        'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood', 'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood'],
        'diana': ['first_blood', 'combo_king', 'level_master', 'treasure_seeker', 'speed_runner', 'combo_king', 'combo_king', 'level_master'],
        'eve': ['level_master', 'treasure_seeker', 'first_blood', 'treasure_seeker', 'first_blood', 'treasure_seeker'],
        'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer', 'first_blood', 'boss_hunter']}




def data_players_show(data):
    print("=== Achievement Tracker System ===\n")
    for player, data in data.items():
        print(f"player {player} achievements: {set(data)}")

def achievement_analytics(data):
    players = list(data.keys())
    common_achievements = set(data[players[0]])
    unique_acheivements = set()
    difference_achievements = set()
    diff_achievements = set()

    for player in data.keys():
        unique_acheivements = unique_acheivements | set(data[player])
        common_achievements = common_achievements & set(data[player])
        diff_achievements = set(data[player])
        for player_ in data.keys():
            if player_ != player:
                diff_achievements = diff_achievements - set(data[player_])
        difference_achievements = difference_achievements | diff_achievements

    if not common_achievements:
        common_achievements = "{}"
    if not unique_acheivements:
        unique_acheivements = "{}"
    if not difference_achievements:
        difference_achievements = "{}"

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_acheivements}")
    print(f"Total unique achievements: {len(unique_acheivements)}")
    print(f"\nCommon to all players:{common_achievements}")
    print(f"Rare achievements (1 player): {difference_achievements}")

def two_players_common(data, player1, player2):
    print("")
    
#data_players_show(data)
achievement_analytics(data)



    alice_bob_common = (set(players_data['alice']['achievements']) &
                        set(players_data['bob']['achievements']))

    alice_unique = (set(players_data['alice']['achievements']) -
                    set(players_data['bob']['achievements']))

    bob_unique = (set(players_data['bob']['achievements']) -
                  set(players_data['alice']['achievements']))

    print("\n=== Achievement Analysis ===")
    print(f"All unique achievements: {unique_acheivements}")
    print(f"Total unique achievements: {len(unique_acheivements)}")
    print(f"\nCommon to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {difference_achievements}")
    print(f"\nAlice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")

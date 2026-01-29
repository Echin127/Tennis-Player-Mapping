import csv

def main(ranking_csv, player_csv):
    with open(ranking_csv, "r", encoding="utf-8") as rank_data, open(player_csv, "r", encoding="utf-8") as player_data:
        rank_dict = {}
        ranking = int(1)
        
        next(rank_data)
        for line in rank_data:
            line = line.strip().split(",")
            rank_id = line[2]
            if rank_id not in rank_dict:
                rank_dict[rank_id] = 0
            rank_dict[rank_id]=ranking
            ranking += 1
        
        player_dict = {}
        next(player_data)
        for line in player_data:
            line = line.strip().split(",")
            player_id = line[0]
            first = line[1]
            last = line[2]
            nation = line[5]
            
            name = (first + " " + last)
            if player_id not in player_dict and player_id in rank_dict:
                player_dict[player_id] = 0
                player_dict[player_id] = [name, rank_dict[player_id], nation]
        
        max_entry = max(value[1] for value in player_dict.values())
        
        for key, value in player_dict.items():
            value[1] = max_entry - value[1]
        
        player_dict = sorted(player_dict.items(), key=lambda x: x[1][1], reverse = True)
        
        
    with open("output_players.csv", "w", newline="", encoding="utf-8") as ranked:
        writer = csv.writer(ranked)
        writer.writerow(["player_id", "name", "ranking", "nation"])  # header
        for player_id, info in player_dict:  
            writer.writerow([player_id, info[0], info[1], info[2]])
            
    with open("output_players.csv", "r", encoding="utf-8") as ranked:
        sum_dict = {}
        total_dict = {}
        next(ranked)  # skip header

        for line in ranked:
            line = line.strip().split(",")
            ranking = int(line[2])
            nation = line[3]

            if nation not in sum_dict:
                sum_dict[nation] = 0
                total_dict[nation] = 0

            sum_dict[nation] += ranking
            total_dict[nation] += 1

# Write CSV including number of players
    with open("countries_ranked00s.csv", "w", newline="", encoding="utf-8") as countries:
        writer = csv.writer(countries)
        writer.writerow(["country", "points", "players"])  # added players column

        for nation in sum_dict:
            writer.writerow([nation, sum_dict[nation], total_dict[nation]])

    print("Completed")

            
            
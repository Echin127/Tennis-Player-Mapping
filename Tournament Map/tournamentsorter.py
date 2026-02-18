import csv

def sorter(tournaments_csv, outputname):
    with open(tournaments_csv, "r", encoding="utf-8-sig") as tour_data:
        tour_dict = {}
        next(tour_data)
        
        tour_rank = ['Grand Slam', 'ATP 1000', 'ATP 500', 'United Cup', 'ATP 250',
                     'Challenger 175', 'Challenger 125', 'Challenger 100', 'Challenger 75',
                     'Challenger 50', 'M25', 'M15']
        
        rank_dict = {cat: i for i, cat in enumerate(tour_rank)}
        
        for line in tour_data:
            line = line.strip().split(",")
            if any('cancelled' in str(field).lower() for field in line):
                continue
            country = line[0]
            city = line[1]
            city = city.rstrip('0123456789').strip('"').title()

            if country == "USA":
                cat = line[3]
                surface = clean_text(line[4])
                name = line[5]

            else:
                cat = line[2]
                surface = clean_text(line[3])
                name = line[4]
            
            if city not in tour_dict:
                count = 0
                tour_dict[city] = [country, [cat], surface, count, name]  # cat as a list
            else:
                if cat not in tour_dict[city][1]:  # Check if cat not in list
                    tour_dict[city][1].append(cat)  # Append to the list
            
            tour_dict[city][3] += 1  # Increment count
            
    
    with open(outputname, "w", newline="", encoding="utf-8-sig") as output:
        writer = csv.writer(output)
        writer.writerow(["City", "Country", "Category", "Surface", "Total", "Tournament Name", "Best"])
        for city in tour_dict:
            categories_list = tour_dict[city][1]
            # Get the one with smallest rank (highest tier)
            highest_category = min(categories_list, key=lambda x: rank_dict.get(x, len(rank_dict)))
            writer.writerow([city, tour_dict[city][0], ", ".join(categories_list),  # original categories as a string
                tour_dict[city][2], tour_dict[city][3], tour_dict[city][4], highest_category])

    
    print("Completed")
    
def clean_text(value):
    if value:
        value = value.replace("\u00A0", " ")  # replace non-breaking space
        value = value.replace("Â", "")        # remove stray Â
        return value.strip()
    return value

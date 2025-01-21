white = "White"
brown = ["Brown","Browne"]
green = ["Green","Greene"]
blue = "Blue"
black = "Black"
grey = ["Gray","Grey"]
import pandas as pd
#download FanGraphs.com leaderboard for career batting WAR and move to desktop. I put it in a color folder within a MLB folder
batter_war = pd.read_csv("~/Desktop/MLB/color/fangraphs-leaderboards.csv")
batter_names = batter_war["Name"]
spaces = []
for name in batter_names:
    n_spaces = name.count(" ")
    spaces.append(n_spaces)
#print(max(spaces))
batter_war = batter_war.assign(spaces = spaces)
batter_war = batter_war[["Name","spaces","PlayerId","WAR"]]
#download FanGraphs.com leaderboard for career pitching WAR and move to desktop ...
pitcher_war = pd.read_csv("~/Desktop/MLB/color/fangraphs-leaderboards-2.csv")
pitcher_names = pitcher_war["Name"]
spaces = []
for name in pitcher_names:
    n_spaces = name.count(" ")
    spaces.append(n_spaces)
#print(max(spaces))
pitcher_war = pitcher_war.assign(spaces = spaces)
pitcher_war = pitcher_war[["Name","spaces","PlayerId","WAR"]]
war = pd.concat([batter_war,pitcher_war])
combined_war = war.groupby(["Name","spaces","PlayerId"])["WAR"].sum().reset_index()
#for n_spaces in set(combined_war["spaces"]):
    #n_spaces_combined_war = combined_war[combined_war["spaces"] == n_spaces]
    #print(n_spaces_combined_war.sort_values(by = "WAR", ascending = False).head(3))
combined_war_1_space = combined_war[combined_war["spaces"] == 1]
Names = combined_war_1_space["Name"]
names_1 = []
names_2 = []
for name in Names:
    split_name = name.split(" ")
    name_1 = split_name[0]
    names_1.append(name_1)
    name_2 = split_name[1]
    names_2.append(name_2)
name_1_colors = []
for name in names_1:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_1_colors.append(color)
name_2_colors = []
for name in names_2:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_2_colors.append(color)
combined_war_1_space = combined_war_1_space.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = "", name_4_color = "")
combined_war_2_spaces = combined_war[combined_war["spaces"] == 2]
Names = combined_war_2_spaces["Name"]
names_1 = []
names_2 = []
names_3 = []
for name in Names:
    split_name = name.split(" ")
    name_1 = split_name[0]
    names_1.append(name_1)
    name_2 = split_name[1]
    names_2.append(name_2)
    name_3 = split_name[2]
    names_3.append(name_3)
name_1_colors = []
for name in names_1:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_1_colors.append(color)
name_2_colors = []
for name in names_2:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_2_colors.append(color)
name_3_colors = []
for name in names_3:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_3_colors.append(color)
combined_war_2_spaces = combined_war_2_spaces.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = name_3_colors, name_4_color = "")
combined_war_3_spaces = combined_war[combined_war["spaces"] == 3]
Names = combined_war_3_spaces["Name"]
names_1 = []
names_2 = []
names_3 = []
names_4 = []
for name in Names:
    split_name = name.split(" ")
    name_1 = split_name[0]
    names_1.append(name_1)
    name_2 = split_name[1]
    names_2.append(name_2)
    name_3 = split_name[2]
    names_3.append(name_3)
    name_4 = split_name[3]
    names_4.append(name_4)
name_1_colors = []
for name in names_1:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_1_colors.append(color)
name_2_colors = []
for name in names_2:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_2_colors.append(color)
name_3_colors = []
for name in names_3:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_3_colors.append(color)
name_4_colors = []
for name in names_4:
    if name == white:
        color = "white"
    elif name in brown:
        color = "brown"
    elif name in green:
        color = "green"
    elif name == blue:
        color = "blue"
    elif name == black:
        color = "black"
    elif name in grey:
        color = "grey"
    else:
        color = "colorless"
    name_4_colors.append(color)
combined_war_3_spaces = combined_war_3_spaces.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = name_3_colors, name_4_color = name_4_colors)
combined_war = pd.concat([combined_war_1_space,combined_war_2_spaces,combined_war_3_spaces])
name_1_color = combined_war["name_1_color"]
name_1_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_1_color]
name_2_color = combined_war["name_2_color"]
name_2_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_2_color]
name_3_color = combined_war["name_3_color"]
name_3_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_3_color]
name_4_color = combined_war["name_4_color"]
name_4_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_4_color]
combined_war = combined_war.assign(name_1_color_value = name_1_color_value, name_2_color_value = name_2_color_value, name_3_color_value = name_3_color_value, name_4_color_value = name_4_color_value)
combined_war["color_value"] = combined_war["name_1_color_value"]+combined_war["name_2_color_value"]+combined_war["name_3_color_value"]+combined_war["name_4_color_value"]
#print(max(combined_war["color_value"]))
white_combined_war = combined_war[(combined_war["name_1_color"] == "white") | (combined_war["name_2_color"] == "white") | (combined_war["name_3_color"] == "white") | (combined_war["name_4_color"] == "white")]
white_combined_war = white_combined_war.assign(color = "white")
brown_combined_war = combined_war[(combined_war["name_1_color"] == "brown") | (combined_war["name_2_color"] == "brown") | (combined_war["name_3_color"] == "brown") | (combined_war["name_4_color"] == "brown")]
brown_combined_war = brown_combined_war.assign(color = "brown")
green_combined_war = combined_war[(combined_war["name_1_color"] == "green") | (combined_war["name_2_color"] == "green") | (combined_war["name_3_color"] == "green") | (combined_war["name_4_color"] == "green")]
green_combined_war = green_combined_war.assign(color = "green")
blue_combined_war = combined_war[(combined_war["name_1_color"] == "blue") | (combined_war["name_2_color"] == "blue") | (combined_war["name_3_color"] == "blue") | (combined_war["name_4_color"] == "blue")]
blue_combined_war = blue_combined_war.assign(color = "blue")
black_combined_war = combined_war[(combined_war["name_1_color"] == "black") | (combined_war["name_2_color"] == "black") | (combined_war["name_3_color"] == "black") | (combined_war["name_4_color"] == "black")]
black_combined_war = black_combined_war.assign(color = "black")
grey_combined_war = combined_war[(combined_war["name_1_color"] == "grey") | (combined_war["name_2_color"] == "grey") | (combined_war["name_3_color"] == "grey") | (combined_war["name_4_color"] == "grey")]
grey_combined_war = grey_combined_war.assign(color = "grey")
color_combined_war = pd.concat([white_combined_war,brown_combined_war,green_combined_war,blue_combined_war,blue_combined_war,black_combined_war,grey_combined_war])
color_combined_war = color_combined_war[["Name","PlayerId","color","WAR"]]
colors = ["white","brown","green","blue","black","grey"]
#for color in colors:
    #print(color_combined_war[color_combined_war["color"] == color].sort_values(by = "WAR", ascending = False).head(3))
color_war = color_combined_war.groupby("color")["WAR"].sum().reset_index()
import matplotlib.pyplot as plt
plt.bar(color_war["color"], color_war["WAR"], color = color_war["color"], edgecolor = "black")
plt.title("Color WAR")
plt.xlabel("color")
plt.ylabel("fWAR")
plt.show()

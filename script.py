white = "White"
brown = ["Brown","Browne"]
green = ["Green","Greene"]
blue = "Blue"
black = "Black"
grey = ["Gray","Grey"]
import pandas as pd
batter_war = pd.read_csv("fangraphs-leaderboards.csv")
batter_names = batter_war.Name
spaces = []
for name in batter_names:
    n_spaces = name.count(" ")
    spaces.append(n_spaces)
#print(max(spaces))
batter_war = batter_war.assign(spaces = spaces)
batter_war = batter_war[["Name","spaces","PlayerId","WAR"]]
pitcher_war = pd.read_csv("fangraphs-leaderboards-2.csv")
pitcher_names = pitcher_war.Name
spaces = []
for name in pitcher_names:
    n_spaces = name.count(" ")
    spaces.append(n_spaces)
#print(max(spaces))
pitcher_war = pitcher_war.assign(spaces = spaces)
pitcher_war = pitcher_war[["Name","spaces","PlayerId","WAR"]]
war = pd.concat([batter_war,pitcher_war])
war = war.groupby(["Name","spaces","PlayerId"])["WAR"].sum().reset_index()
#for n_spaces in set(war.spaces):
    #n_spaces_war = war[war.spaces == n_spaces]
    #print(n_spaces_war.sort_values(by = "WAR", ascending = False).head(3))
war_1_space = war[war.spaces == 1]
names = war_1_space.Name
names_1 = []
names_2 = []
for name in names:
    split_name = name.split(" ")
    name_1 = split_name[0]
    names_1.append(name_1)
    name_2 = split_name[1]
    names_2.append(name_2)
name_1_colors = []
def coloring(name_n_colors,names_n):
    for name in names_n:
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
        name_n_colors.append(color)
coloring(name_1_colors,names_1)
name_2_colors = []
coloring(name_2_colors,names_2)
war_1_space = war_1_space.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = "", name_4_color = "")
war_2_spaces = war[war.spaces == 2]
names = war_2_spaces.Name
names_1 = []
names_2 = []
names_3 = []
for name in names:
    split_name = name.split(" ")
    name_1 = split_name[0]
    names_1.append(name_1)
    name_2 = split_name[1]
    names_2.append(name_2)
    name_3 = split_name[2]
    names_3.append(name_3)
name_1_colors = []
coloring(name_1_colors,names_1)
name_2_colors = []
coloring(name_2_colors,names_2)
name_3_colors = []
coloring(name_3_colors,names_3)
war_2_spaces = war_2_spaces.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = name_3_colors, name_4_color = "")
war_3_spaces = war[war.spaces == 3]
names = war_3_spaces.Name
names_1 = []
names_2 = []
names_3 = []
names_4 = []
for name in names:
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
coloring(name_1_colors,names_1)
name_2_colors = []
coloring(name_2_colors,names_2)
name_3_colors = []
coloring(name_3_colors,names_3)
name_4_colors = []
coloring(name_4_colors,names_4)
war_3_spaces = war_3_spaces.assign(name_1_color = name_1_colors, name_2_color = name_2_colors, name_3_color = name_3_colors, name_4_color = name_4_colors)
war = pd.concat([war_1_space,war_2_spaces,war_3_spaces])
name_1_color = war.name_1_color
name_1_color_value = [1 if color != "colorless" else 0 for color in name_1_color]
name_2_color = war.name_2_color
name_2_color_value = [1 if color != "colorless" else 0 for color in name_2_color]
name_3_color = war.name_3_color
name_3_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_3_color]
name_4_color = war.name_4_color
name_4_color_value = [1 if (color != "colorless") & (color != "") else 0 for color in name_4_color]
war = war.assign(name_1_color_value = name_1_color_value, name_2_color_value = name_2_color_value, name_3_color_value = name_3_color_value, name_4_color_value = name_4_color_value)
war.color_value = war.name_1_color_value+war.name_2_color_value+war.name_3_color_value+war.name_4_color_value
#print(max(war.color_value))
white_war = war[(war.name_1_color == "white") | (war.name_2_color == "white") | (war.name_3_color == "white") | (war.name_4_color == "white")]
white_war = white_war.assign(color = "white")
brown_war = war[(war.name_1_color == "brown") | (war.name_2_color == "brown") | (war.name_3_color == "brown") | (war.name_4_color == "brown")]
brown_war = brown_war.assign(color = "brown")
green_war = war[(war.name_1_color == "green") | (war.name_2_color == "green") | (war.name_3_color == "green") | (war.name_4_color == "green")]
green_war = green_war.assign(color = "green")
blue_war = war[(war.name_1_color == "blue") | (war.name_2_color == "blue") | (war.name_3_color == "blue") | (war.name_4_color == "blue")]
blue_war = blue_war.assign(color = "blue")
black_war = war[(war.name_1_color == "black") | (war.name_2_color == "black") | (war.name_3_color == "black") | (war.name_4_color == "black")]
black_war = black_war.assign(color = "black")
grey_war = war[(war.name_1_color == "grey") | (war.name_2_color == "grey") | (war.name_3_color == "grey") | (war.name_4_color == "grey")]
grey_war = grey_war.assign(color = "grey")
color_war = pd.concat([white_war,brown_war,green_war,blue_war,black_war,grey_war])
color_war = color_war[["Name","PlayerId","color","WAR"]]
#color_war.to_csv("color_war.csv")
colors = ["white","brown","green","blue","black","grey"]
for color in colors:
    print(color_war[color_war.color == color].sort_values(by = "WAR", ascending = False).head(3))
color_war = color_war.groupby("color")["WAR"].sum().reset_index()
import matplotlib.pyplot as plt
plt.bar(color_war.color, color_war.WAR, color = color_war.color, edgecolor = "black")
plt.xlabel("color")
plt.ylabel("fWAR")
plt.title("Color WAR")
plt.show()

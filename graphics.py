from PIL import Image, ImageDraw, ImageFont
import time

starttime = time.time()

image_width = 3840
image_height = 2160

n_teams = 9

banner_height = int(image_height/25)
banner_east = int(image_width*0.95)
banner_west = int(image_width*0.05)
banner_south = int(image_height * 0.95)
banner_north = banner_south - banner_height

team_spacing = 10
team_width = int((banner_east - banner_west - (team_spacing*(n_teams + 1))) / (n_teams))


scorboard_spacing = 5
scoreboard_width = int(image_width/7)
scoreboard_height = int(banner_height*(n_teams + 1))
scoreboard_west = int(image_width*0.05)
scoreboard_east = scoreboard_west + scoreboard_width
scoreboard_north = int(image_height*0.05)
scoreboard_south = scoreboard_north + scoreboard_height

background = Image.open('boat.jpg')

image = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))

image.paste(background, (0, 0))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30*2)

#draw.rectangle([(0, 0), (image_width, image_height)], fill=(100, 10, 10, 255))

banner = [(banner_west, banner_north), (banner_east, banner_south)]
#draw.rectangle(banner, fill=(27, 59, 121, 255))

colors = [(16, 37, 140, 255), (247, 43, 22, 255), (0, 162, 75, 255), (255, 207, 53, 255), (161, 221, 240, 255), (241, 148, 192, 255), (133, 135, 139, 255), (255, 163, 43, 255), (255, 255, 255, 255)]
Teams = ["HSII", "FSK", "SKSII", "WC 2", "WC 3", "TS", "SSF", "FYC", "WC 6"]


for i in range(n_teams):
    draw.rectangle([(banner_west + team_spacing*(i) + team_width*i, banner_north), (banner_west + team_spacing*(i) + team_width*(i+1), banner_south)], fill=colors[i])
    draw.text((banner_west + team_spacing*(i) + team_width*i + team_width/2, banner_north+banner_height/2), Teams[i], font=font, fill=(255, 255, 255, 255), stroke_width=1, stroke_fill='black', anchor="mm")    

for i in range(n_teams):
    draw.rectangle([(scoreboard_west, scoreboard_north + banner_height*i + team_spacing*i), (scoreboard_east, scoreboard_north + banner_height*(i+1) + team_spacing*i)], fill=(255, 255, 255, 255))
    
for i in range(n_teams-1):
    draw.text((scoreboard_west + scoreboard_width/2, scoreboard_north + banner_height*(i+1) + team_spacing*(i+1) + banner_height/2), "0", font=font, fill=(255, 255, 255, 255), stroke_width=1, stroke_fill='black', anchor="mm")

draw.text((scoreboard_west + team_spacing, scoreboard_north + banner_height/2), "F2R2", font=font, fill=(0, 0, 0, 255), stroke_width=1, stroke_fill='black', anchor="lm")

draw.text((scoreboard_east - team_spacing, scoreboard_north + banner_height/2), "Time: -2:15", font=font, fill=(0, 0, 0, 255), stroke_width=1, stroke_fill='black', anchor="rm")




image.save('rectangle.png')










endtime = time.time()
print("Time taken: ", endtime - starttime)

image.show()
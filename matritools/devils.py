from matritools import nodefile as nf, utils as mu
import json
import pandas as pd

min_player_height = 64
max_player_height = 84
min_player_weight = 150
max_player_weight = 275
min_player_age = 17
max_player_age = 50


scout_report_distance = 20
scout_report_limit = 10
scout_offset = - 175

# player profile
age_color_scalar = mu.make_interpolator(min_player_age, max_player_age, 0, 127, True, True, 0)
height_cylinder_scalar = mu.make_interpolator(min_player_height, max_player_height, 0.1, 1, True, True, 0)
weight_cylinder_scalar = mu.make_interpolator(min_player_weight, max_player_weight, 0.1, 1, True, True, 0)

# scouting report
nhl_scalar = mu.make_interpolator(0, 8, 0.25, 1.85, True, True, 0)
skill_scalar = mu.make_interpolator(0, 8, 1.1, 3.7, True, True, 0)
total_skill_scalar = mu.make_interpolator(0, 48, 0.6, 2.4, True, True, 0)
game_rating_scalar = mu.make_interpolator(1, 5, 0.6, 3, True, True, 0)

# game ratings
game_rating_stone_xy_scalar = mu.make_interpolator(1,5, 0.6, 2, True, True, 0)
game_rating_stone_z_scalar = mu.make_interpolator(1,5, 0.06, 0.28, True, True, 0)
total_skill_delta_color_id_scalar = mu.make_interpolator(-48, 48, 127, 0, True, True, 0)

# bta
bta_ring_scalar = mu.make_interpolator(0, 10, 0.3, 2)

position_colors = {
    'Goalie': 'white',
    'Center/R.Wing': 'pink',
    'Left Wing': 'blue',
    'Forward': 'yellow',
    'Right Wing': 'red',
    'Defence': 'cyan',
    'Center': 'magenta',
    'Right Defence': 'orange',
    'Center/L.Wing': 'grey',
    'Wing': 'green',
    'Left Defence': 'lime',
    'D': 'cyan',
    'F': 'yellow',
    'G': 'white',
    'C': 'magenta',
    'R': 'red',
    'L': 'blue',
}

team_textures = {
  "Abbotsford Canucks": 4,
  "Bakersfield Condors": 5,
  "Belleville Senators": 6,
  "Bridgeport Islanders": 7,
  "Charlotte Checkers": 8,
  "Chicago Wolves": 9,
  "Cleveland Monsters": 10,
  "Colorado Eagles": 11,
  "Grand Rapids Griffins": 12,
  "Hartford Wolf Pack": 13,
  "Hershey Bears": 14,
  "Henderson Silver Knights": 15,
  "Iowa Wild": 16,
  "Laval Rocket": 17,
  "Lehigh Valley Phantoms": 18,
  "Manitoba Moose": 19,
  "Milwaukee Admirals": 20,
  "Ontario Reign": 21,
  "Providence Bruins": 22,
  "Rochester Americans": 23,
  "Rockford IceHogs": 24,
  "San Jose Barracuda": 25,
  "San Diego Gulls": 26,
  "Springfield Thunderbirds": 27,
  "Stockton Heat": 28,
  "Syracuse Crunch": 29,
  "Texas Stars": 30,
  "Toronto Marlies": 31,
  "Tucson Roadrunners": 32,
  "Utica Comets": 33,
  "Wilkes-Barre/Scranton Penguins": 34,
  "Anaheim Ducks": 35,
  "Arizona Coyotes": 36,
  "Boston Bruins": 37,
  "Buffalo Sabres": 38,
  "Calgary Flames": 39,
  "Carolina Hurricanes": 40,
  "Chicago Blackhawks": 41,
  "Colorado Avalanche": 42,
  "Columbus Blue Jackets": 43,
  "Dallas Stars": 44,
  "Detroit Red Wings": 45,
  "Edmonton Oilers": 46,
  "Florida Panthers": 47,
  "Los Angeles Kings": 48,
  "Minnesota Wild": 49,
  "Montreal Canadiens": 50,
  "Nashville Predators": 51,
  "New Jersey Devils": 52,
  "New York Islanders": 53,
  "New York Rangers": 54,
  "Ottawa Senators": 55,
  "Philadelphia Flyers": 56,
  "Pittsburgh Penguins": 57,
  "San Jose Sharks": 58,
  "Seattle Kraken": 59,
  "St. Louis Blues": 60,
  "Tampa Bay Lightning": 61,
  "Toronto Maple Leafs": 62,
  "Vancouver Canucks": 63,
  "Vegas Golden Knights": 64,
  "Washington Capitals": 65,
  "Winnipeg Jets": 66
}

nhl_grade_to_number = {
            'A+': 8,
            'A': 7,
            'B+': 6,
            'B': 5,
            'B-': 4,
            'C+': 3,
            'C': 2,
            'D+': 1,
            'D': 0,
            '--': None,
            'DK': None,
            'DN': None,
            '0': 0
}

number_to_nhl_grade = {
            8: 'A+',
            7: 'A',
            6: 'B+',
            5: 'B',
            4: 'B-',
            3: 'C+',
            2: 'C',
            1: 'D+',
            0: 'D',
}

# region set up glyph and NodeFile---------------------------------------
try:
    player_glyph = nf.Glyph('../glyphs/amateur_player/am_player_profile_v2_template_node.csv')
    scouting_report_mod = nf.Glyph('../glyphs/amateur_player/am_player_scouting_report_mod_template_node.csv')
    game_stats_mod = nf.Glyph('../glyphs/amateur_player/am_player_game_stats_mod_node.csv')
    game_ratings_mod = nf.Glyph('../glyphs/amateur_player/am_player_game_ratings_mod_node.csv')
    scout_coverage_mod = nf.Glyph('../glyphs/amateur_player/am_player_scout_coverage_mod_node.csv')
    scout_report_glyph = nf.Glyph('../glyphs/amateur_player/scout_report_template.csv')
    bta_mod = nf.Glyph('../glyphs/amateur_player/player_bta_mode_v2_node.csv')

    # endregion--------------------------------------------------------------

    # region identify key pieces of glyph----------------------------

    # since the glyph will be built in pieces, we can get references from the individual mods and append them to the main
    # glyph. The references are not copied to the main glyph, they are shared

    # player profile
    root = player_glyph.nodes[0]
    root.tag_text = 'root'
    age_ring = player_glyph.nodes[2]
    age_ring.set_color(0,0,0)
    age_ring.palette_id = 6
    shot_side_cone = player_glyph.nodes[3]
    team_ring = player_glyph.nodes[4]
    team_ring.set_color_by_name('white')
    height_weight_cylinder = player_glyph.nodes[5]
    league_ring = player_glyph.nodes[6]

    # scouting report
    scouting_root = scouting_report_mod.nodes[0]
    scouting_root.tag_text = 'scouting root'
    game_rating_cone = scouting_report_mod.nodes[1]
    nhl_ring = scouting_report_mod.nodes[2]
    shot_puck_handling_ring = scouting_report_mod.nodes[3]
    hockey_strength_low_post_ring = scouting_report_mod.nodes[4]
    compete_ring = scouting_report_mod.nodes[5]
    skating_technical_ring = scouting_report_mod.nodes[6]
    puck_athleticism_ring = scouting_report_mod.nodes[7]
    hockey_sense_ring = scouting_report_mod.nodes[8]
    total_skills_ring = scouting_report_mod.nodes[15]

    # game stats
    game_stats_root = game_stats_mod.nodes[0]
    game_stats_root.tag_text = 'game stats root'
    toi_sphere = game_stats_mod.nodes[1]
    xGA_ring = game_stats_mod.nodes[2]
    xGF_ring = game_stats_mod.nodes[3]

    # game ratings
    game_ratings_root = game_ratings_mod.nodes[0]
    game_ratings_root.tag_text = 'game ratings root'
    total_skill_delta_node = game_ratings_mod.nodes[11]
    total_skill_delta_node.set_color(0,0,0)
    total_skill_delta_node.palette_id = 6
    game_stone_1 = game_ratings_mod.nodes[5]
    game_stone_2 = game_ratings_mod.nodes[4]
    game_stone_3 = game_ratings_mod.nodes[3]
    game_stone_4 = game_ratings_mod.nodes[2]
    game_stone_5 = game_ratings_mod.nodes[1]
    game_stone_6 = game_ratings_mod.nodes[10]
    game_stone_7 = game_ratings_mod.nodes[9]
    game_stone_8 = game_ratings_mod.nodes[8]
    game_stone_9 = game_ratings_mod.nodes[7]
    game_stone_10 = game_ratings_mod.nodes[6]
    game_stones = [game_stone_1,
                   game_stone_2,
                   game_stone_3,
                   game_stone_4,
                   game_stone_5,
                   game_stone_6,
                   game_stone_7,
                   game_stone_8,
                   game_stone_9,
                   game_stone_10]

    # scout coverage
    scout_coverage_root = scout_coverage_mod.nodes[0]
    scout_coverage_root.tag_text = 'scout coverage root'
    low_coverage_alert = scout_coverage_mod.nodes[1]

    # scout report
    scout_report_root = scout_report_glyph.nodes[0]
    scout_type_node = scout_report_glyph.nodes[1]
    was_tournament_node = scout_report_glyph.nodes[2]
    win_loss_node = scout_report_glyph.nodes[3]
    home_away_node = scout_report_glyph.nodes[4]

    # bta
    bta_root = bta_mod.nodes[0]
    bta_root.tag_text = 'bta root'
    individual_ring = bta_mod.nodes[2]
    teammate_ring = bta_mod.nodes[3]
    learner_ring = bta_mod.nodes[4]
    leader_ring = bta_mod.nodes[5]
    competitor_ring = bta_mod.nodes[6]

except Exception as exc:
    print(mu.WARNING + 'If you are working outside of the Devils project, you may ignore the following warning. '
                       'If you working in Devils project, contact Greg.\n' +  str(exc) + mu.ENDC)
#endregion---------------------------------------------------------------

# region piece mods together-------------------------------

modding_scouting_report = False
modding_game_stats = False
modding_game_ratings = False
modding_scout_coverage = False
modding_bta = False
using_pro_data = True
player_tag_mode = 0
# append_scouting_report
def mod_scouting_report():
    global modding_scouting_report
    modding_scouting_report = True
    #scouting_root.parent_id = league_ring.id
    #scouting_report_mod.make_ids_consecutive(player_glyph.get_last_node().id + 1)
    scouting_root.set_translate()
    player_glyph.add_glyph(scouting_report_mod, league_ring.id, False)
    #for node in scouting_report_mod.nodes:
        #player_glyph.nodes.append(node)

# append game_stats_mod
def mod_game_stats():
    global modding_game_stats
    modding_game_stats = True
    #game_stats_root.parent_id = league_ring.id
    #game_stats_mod.make_ids_consecutive(player_glyph.get_last_node().id + 1)
    game_stats_root.set_translate(90, 0, 0)
    player_glyph.add_glyph(game_stats_mod, league_ring.id, False)
    #for node in game_stats_mod.nodes:
        #player_glyph.nodes.append(node)

# append game_ratings_mod
def mod_game_ratings():
    global modding_game_ratings
    modding_game_ratings = True
    #game_ratings_root.parent_id = league_ring.id
    #game_ratings_mod.make_ids_consecutive(player_glyph.get_last_node().id + 1)
    game_ratings_root.set_translate(180, 0, 0)
    player_glyph.add_glyph(game_ratings_mod, league_ring.id, False)
    #for node in game_ratings_mod.nodes:
     #   player_glyph.nodes.append(node)

# append scout_coverage_mod
def mod_scout_coverage():
    global modding_scout_coverage
    modding_scout_coverage = True
    #scout_coverage_root.parent_id = league_ring.id
    #scout_coverage_mod.make_ids_consecutive(player_glyph.get_last_node().id + 1)
    scout_coverage_root.set_translate(-90, 0, 0)
    player_glyph.add_glyph(scout_coverage_mod, league_ring.id, False)
    #for node in scout_coverage_mod.nodes:
        #player_glyph.nodes.append(node)

def mod_bta():
    global modding_bta
    modding_bta = True
    #bta_root.parent_id = league_ring.id
    #bta_mod.make_ids_consecutive(player_glyph.get_last_node().id + 1)
    bta_root.set_translate(-45, 0, 0)
    player_glyph.add_glyph(bta_mod, league_ring.id, False)
    #for node in bta_mod.nodes:
        #player_glyph.nodes.append(node)


# player profile
def build_player_profile(player, league_color_legend):

    # height, weight, position
    height_weight_cylinder.set_color_by_name(position_colors[player.position])
    x = y = weight_cylinder_scalar(player.weight)
    z = height_cylinder_scalar(player.height)
    height_weight_cylinder.set_scale(x, y, z)
    height_weight_cylinder.set_tag(
        player.fname + ' ' + player.lname + ', P: ' + player.position + ', W: ' + str(player.weight) + ', H: ' + str(
            player.height), player_tag_mode)

    # league
    league_ring.set_color_by_name(league_color_legend[player.league])
    league_ring.set_tag(player.league)

    if using_pro_data:
        team_ring.texture_id = team_textures[player.team]
    team_ring.tag_text = player.team

    age_ring.color_id = int(age_color_scalar(player.age))
    age_ring.tag_text = 'Age: ' + str(player.age)

    if player.shot_side == 'L':
        shot_side_cone.color_a = 255
        shot_side_cone.set_color_by_name('blue')
        shot_side_cone.translate_x = 90
        shot_side_cone.tag_text = "Shot Side: L"
    elif player.shot_side == 'R':
        shot_side_cone.color_a = 255
        shot_side_cone.set_color_by_name('red')
        shot_side_cone.translate_x = -90
        shot_side_cone.tag_text = "Shot Side: R"
    else:
        shot_side_cone.color_a = 0
        shot_side_cone.tag_text = ""

# region scouting report
def build_scouting_report(player):
    # total skills
    total_skills_ring.set_u_scale(total_skill_scalar(player.total_skills))
    total_skills_ring.set_tag("Total Skills(" + str(player.total_skills) + "/48)")

    build_nhl_ring(player)
    build_skill_rings(player)

    # game rating
    game_rating_cone.set_u_scale(game_rating_scalar(player.game_rating))
    game_rating_cone.set_tag("Game Rating(" + str(player.game_rating) + "/5)")

def build_skill_rings(player):
    if player.position == 'Goalie':
        build_skill_ring(player.low_post_play, hockey_strength_low_post_ring, 'Low / Post Play')
        build_skill_ring(player.technical, skating_technical_ring, 'Technical')
        build_skill_ring(player.athleticism, puck_athleticism_ring, 'Athleticism')
        build_skill_ring(player.puck_handling, shot_puck_handling_ring, 'Puck Handling')
    else:
        build_skill_ring(player.hockey_strength, hockey_strength_low_post_ring, 'Hockey Strength')
        build_skill_ring(player.skating, skating_technical_ring, 'Skating')
        build_skill_ring(player.puck_skills, puck_athleticism_ring, 'Puck Skills')
        build_skill_ring(player.shot, shot_puck_handling_ring, 'Shot')

    build_skill_ring(player.compete, compete_ring, 'Compete')
    build_skill_ring(player.hockey_sense, hockey_sense_ring, 'Hockey Sense')

def build_skill_ring(skill_rating, ring, skill_name):
    ring.scale_z = skill_scalar(skill_rating)
    ring.set_tag(skill_name + "(" + str(skill_rating) + "/8)")

def build_nhl_ring(player):
    nhl_scale = nhl_scalar(player.nhl_rating)
    nhl_ring.scale_x = nhl_scale
    nhl_ring.scale_y = nhl_scale
    if player.nhl_rating is not None:
        nhl_ring.set_tag("NHL Rating(" + number_to_nhl_grade[round(player.nhl_rating)] + ")")
    else:
        nhl_ring.set_tag("NHL Rating(" + str(player.nhl_rating) + ")")
# endregion

# region game ratings
def build_game_ratings(player):
    build_game_stones(player)

    # reset color_a
    total_skill_delta_node.color_a = 255
    total_skill_deltas = []
    for i in range(1, len(game_stones)):
        if i >= len(player.reports):
            continue
        total_skill_deltas.append(player.reports[i].total_skills - player.reports[i-1].total_skills)

    # if there are no total_skill_deltas, hide total_skill_delta
    if len(total_skill_deltas) == 0:
        total_skill_delta_node.color_a = 0
        total_skill_delta_node.set_tag("Total Skill Delta: N/A")
    else:
        total_skill_delta_node.color_id = int(total_skill_delta_color_id_scalar(sum(total_skill_deltas) / len(total_skill_deltas)))
        total_skill_delta_node.set_tag("Total Skill Delta: " + str(sum(total_skill_deltas) / len(total_skill_deltas)))

def build_game_stones(player):
    for i in range(len(game_stones)):
        # if less reports than there are stones, fill the rest N/A
        if i >= len(player.reports):
            game_stones[i].set_scale(0, 0, 0)
            game_stones[i].set_tag("Game " + str(i + 1) + " Rating(N/A)")
        else:
            if player.reports[i].game_rating is None:
                game_stones[i].set_scale(0,0,0)
                game_stones[i].set_tag("Game " + str(i + 1) + " Rating(N/A)")
            else:
                x = y = game_rating_stone_xy_scalar(player.reports[i].game_rating)
                z = game_rating_stone_z_scalar(player.reports[i].game_rating)
                game_stones[i].set_scale(x, y, z)
                game_stones[i].set_tag("Game " + str(i+1) + " Rating(" + str(player.reports[i].game_rating) + ")")
# endregion

# region scout coverage
def build_scout_coverage(player):
    # paraent scout report to scout coverage mod
    #scout_report_root.parent_id = scout_coverage_root.id

    # build each report
    for i in range(len(player.reports)):
        if i == scout_report_limit:
            break
        build_scout_report(i, player.reports[i])

def build_scout_report(index, report):
    # adjust ids
    #scout_report_glyph.make_ids_consecutive(player_glyph.get_next_id())

    scout_report_root.set_translate((index * scout_report_distance) + scout_offset)

    # edit individual pieces of scout report glyph
    build_win_loss(report)
    build_home_away(report)
    build_was_tournament(report)
    build_scout_type(report)
    player_glyph.add_temp_glyph(scout_report_glyph, scout_coverage_root.id)

def build_scout_type(report):
    if report.scout_type == 'A':
        scout_type_node.geometry = nf.geos['sphere']
        scout_type_node.set_color_by_name('green')
        scout_type_node.set_tag('A')
    else:
        scout_type_node.geometry = nf.geos['cube']
        scout_type_node.set_color_by_name('orange')
        scout_type_node.set_tag('M')

def build_was_tournament(report):
    if report.tournament != "N/A":
        was_tournament_node.geometry = nf.geos['cube']
        was_tournament_node.set_color_by_name('beige')
    else:
        was_tournament_node.geometry = nf.geos['cone']
        was_tournament_node.set_color_by_name('cyan')

    was_tournament_node.set_tag(report.tournament)

def build_home_away(report):
    home_away_node.color_a = 255
    if report.home_away == "Home":
        home_away_node.geometry = nf.geos['sphere']
        home_away_node.set_color_by_name('hot pink')
        home_away_node.set_tag("Home")
    elif report.home_away == "Away":
        home_away_node.geometry = nf.geos['cube']
        home_away_node.set_color_by_name('purple')
        home_away_node.set_tag("Away")
    else:
        home_away_node.color_a = 0

def build_win_loss(report):
    if report.game_won == 'True':
        win_loss_node.geometry = 13
        win_loss_node.set_color_by_name('grey')
        win_loss_node.tag_text = "Game Won"
    else:
        win_loss_node.geometry = 15
        win_loss_node.set_color_by_name('yellow')
        win_loss_node.tag_text = "Game loss"
# endregion

# region bta
def build_bta(player):
    individual_ring.color_a = 255
    teammate_ring.color_a = 255
    learner_ring.color_a = 255
    leader_ring.color_a = 255
    competitor_ring.color_a = 255

    build_bta_ring(player.bta_individual, individual_ring, "Individual")
    build_bta_ring(player.bta_teammate, teammate_ring, 'Teammate')
    build_bta_ring(player.bta_learner, learner_ring, 'Learner')
    build_bta_ring(player.bta_leader, leader_ring, 'Leader')
    build_bta_ring(player.bta_competitor, competitor_ring, 'Competitor')

def build_bta_ring(bta_rating, ring, tag):
    if bta_rating is None:
        ring.color_a = 0
    else:
        ring.set_u_scale(bta_ring_scalar(bta_rating))
        ring.tag_text = tag + ": " + str(bta_rating)

# endregion

def build_glyph(player, league_color_legend):
    build_player_profile(player, league_color_legend)
    if modding_scouting_report:
        build_scouting_report(player)
    if modding_game_ratings:
        build_game_ratings(player)
    if modding_scout_coverage:
        build_scout_coverage(player)
    if modding_bta:
        build_bta(player)

class Player:
    def __init__(self, df, number_of_reports = 0, less_than_function=None):
        self.bta_individual = None
        self.bta_teammate = None
        self.bta_learner = None
        self.bta_leader = None
        self.bta_competitor = None

        self.bta_individual_z_score = None
        self.bta_teammate_z_score = None
        self.bta_learner_z_score = None
        self.bta_leader_z_score = None
        self.bta_competitor_z_score = None

        self.hockey_sense_z_score = None
        self.skating_z_score = None
        self.compete_z_score = None
        self.hockey_strength_z_score = None
        self.puck_skills_z_score = None
        self.game_rating_z_score = None
        self.nhl_rating_z_score = None
        self.low_post_play_z_score = None
        self.technical_z_score = None
        self.athleticism_z_score = None
        self.puck_handling_z_score = None
        self.shot_z_score = None
        self.total_skills_z_score = None

        self.age_z_score = None
        self.height_z_score = None
        self.weight_z_score = None

        self.rank = None
        self.change = None
        if isinstance(df, dict):
            self.__build_from_dict__(df, number_of_reports)
        else:
            self.__build_from_df__(df, number_of_reports)

        def sort_by_total_skill(first, other):
            return first.total_skills < other.total_skills

        if less_than_function is None:
            self.less_than = sort_by_total_skill
        else:
            self.less_than = less_than_function

    def __repr__(self, include_reports=False):
        report_str = ""
        if include_reports:
            for report in self.reports:
                report_str += str(report)
            report_str += "\n"

        return  "id: " + self.id + "\n" + \
                "fname: " + self.fname + "\n" + \
                "lname: " + self.lname + "\n" + \
                "age: " + str(self.age) + "\n" + \
                "height: " + str(self.height) + "\n" + \
                "weight: " + str(self.weight) + "\n" + \
                "rank: " + str(self.rank) + "\n" + \
                "change: " + str(self.change) + "\n" + \
                "shot side: " + self.shot_side + "\n" + \
                "total skills: " + str(self.total_skills) + "\n" + \
                "nhl rating: " + str(self.nhl_rating) + "\n" + \
                "hockey sense: " + str(self.hockey_sense) + "\n" + \
                "skating: " + str(self.skating) + "\n" + \
                "compete: " + str(self.compete) + "\n" + \
                "hockey strength: " + str(self.hockey_strength) + "\n" + \
                "game rating: " + str(self.game_rating) + "\n" + \
                "puck skills: " + str(self.puck_skills) + "\n" + \
                "puck handling: " + str(self.puck_handling) + "\n" + \
                "athleticism: " + str(self.athleticism) + "\n" + \
                "technical: " + str(self.technical) + "\n" + \
                "shot: " + str(self.shot) + "\n" + \
                "low / post play: " + str(self.low_post_play) + "\n" + \
                "bta individual:" + str(self.bta_individual) + "\n" + \
                "bta teammate: " + str(self.bta_teammate) + "\n" + \
                "bta learner: " + str(self.bta_learner) + "\n" + \
                "bta leader: " + str(self.bta_leader) + "\n" + \
                "bta competitor: " + str(self.bta_competitor) + "\n" + \
                report_str + "\n"

    def __lt__(self, other):
        return self.less_than(self, other)

    def to_dict(self, include_reports=True):
        result = {}

        result['ID'] = self.id
        result['First Name'] = self.fname
        result['Last Name'] = self.lname
        result['Age'] = self.age
        result['Height'] = self.height
        result['Weight'] = self.weight
        result['Rank'] = self.rank
        result['Change'] = self.change
        result['Shot Side'] = self.shot_side
        result['Position'] = self.position
        result['League'] = self.league
        result['Team'] = self.team
        result['Hockey Sense'] = self.hockey_sense
        result['Skating'] = self.skating
        result['Compete'] = self.compete
        result['Hockey Strength'] = self.hockey_strength
        result['Puck Skills'] = self.puck_skills
        result['Game Rating'] = self.game_rating
        result['NHL Rating'] = self.nhl_rating
        result['Low / Post Play'] = self.low_post_play
        result['Technical'] = self.technical
        result['Athleticism'] = self.athleticism
        result['Puck Handling'] = self.puck_handling
        result['Shot'] = self.shot
        result['Total Skills'] = self.total_skills
        result['BTA Individual'] = self.bta_individual
        result['BTA Teammate'] = self.bta_teammate
        result['BTA Learner'] = self.bta_learner
        result['BTA Leader'] = self.bta_leader
        result['BTA Competitor'] = self.bta_competitor


        result['Age Z Score'] = self.age_z_score
        result['Height Z Score'] = self.height_z_score
        result['Weight Z Score'] = self.weight_z_score
        result['Hockey Sense Z Score'] = self.hockey_sense_z_score
        result['Skating Z Score'] = self.skating_z_score
        result['Compete Z Score'] = self.compete_z_score
        result['Hockey Strength Z Score'] = self.hockey_strength_z_score
        result['Puck Skills Z Score'] = self.puck_skills_z_score
        result['Game Rating Z Score'] = self.game_rating_z_score
        result['NHL Rating Z Score'] = self.nhl_rating_z_score
        result['Low / Post Play Z Score'] = self.low_post_play_z_score
        result['Technical Z Score'] = self.technical_z_score
        result['Athleticism Z Score'] = self.athleticism_z_score
        result['Puck Handling Z Score'] = self.puck_handling_z_score
        result['Shot Z Score'] = self.shot_z_score
        result['Total Skills Z Score'] = self.total_skills_z_score
        result['BTA Individual Z Score'] = self.bta_individual_z_score
        result['BTA Teammate Z Score'] = self.bta_teammate_z_score
        result['BTA Learner Z Score'] = self.bta_learner_z_score
        result['BTA Leader Z Score'] = self.bta_leader_z_score
        result['BTA Competitor Z Score'] = self.bta_competitor_z_score

        if include_reports:
            report_dict = {}
            for report in self.reports:
                report_dict[str(report.date)] = report.to_dict()

            result['Reports'] = report_dict
        return result

    def __build_from_dict__(self, player_dict, number_of_reports):

        self.hockey_sense = player_dict['Hockey Sense']
        self.skating = player_dict['Skating']
        self.compete = player_dict['Compete']
        self.hockey_strength = player_dict['Hockey Strength']
        self.puck_skills = player_dict['Puck Skills']
        self.game_rating = player_dict['Game Rating']
        self.nhl_rating = player_dict['NHL Rating']
        self.low_post_play = player_dict['Low / Post Play']
        self.technical = player_dict['Technical']
        self.athleticism = player_dict['Athleticism']
        self.puck_handling = player_dict['Puck Handling']
        self.shot = player_dict['Shot']
        self.total_skills = player_dict['Total Skills']

        self.bta_individual = player_dict['BTA Individual']
        self.bta_teammate = player_dict['BTA Teammate']
        self.bta_learner = player_dict['BTA Learner']
        self.bta_leader = player_dict['BTA Leader']
        self.bta_competitor = player_dict['BTA Competitor']

        self.id = player_dict['ID']
        self.fname = player_dict['First Name'].lower()
        self.lname = player_dict['Last Name'].lower()
        self.age = player_dict['Age']
        self.height = player_dict['Height']
        self.weight = player_dict['Weight']
        if str(self.weight) == 'nan':
            self.weight = None
        else:
            if self.weight > 400:
                self.weight = 400
            if self.weight < 70:
                self.weight = 70
        self.rank = player_dict['Rank']
        self.change = player_dict['Change']
        self.shot_side = player_dict['Shot Side']
        self.position = player_dict['Position']
        self.league = player_dict['League']
        self.team = player_dict['Team']
        self.reports = []


        for key in player_dict['Reports'].keys():
            self.reports.append(PlayerReport(player_dict['Reports'][key]))

        self.__set_stats__(number_of_reports)
        self.__set_total_skills__()


        self.age_z_score = player_dict['Age Z Score']
        self.height_z_score = player_dict['Height Z Score']
        self.weight_z_score = player_dict['Weight Z Score']

        self.hockey_sense_z_score = player_dict['Hockey Sense Z Score']
        self.skating_z_score = player_dict['Skating Z Score']
        self.compete_z_score = player_dict['Compete Z Score']
        self.hockey_strength_z_score = player_dict['Hockey Strength Z Score']
        self.puck_skills_z_score = player_dict['Puck Skills Z Score']
        self.game_rating_z_score = player_dict['Game Rating Z Score']
        self.nhl_rating_z_score = player_dict['NHL Rating Z Score']
        self.low_post_play_z_score = player_dict['Low / Post Play Z Score']
        self.technical_z_score = player_dict['Technical Z Score']
        self.athleticism_z_score = player_dict['Athleticism Z Score']
        self.puck_handling_z_score = player_dict['Puck Handling Z Score']
        self.shot_z_score = player_dict['Shot']
        self.total_skills_z_score = player_dict['Total Skills Z Score']

        self.bta_individual_z_score = player_dict['BTA Individual Z Score']
        self.bta_teammate_z_score = player_dict['BTA Teammate Z Score']
        self.bta_learner_z_score = player_dict['BTA Learner Z Score']
        self.bta_leader_z_score = player_dict['BTA Leader Z Score']
        self.bta_competitor_z_score = player_dict['BTA Competitor Z Score']


    def __build_from_df__(self, df, number_of_reports):
        self.id = df.iloc[0]['playerid']
        self.fname = df.iloc[0]['firstname']
        self.lname = df.iloc[0]['lastname']
        self.age = round(int( df.iloc[0]['age'].days) / 365, 2)
        try:
            temp_height = str(df.iloc[0]['height']).split('.')
            self.height = (int(temp_height[0]) * 12) + int(temp_height[1])
        except:
            self.height = 0

        self.weight = df.iloc[0]['weight']
        self.shot_side = df.iloc[0]['shotside']
        self.position = df.iloc[0]['positionname']
        self.league = df.iloc[0]['league_name']
        self.team = df.iloc[0]['currentteamname']
        if self.team is None:
            if df.iloc[0]['home_or_away_team'] == 'Away':
                self.team = df.iloc[0]['awayteamname']
            else:
                self.team = df.iloc[0]['hometeamname']
        self.nhl_rating = None
        self.hockey_sense = None
        self.skating = None
        self.compete = None
        self.hockey_strength = None
        self.puck_skills = None
        self.game_rating = None
        self.low_post_play = None
        self.technical = None
        self.athleticism = None
        self.shot = None
        self.puck_handling = None
        self.total_skills = 0
        self.reports = []

        scout_dfs = mu.split_df_by_value(df, 'scoutid')
        for scout_df in scout_dfs:
            report_dfs = mu.split_df_by_value(scout_df, 'report_date')
            for report_df in report_dfs:
                self.reports.append(PlayerReport(report_df))

        self.__set_stats__(number_of_reports)
        self.__set_total_skills__()

    def __set_stats__(self, number_of_reports):
        nhl_total = 0
        nhl_count = 0
        skating_total = 0
        skating_count = 0
        sense_total = 0
        sense_count = 0
        compete_total = 0
        compete_count = 0
        strength_total = 0
        strength_count = 0
        game_total = 0
        game_count = 0
        puck_total = 0
        puck_count = 0
        low_post_total =0
        low_post_count = 0
        technical_total = 0
        technical_count = 0
        athlete_total = 0
        athlete_count = 0
        puck_handling_total = 0
        puck_handling_count = 0
        shot_total = 0
        shot_count = 0

        loop_count = number_of_reports if number_of_reports > 0 else len(self.reports)

        for i in range(loop_count):
            if i == len(self.reports):
                break
            report = self.reports[i]
            if report.nhl_rating is not None and str(report.nhl_rating) != 'nan':
                nhl_count += 1
                nhl_total += report.nhl_rating
            if report.skating is not None and str(report.skating) != 'nan':
                skating_count += 1
                skating_total += report.skating
            if report.hockey_sense is not None and str(report.hockey_sense) != 'nan':
                sense_count += 1
                sense_total += report.hockey_sense
            if report.compete is not None and str(report.compete) != 'nan':
                compete_count += 1
                compete_total += report.compete
            if report.hockey_strength is not None and str(report.hockey_strength) != 'nan':
                strength_count += 1
                strength_total += report.hockey_strength
            if report.game_rating is not None and str(report.game_rating) != 'nan':
                game_count += 1
                game_total += report.game_rating
            if report.puck_skills is not None and str(report.puck_skills) != 'nan':
                puck_count += 1
                puck_total += report.puck_skills
            if report.low_post_play is not None and str(report.low_post_play) != 'nan':
                low_post_count += 1
                low_post_total += report.low_post_play
            if report.technical is not None and str(report.technical) != 'nan':
                technical_count += 1
                technical_total += report.technical
            if report.athleticism is not None and str(report.athleticism) != 'nan':
                athlete_count += 1
                athlete_total += report.athleticism
            if report.shot is not None and str(report.shot) != 'nan':
                shot_count += 1
                shot_total += report.shot
            if report.puck_handling is not None and str(report.puck_handling) != 'nan':
                puck_handling_count += 1
                puck_handling_total += report.puck_handling

            if nhl_count == 0:
                self.nhl_rating = None
            else:
                self.nhl_rating = nhl_total / nhl_count
            if skating_count == 0:
                self.skating = None
            else:
                self.skating = skating_total / skating_count
            if sense_count == 0:
                self.hockey_sense = None
            else:
                self.hockey_sense = sense_total / sense_count
            if compete_count == 0:
                self.compete = None
            else:
                self.compete = compete_total / compete_count
            if strength_count == 0:
                self.hockey_strength = None
            else:
                self.hockey_strength = strength_total / strength_count
            if game_count == 0:
                self.game_rating = None
            else:
                self.game_rating = game_total / game_count
            if puck_count == 0:
                self.puck_skills = None
            else:
                self.puck_skills = puck_total / puck_count
            if athlete_count == 0:
                self.athleticism = None
            else:
                self.athleticism = athlete_total / athlete_count
            if technical_count == 0:
                self.technical = None
            else:
                self.technical = technical_total / technical_count
            if low_post_count == 0:
                self.low_post_play = None
            else:
                self.low_post_play = low_post_total / low_post_count
            if shot_count == 0:
                self.shot = None
            else:
                self.shot = shot_total / shot_count
            if puck_handling_count == 0:
                self.puck_handling = None
            else:
                self.puck_handling = puck_handling_total / puck_handling_count

    def __set_total_skills__(self):
        self.total_skills = 0
        if self.skating is not None:
            self.total_skills += self.skating
        if self.hockey_sense is not None:
            self.total_skills += self.hockey_sense
        if self.compete is not None:
            self.total_skills += self.compete
        if self.hockey_strength is not None:
            self.total_skills += self.hockey_strength
        if self.puck_skills is not None:
            self.total_skills += self.puck_skills
        if self.technical is not None:
            self.total_skills += self.technical
        if self.athleticism is not None:
            self.total_skills += self.athleticism
        if self.low_post_play is not None:
            self.total_skills += self.low_post_play
        if self.shot is not None:
            self.total_skills += self.shot
        if self.puck_handling is not None:
            self.total_skills += self.puck_handling

class PlayerReport:

    def __init__(self, df):
        if isinstance(df, dict):
            self.__build_from_dict__(df)
        else:
            self.__build_from_df__(df)
        self.total_skills = 0
        self.__set_total_skills__()

    def __str__(self):
        return  'Report Date: ' + self.date + \
                "\n\tnhl rating: " + str(self.nhl_rating) + \
                "\n\thockey sense: " + str(self.hockey_sense) + \
                "\n\tskating: " + str(self.skating) + \
                "\n\tcompete: " + str(self.compete) + \
                "\n\thockey strength: " + str(self.hockey_strength) + \
                "\n\tgame rating: " + str(self.game_rating) + \
                "\n\tpuck skills: " + str(self.puck_skills) + "\n" + \
                "\n\tpuck handling: " + str(self.puck_handling) + "\n" + \
                "\n\tatheticism: " + str(self.athleticism) + "\n" + \
                "\n\tshot: " + str(self.shot) + "\n" + \
                "\n\ttechnical: " + str(self.technical) + "\n" + \
                "\n\tlow / post play: " + str(self.low_post_play) + "\n" + \
                "\n\twas tournament: " + str(self.tournament) + "\n" + \
                "\n\tscout: " + str(self.scout) + "\n" + \
                "\n\tscout type: " + str(self.scout_type) + "\n" + \
                "\n\thome / away: " + str(self.home_away) + "\n" + \
                "\n\tgame id: " + str(self.game_id) + "\n" + \
                "\n\tgame type: " + str(self.game_type) + "\n" + \
                "\n\tlocation: " + self.location + "\n" + \
                "\n\thome team: " + self.home_team + "\n" + \
                "\n\taway team: " + self.away_team + "\n" + \
                "\n\thome city: " + self.home_city + "\n" + \
                "\n\taway city: " + self.away_city + "\n" + \
                "\n\tgame_won: " + str(self.game_won) + "\n"


    def to_dict(self):
        result = {}

        result['Hockey Sense'] = self.hockey_sense
        result['Skating'] = self.skating
        result['Compete'] = self.compete
        result['Hockey Strength'] = self.hockey_strength
        result['Puck Skills'] = self.puck_skills
        result['Game Rating'] = self.game_rating
        result['NHL Rating'] = self.nhl_rating
        result['Low / Post Play'] = self.low_post_play
        result['Technical'] = self.technical
        result['Athleticism'] = self.athleticism
        result['Puck Handling'] = self.puck_handling
        result['Shot'] = self.shot
        result['Date'] = str(self.date)
        result['Scout'] = self.scout
        result['Game_Won'] = self.game_won
        result['Home / Away'] = self.home_away
        result['Scout Type'] = self.scout_type
        result['Tournament'] = self.tournament
        result['Game ID'] = self.game_id
        result['Game Type'] = self.game_type
        result['Location'] = self.location
        result['Home Team'] = self.home_team
        result['Away Team'] = self.away_team
        result['Home City'] = self.home_city
        result['Away City'] = self.away_city

        return result

    def __build_from_df__(self, df):
        self.hockey_sense = None
        self.skating = None
        self.compete = None
        self.hockey_strength = None
        self.puck_skills = None
        self.game_rating = None
        self.nhl_rating = None
        self.low_post_play = None
        self.technical = None
        self.athleticism = None
        self.shot = None
        self.puck_handling = None
        self.scout = df.iloc[0]['scoutname']
        self.date = df.iloc[0]['report_date']
        self.game_won = str(df.iloc[0]['game_won'])
        self.home_away = df.iloc[0]['home_or_away_team']
        self.tournament = "N/A" if df.iloc[0]['tournamentname'] is None else df.iloc[0]['tournamentname']
        self.scout_type = df.iloc[0]['scouttype']
        self.game_id = df.iloc[0]['gameid']
        self.game_type = df.iloc[0]['game_type']
        self.location = df.iloc[0]['location']
        self.home_team = df.iloc[0]['hometeamname']
        self.away_team = df.iloc[0]['awayteamname']
        self.home_city = df.iloc[0]['homecity']
        self.away_city = df.iloc[0]['awaycity']

        self.__get_stats__(df)

    def __build_from_dict__(self, player_dict):
        self.hockey_sense = player_dict['Hockey Sense']
        self.skating = player_dict['Skating']
        self.compete = player_dict['Compete']
        self.hockey_strength = player_dict['Hockey Strength']
        self.puck_skills = player_dict['Puck Skills']
        self.game_rating = player_dict['Game Rating']
        self.nhl_rating = player_dict['NHL Rating']
        self.low_post_play = player_dict['Low / Post Play']
        self.technical = player_dict['Technical']
        self.athleticism = player_dict['Athleticism']
        self.puck_handling = player_dict['Puck Handling']
        self.shot = player_dict['Shot']
        self.date = player_dict['Date']
        self.scout = player_dict['Scout']
        self.game_won = player_dict['Game_Won']
        self.home_away = player_dict['Home / Away']
        self.tournament = player_dict['Tournament']
        self.scout_type = player_dict['Scout Type']
        self.game_id = player_dict['Game ID']
        self.game_type = player_dict['Game Type']
        self.location = player_dict['Location']
        self.home_team = player_dict['Home Team']
        self.away_team = player_dict['Away Team']
        self.home_city = player_dict['Home City']
        self.away_city = player_dict['Away City']

    def __get_stats__(self, df):

        for index, row in df.iterrows():
            if row['rating_type'] == 'Skating':
                self.skating = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Compete':
                self.compete = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'NHL Rating':
                self.nhl_rating = nhl_grade_to_number[row['rating']]
            if row['rating_type'] == 'Hockey Sense':
                self.hockey_sense = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Hockey Strength':
                self.hockey_strength = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Puck Skills':
                self.puck_skills = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Game Rating':
                self.game_rating = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Low/Post Play':
                self.low_post_play = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Technical':
                self.technical = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Athleticism':
                self.athleticism = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Shot':
                self.shot = self.__sanitize_stat__(row['rating'])
            if row['rating_type'] == 'Puck Handling':
                self.puck_handling = self.__sanitize_stat__(row['rating'])

    def __set_total_skills__(self):
        if self.skating is not None:
            self.total_skills += self.skating
        if self.hockey_sense is not None:
            self.total_skills += self.hockey_sense
        if self.compete is not None:
            self.total_skills += self.compete
        if self.hockey_strength is not None:
            self.total_skills += self.hockey_strength
        if self.puck_skills is not None:
            self.total_skills += self.puck_skills
        if self.technical is not None:
            self.total_skills += self.technical
        if self.athleticism is not None:
            self.total_skills += self.athleticism
        if self.low_post_play is not None:
            self.total_skills += self.low_post_play
        if self.shot is not None:
            self.total_skills += self.shot
        if self.puck_handling is not None:
            self.total_skills += self.puck_handling

    def __sanitize_stat__(self, stat):
        try:
            new_stat = float(stat)
            return new_stat
        except:
            return None

class Game:
    def __init__(self):
        self.home_players = {}
        self.away_players = {}
        self.attached_home_players = 0
        self.attached_away_players = 0
        self.home_team = None
        self.away_team = None
        self.home_city = None
        self.away_city = None
        self.date = None
        self.location = None
        self.winning_team = None
        self.game_type = None

    def __repr__(self):
        return "\nhome players: " + str(len(self.home_players)) + \
                "\naway players: " + str(len(self.away_players)) + \
                "\nhome team: " + self.home_team + \
                "\naway team: " + self.away_team + \
                "\nhome city: " + self.home_city + \
                "\ndate: " + str(self.date) + \
                "\nlocation: " + self.location + \
                "\nwinning team: " + self.winning_team + \
                "\ngame type: " + self.game_type

def get_games(path=None, players=None):
    if players is None:
        if path is None:
            raise RuntimeError('path must not be None')
        players = get_players(path)

    games = {}
    for player in players:
        for report in player.reports:
            if report.game_id not in games.keys():
                games[report.game_id] = Game()
                games[report.game_id].date = report.date
                games[report.game_id].game_type = report.game_type
                games[report.game_id].home_team = report.home_team
                games[report.game_id].away_team = report.away_team
                games[report.game_id].home_city = report.home_city
                games[report.game_id].away_city = report.away_city
                games[report.game_id].location = report.location
            if report.home_away == "Home":
                games[report.game_id].home_players[player.id] = player
                if report.game_won:
                    games[report.game_id].winning_team = "Home"
            elif report.home_away == "Away":
                games[report.game_id].away_players[player.id] = player
                if report.game_won:
                    games[report.game_id].winning_team = "Away"

    return games

def get_players(path, number_of_reports=0, less_than_function=None):
    players = []
    with open(path) as json_file:
        players_from_json = json.load(json_file)

    for player in players_from_json:
        players.append(Player(player, number_of_reports, less_than_function))

    players.sort(reverse=True)

    return players

def players_to_df(players):
    result = pd.DataFrame()
    for player in players:
        player_dict = player.to_dict(False)
        player_dict['Full Name'] = player.fname + " " + player.lname
        series = pd.Series(player_dict)
        result = result.append(series, True)

    return result
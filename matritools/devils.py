from matritools import utils as mu
import json
import datetime

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
    'team1': 1,
    'team2': 2,
}

class Player:
    def __init__(self, df, number_of_reports = 0, less_than_function=None):
        self.bta_individual = None
        self.bta_teammate = None
        self.bta_learner = None
        self.bta_leader = None
        self.bta_competitor = None

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

    def __repr__(self, include_reports = False):
        report_str = ""
        if include_reports:
            for report in self.reports:
                report_str += str(report)
            report_str += "\n"

        return  "fname: " + self.fname + "\n" + \
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

    def to_dict(self):
        result = {}

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

        self.fname = player_dict['First Name'].lower()
        self.lname = player_dict['Last Name'].lower()
        self.age = player_dict['Age']
        self.height = player_dict['Height']
        self.weight = player_dict['Weight']
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


    def __build_from_df__(self, df, number_of_reports):
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
            if report.nhl_rating is not None:
                nhl_count += 1
                nhl_total += report.nhl_rating
            if report.skating is not None:
                skating_count += 1
                skating_total += report.skating
            if report.hockey_sense is not None:
                sense_count += 1
                sense_total += report.hockey_sense
            if report.compete is not None:
                compete_count += 1
                compete_total += report.compete
            if report.hockey_strength is not None:
                strength_count += 1
                strength_total += report.hockey_strength
            if report.game_rating is not None:
                game_count += 1
                game_total += report.game_rating
            if report.puck_skills is not None:
                puck_count += 1
                puck_total += report.puck_skills
            if report.low_post_play is not None:
                low_post_count += 1
                low_post_total += report.low_post_play
            if report.technical is not None:
                technical_count += 1
                technical_total += report.technical
            if report.athleticism is not None:
                athlete_count += 1
                athlete_total += report.athleticism
            if report.shot is not None:
                shot_count += 1
                shot_total += report.shot
            if report.puck_handling is not None:
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

    def __get_stats__(self, df):
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
        self.home_players = []
        self.away_players = []
        self.home_team = None
        self.away_team = None
        self.home_city = None
        self.away_city = None
        self.date = None
        self.location = None
        self.game_won = None
        self.game_type = None

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
                games[report.game_id].game_won = report.game_won

            if report.home_away == "Home":
                games[report.game_id].home_team = player.team
            else:
                games[report.game_id].away_team = player.team

def get_players(path, number_of_reports=0, less_than_function=None):
    players = []
    with open(path) as json_file:
        players_from_json = json.load(json_file)

    for player in players_from_json:
        players.append(Player(player, number_of_reports, less_than_function))

    players.sort(reverse=True)

    return players


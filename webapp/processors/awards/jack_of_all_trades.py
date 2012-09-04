
from processors.awards import AwardProcessor,Column,PLAYER_COL
import collections
import math
from models import kits
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of the most distributed use of kits

    Implementation
	store rankings of weapon types and compare rank of attacker and victim weapon types.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jack of All Trades',
                'Most Distributed Use of Kits',
                [PLAYER_COL, Column('Score Deviation', Column.NUMBER, Column.ASC)])

        self.kitScores = dict()
		
    def on_score(self, e):

        if e.player not in self.kitScores:
            self.kitScores[e.player] = collections.Counter()
            self.kitScores[e.player][kits.ASSAULT] = 0
            self.kitScores[e.player][kits.ANTI_TANK] = 0
            self.kitScores[e.player][kits.ENGINEER] = 0
            self.kitScores[e.player][kits.MEDIC] = 0
            self.kitScores[e.player][kits.SNIPER] = 0
            self.kitScores[e.player][kits.SPEC_OPS] = 0
            self.kitScores[e.player][kits.SUPPORT] = 0

        kit = model_mgr.get_kit(e.player.kit_id).kit_type
        if kit not in self.kitScores[e.player]:
            return #empty kit

        self.kitScores[e.player][kit] += e.value

        #change to use numpy?
        scores = []
        totalScore = 0
        for kit in self.kitScores[e.player]:
            score = self.kitScores[e.player][kit]
            if score < 1:
                return #ignore if player unable to score a point with each kit
            scores.append(score)
            totalScore += score

        avg = totalScore / (len(scores) * 1.0)
        totalDev = 0
        for score in scores:
            totalDev += (score - avg) * (score - avg)

        self.results[e.player] = round(math.sqrt(totalDev / (len(scores) * 1.0)))

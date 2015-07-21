from axelrod import Player
import random


class AverageCopier(Player):
    """The player will cooperate with probability p if the opponent's cooperation ratio is p."""

    name = 'Average Copier'
    memoryone = False  # Long memory

    @staticmethod
    def strategy(opponent):
        """Randomly picks a strategy (not affected by history)."""
        if len(opponent.history) == 0:
            return random.choice(['C', 'D'])
        p = sum([s == 'C' for s in opponent.history]) / len(opponent.history)
        rnd_num = random.random()
        if rnd_num < p:
            return 'C'
        return 'D'


class NiceAverageCopier(Player):
    """Same as Average Copier, but always starts by cooperating."""

    name = 'Nice Average Copier'
    memoryone = False  # Long memory

    @staticmethod
    def strategy(opponent):
        """Randomly picks a strategy (not affected by history)."""
        if len(opponent.history) == 0:
            return 'C'
        p = sum([s == 'C' for s in opponent.history]) / len(opponent.history)
        rnd_num = random.random()
        if rnd_num < p:
            return 'C'
        return 'D'

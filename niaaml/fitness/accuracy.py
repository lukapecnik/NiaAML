from sklearn.metrics import accuracy_score
from niaaml.fitness.fitness_function import FitnessFunction

__all__ = ["Accuracy"]


class Accuracy(FitnessFunction):
    r"""Class representing the accuracy as a fitness function.

    Date:
        2020

    Author:
        Luka Pečnik

    License:
        MIT

    Documentation:
        https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html

    See Also:
        * :class:`niaaml.fitness.FitnessFunction`
    """
    Name = "Accuracy"

    def get_fitness(self, predicted, expected):
        r"""Return fitness value. The larger return value should represent a better fitness for the framework to work properly.

        Arguments:
            predicted (pandas.core.series.Series): Predicted values.
            expected (pandas.core.series.Series): Expected values.

        Returns:
            float: Calculated fitness value.
        """
        return accuracy_score(expected, predicted)

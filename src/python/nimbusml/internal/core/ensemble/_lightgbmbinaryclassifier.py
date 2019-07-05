# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LightGbmBinaryClassifier
"""

__all__ = ["LightGbmBinaryClassifier"]


from ...entrypoints.trainers_lightgbmbinaryclassifier import \
    trainers_lightgbmbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class LightGbmBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Gradient Boosted Decision Trees

    .. remarks::
        Light GBM is an open source implementation of boosted trees. It is
        available in nimbusml as a binary classification trainer, a multi-class
        trainer, a regression trainer and a ranking trainer.


        **Reference**

            `GitHub: LightGBM <https://github.com/Microsoft/LightGBM/wiki>`_


    :param number_of_iterations: Number of iterations.

    :param learning_rate: Determines the size of the step taken in the
        direction of the gradient in each step of the learning process.  This
        determines how fast or slow the learner converges on the optimal
        solution. If the step size is too big, you might overshoot the optimal
        solution.  If the step size is too small, training takes longer to
        converge to the best solution.

    :param number_of_leaves: The maximum number of leaves (terminal nodes) that
        can be created in any tree. Higher values potentially increase the size
        of the tree and get better precision, but risk overfitting and
        requiring longer training times.

    :param minimum_example_count_per_leaf: Minimum number of training instances
        required to form a leaf. That is, the minimal number of documents
        allowed in a leaf of regression tree, out of the sub-sampled data. A
        'split' means that features in each level of the tree (node) are
        randomly divided.

    :param booster: Which booster to use. Available options are:

        #. :py:func:`Dart <nimbusml.ensemble.booster.Dart>`
        #. :py:func:`Gbdt <nimbusml.ensemble.booster.Gbdt>`
        #. :py:func:`Goss <nimbusml.ensemble.booster.Goss>`.

    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param unbalanced_sets: Use for binary classification when training data is
        not balanced.

    :param weight_of_positive_examples: Control the balance of positive and
        negative weights, useful for unbalanced classes. A typical value to
        consider: sum(negative cases) / sum(positive cases).

    :param sigmoid: Parameter for the sigmoid function.

    :param evaluation_metric: Evaluation metrics.

    :param maximum_bin_count_per_feature: Maximum number of bucket bin for
        features.

    :param verbose: Verbose.

    :param silent: Printing running messages.

    :param number_of_threads: Number of parallel threads used to run LightGBM.

    :param early_stopping_round: Rounds of early stopping, 0 will disable it.

    :param batch_size: Number of entries in a batch when loading data.

    :param use_categorical_split: Enable categorical split or not.

    :param handle_missing_value: Enable special handling of missing value or
        not.

    :param minimum_example_count_per_group: Minimum number of instances per
        categorical group.

    :param maximum_categorical_split_point_count: Max number of categorical
        thresholds.

    :param categorical_smoothing: Lapalace smooth term in categorical feature
        spilt. Avoid the bias of small categories.

    :param l2_categorical_regularization: L2 Regularization for categorical
        split.

    :param random_state: Sets the random seed for LightGBM to use.

    :param parallel_trainer: Parallel LightGBM Learning Algorithm.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,
        :py:class:`FastForestRegressor <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`Dart <nimbusml.ensemble.booster.Dart>`,
        :py:func:`Goss <nimbusml.ensemble.booster.Goss>`,
        :py:func:`Gbdt <nimbusml.ensemble.booster.Gbdt>`

    .. index:: models, classification, regression

    Example:
       .. literalinclude:: /../nimbusml/examples/LightGbmBinaryClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            number_of_iterations=100,
            learning_rate=None,
            number_of_leaves=None,
            minimum_example_count_per_leaf=None,
            booster=None,
            normalize='Auto',
            caching='Auto',
            unbalanced_sets=False,
            weight_of_positive_examples=1.0,
            sigmoid=0.5,
            evaluation_metric='Default',
            maximum_bin_count_per_feature=255,
            verbose=False,
            silent=True,
            number_of_threads=None,
            early_stopping_round=0,
            batch_size=1048576,
            use_categorical_split=None,
            handle_missing_value=True,
            minimum_example_count_per_group=100,
            maximum_categorical_split_point_count=32,
            categorical_smoothing=10.0,
            l2_categorical_regularization=10.0,
            random_state=None,
            parallel_trainer=None,
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.number_of_iterations = number_of_iterations
        self.learning_rate = learning_rate
        self.number_of_leaves = number_of_leaves
        self.minimum_example_count_per_leaf = minimum_example_count_per_leaf
        self.booster = booster
        self.normalize = normalize
        self.caching = caching
        self.unbalanced_sets = unbalanced_sets
        self.weight_of_positive_examples = weight_of_positive_examples
        self.sigmoid = sigmoid
        self.evaluation_metric = evaluation_metric
        self.maximum_bin_count_per_feature = maximum_bin_count_per_feature
        self.verbose = verbose
        self.silent = silent
        self.number_of_threads = number_of_threads
        self.early_stopping_round = early_stopping_round
        self.batch_size = batch_size
        self.use_categorical_split = use_categorical_split
        self.handle_missing_value = handle_missing_value
        self.minimum_example_count_per_group = minimum_example_count_per_group
        self.maximum_categorical_split_point_count = maximum_categorical_split_point_count
        self.categorical_smoothing = categorical_smoothing
        self.l2_categorical_regularization = l2_categorical_regularization
        self.random_state = random_state
        self.parallel_trainer = parallel_trainer

    @property
    def _entrypoint(self):
        return trainers_lightgbmbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column_name=self._getattr_role('feature_column_name', all_args),
            label_column_name=self._getattr_role('label_column_name', all_args),
            example_weight_column_name=self._getattr_role('example_weight_column_name', all_args),
            row_group_column_name=self._getattr_role('row_group_column_name', all_args),
            number_of_iterations=self.number_of_iterations,
            learning_rate=self.learning_rate,
            number_of_leaves=self.number_of_leaves,
            minimum_example_count_per_leaf=self.minimum_example_count_per_leaf,
            booster=self.booster,
            normalize_features=self.normalize,
            caching=self.caching,
            unbalanced_sets=self.unbalanced_sets,
            weight_of_positive_examples=self.weight_of_positive_examples,
            sigmoid=self.sigmoid,
            evaluation_metric=self.evaluation_metric,
            maximum_bin_count_per_feature=self.maximum_bin_count_per_feature,
            verbose=self.verbose,
            silent=self.silent,
            number_of_threads=self.number_of_threads,
            early_stopping_round=self.early_stopping_round,
            batch_size=self.batch_size,
            use_categorical_split=self.use_categorical_split,
            handle_missing_value=self.handle_missing_value,
            minimum_example_count_per_group=self.minimum_example_count_per_group,
            maximum_categorical_split_point_count=self.maximum_categorical_split_point_count,
            categorical_smoothing=self.categorical_smoothing,
            l2_categorical_regularization=self.l2_categorical_regularization,
            seed=self.random_state,
            parallel_trainer=self.parallel_trainer)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)

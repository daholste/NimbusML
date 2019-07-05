# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TimeSeriesProcessingEntryPoints.SsaForecasting
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def timeseriesprocessingentrypoints_ssaforecasting(
        source,
        data,
        name,
        output_data=None,
        model=None,
        window_size=0,
        series_length=0,
        train_size=0,
        horizon=0,
        confidence_level=0.95,
        variable_horizon=False,
        confidence_lower_bound_column=None,
        confidence_upper_bound_column=None,
        rank_selection_method='Exact',
        rank=None,
        max_rank=None,
        should_stabilize=True,
        should_maintain_info=False,
        max_growth=None,
        discount_factor=1.0,
        is_adaptive=False,
        **params):
    """
    **Description**
        This transform forecasts using Singular Spectrum Analysis (SSA).

    :param source: The name of the source column. (inputs).
    :param data: Input dataset (inputs).
    :param name: The name of the new column. (inputs).
    :param window_size: The length of the window on the series for
        building the trajectory matrix (parameter L). (inputs).
    :param series_length: The length of series that is kept in buffer
        for modeling (parameter N). (inputs).
    :param train_size: The length of series from the begining used
        for training. (inputs).
    :param horizon: The number of values to forecast. (inputs).
    :param confidence_level: The confidence level in [0, 1) for
        forecasting. (inputs).
    :param variable_horizon: Set this to true horizon will change at
        prediction time. (inputs).
    :param confidence_lower_bound_column: The name of the confidence
        interval lower bound column. (inputs).
    :param confidence_upper_bound_column: The name of the confidence
        interval upper bound column. (inputs).
    :param rank_selection_method: The rank selection method.
        (inputs).
    :param rank: The desired rank of the subspace used for SSA
        projection (parameter r). This parameter should be in the
        range in [1, windowSize]. If set to null, the rank is
        automatically determined based on prediction error
        minimization. (inputs).
    :param max_rank: The maximum rank considered during the rank
        selection process. If not provided (i.e. set to null), it is
        set to windowSize - 1. (inputs).
    :param should_stabilize: The flag determining whether the model
        should be stabilized. (inputs).
    :param should_maintain_info: The flag determining whether the
        meta information for the model needs to be maintained.
        (inputs).
    :param max_growth: The maximum growth on the exponential trend.
        (inputs).
    :param discount_factor: The discount factor in [0,1] used for
        online updates. (inputs).
    :param is_adaptive: The flag determing whether the model is
        adaptive (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'TimeSeriesProcessingEntryPoints.SsaForecasting'
    inputs = {}
    outputs = {}

    if source is not None:
        inputs['Source'] = try_set(
            obj=source,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if name is not None:
        inputs['Name'] = try_set(
            obj=name,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if window_size is not None:
        inputs['WindowSize'] = try_set(
            obj=window_size,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if series_length is not None:
        inputs['SeriesLength'] = try_set(
            obj=series_length,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if train_size is not None:
        inputs['TrainSize'] = try_set(
            obj=train_size,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if horizon is not None:
        inputs['Horizon'] = try_set(
            obj=horizon,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if confidence_level is not None:
        inputs['ConfidenceLevel'] = try_set(
            obj=confidence_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if variable_horizon is not None:
        inputs['VariableHorizon'] = try_set(
            obj=variable_horizon,
            none_acceptable=True,
            is_of_type=bool)
    if confidence_lower_bound_column is not None:
        inputs['ConfidenceLowerBoundColumn'] = try_set(
            obj=confidence_lower_bound_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if confidence_upper_bound_column is not None:
        inputs['ConfidenceUpperBoundColumn'] = try_set(
            obj=confidence_upper_bound_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if rank_selection_method is not None:
        inputs['RankSelectionMethod'] = try_set(
            obj=rank_selection_method,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Fixed',
                'Exact',
                'Fast'])
    if rank is not None:
        inputs['Rank'] = try_set(
            obj=rank,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if max_rank is not None:
        inputs['MaxRank'] = try_set(
            obj=max_rank,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if should_stabilize is not None:
        inputs['ShouldStabilize'] = try_set(
            obj=should_stabilize,
            none_acceptable=True,
            is_of_type=bool)
    if should_maintain_info is not None:
        inputs['ShouldMaintainInfo'] = try_set(
            obj=should_maintain_info,
            none_acceptable=True,
            is_of_type=bool)
    if max_growth is not None:
        inputs['MaxGrowth'] = try_set(
            obj=max_growth,
            none_acceptable=True,
            is_of_type=dict,
            field_names=[
                'TimeSpan',
                'Growth'])
    if discount_factor is not None:
        inputs['DiscountFactor'] = try_set(
            obj=discount_factor,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if is_adaptive is not None:
        inputs['IsAdaptive'] = try_set(
            obj=is_adaptive,
            none_acceptable=True,
            is_of_type=bool)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint

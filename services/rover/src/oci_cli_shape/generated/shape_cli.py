# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.rover.src.oci_cli_rover.generated import rover_service_cli


@click.command(cli_util.override('shape.shape_root_group.command_name', 'shape'), cls=CommandGroupWithAlias, help=cli_util.override('shape.shape_root_group.help', """A description of the RoverCloudService API."""), short_help=cli_util.override('shape.shape_root_group.short_help', """RoverCloudService API"""))
@cli_util.help_option_group
def shape_root_group():
    pass


@click.command(cli_util.override('shape.shape_summary_group.command_name', 'shape-summary'), cls=CommandGroupWithAlias, help="""A shape of a node on a Rover device.""")
@cli_util.help_option_group
def shape_summary_group():
    pass


rover_service_cli.rover_service_group.add_command(shape_root_group)
shape_root_group.add_command(shape_summary_group)


@shape_summary_group.command(name=cli_util.override('shape.list_shapes.command_name', 'list-shapes'), help=u"""Returns a list of Shapes. \n[Command Reference](listShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'rover', 'class': 'ShapeCollection'})
@cli_util.wrap_exceptions
def list_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('rover', 'shape', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)

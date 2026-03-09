# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from services.loggingsearch.src.oci_cli_log_search.generated import logsearch_cli
from oci_cli import cli_util, json_skeleton_utils
import click
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli import custom_types  # noqa: F401


# oci loggingsearch search-result search-logs -> oci loggingsearch search-logs
logsearch_cli.logging_search_root_group.commands.pop(logsearch_cli.search_result_group.name)
logsearch_cli.logging_search_root_group.add_command(logsearch_cli.search_logs)


@cli_util.copy_params_from_generated_command(logsearch_cli.search_logs)
@logsearch_cli.logging_search_root_group.command(name=logsearch_cli.search_logs.name)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def search_logs_extended(ctx, from_json, time_start, time_end, search_query, is_return_field_info, limit, page, all_pages):
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['timeStart'] = time_start
    _details['timeEnd'] = time_end
    _details['searchQuery'] = search_query

    if is_return_field_info is not None:
        _details['isReturnFieldInfo'] = is_return_field_info

    client = cli_util.build_client('loggingsearch', 'log_search', ctx)

    response = None

    if all_pages:
      # the SDK's search_logs function does not support the standard OCI pagination
      # so this alternative implementation does that

      subresult = client.search_logs(
        search_logs_details=_details,
        **kwargs
      )

      data = subresult.data.results
      next_page = subresult.next_page
      while next_page:
        subresult = client.search_logs( 
           search_logs_details=_details,
           page=next_page, 
           **kwargs )
        data += subresult.data.results

        next_page = subresult.next_page

      from oci.response import Response
      response = Response(
         status=200,
         headers=subresult.headers,
         request=None,
         data = {
            "fields": None,
            "results": data,
            "summary": {
              "field-count": None,
              "result-count": len(data)
            }
         }
      )

    else:
      response = client.search_logs(
          search_logs_details=_details,
          **kwargs
      )
    
    cli_util.render_response(response, ctx)
       

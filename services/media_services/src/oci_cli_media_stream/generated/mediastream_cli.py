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
from services.media_services.src.oci_cli_media_services.generated import media_services_service_cli


@click.command(cli_util.override('media_stream.media_stream_root_group.command_name', 'media-stream'), cls=CommandGroupWithAlias, help=cli_util.override('media_stream.media_stream_root_group.help', """Media Services (includes Media Flow and Media Streams) is a fully managed service for processing media (video) source content. Use Media Flow and Media Streams to transcode and package digital video using configurable workflows and stream video outputs.

Use the Media Services API to configure media workflows and run Media Flow jobs, create distribution channels, ingest assets, create Preview URLs and play assets. For more information, see [Media Flow] and [Media Streams]."""), short_help=cli_util.override('media_stream.media_stream_root_group.short_help', """Media Services API"""))
@cli_util.help_option_group
def media_stream_root_group():
    pass


@click.command(cli_util.override('media_stream.stream_distribution_channel_group.command_name', 'stream-distribution-channel'), cls=CommandGroupWithAlias, help="""Channel used for delivering video streams to the end-users.""")
@cli_util.help_option_group
def stream_distribution_channel_group():
    pass


media_services_service_cli.media_services_service_group.add_command(media_stream_root_group)
media_stream_root_group.add_command(stream_distribution_channel_group)


@stream_distribution_channel_group.command(name=cli_util.override('media_stream.generate_playlist.command_name', 'generate-playlist'), help=u"""Gets the playlist content for the specified Packaging Configuration and Media Asset combination. \n[Command Reference](generatePlaylist)""")
@cli_util.option('--stream-packaging-config-id', required=True, help=u"""Unique Stream Packaging Configuration identifier.""")
@cli_util.option('--media-asset-id', required=True, help=u"""Unique MediaAsset identifier.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--token', help=u"""Streaming session authentication token.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_playlist(ctx, from_json, file, stream_packaging_config_id, media_asset_id, token):

    kwargs = {}
    if token is not None:
        kwargs['token'] = token
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('media_services', 'media_stream', ctx)
    result = client.generate_playlist(
        stream_packaging_config_id=stream_packaging_config_id,
        media_asset_id=media_asset_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@stream_distribution_channel_group.command(name=cli_util.override('media_stream.generate_session_token.command_name', 'generate-session-token'), help=u"""Generate a new streaming session token. \n[Command Reference](generateSessionToken)""")
@cli_util.option('--scopes', required=True, type=custom_types.CliCaseInsensitiveChoice(["PLAYLIST", "EDGE"]), help=u"""Array of scopes the token can act upon.""")
@cli_util.option('--packaging-config-id', required=True, help=u"""The packaging config resource identifier used to limit the scope of the token.""")
@cli_util.option('--time-expires', type=custom_types.CLI_DATETIME, help=u"""Token expiry time. An RFC3339 formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--asset-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of asset resource IDs used to limit the scope of the token.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-ids': {'module': 'media_services', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-ids': {'module': 'media_services', 'class': 'list[string]'}}, output_type={'module': 'media_services', 'class': 'SessionToken'})
@cli_util.wrap_exceptions
def generate_session_token(ctx, from_json, scopes, packaging_config_id, time_expires, asset_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['scopes'] = cli_util.parse_json_parameter("scopes", scopes)
    _details['packagingConfigId'] = packaging_config_id

    if time_expires is not None:
        _details['timeExpires'] = time_expires

    if asset_ids is not None:
        _details['assetIds'] = cli_util.parse_json_parameter("asset_ids", asset_ids)

    client = cli_util.build_client('media_services', 'media_stream', ctx)
    result = client.generate_session_token(
        generate_session_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)

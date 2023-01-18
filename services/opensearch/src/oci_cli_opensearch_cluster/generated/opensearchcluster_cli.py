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
from services.opensearch.src.oci_cli_opensearch.generated import opensearch_service_cli


@click.command(cli_util.override('opensearch_cluster.opensearch_cluster_root_group.command_name', 'opensearch-cluster'), cls=CommandGroupWithAlias, help=cli_util.override('opensearch_cluster.opensearch_cluster_root_group.help', """The OpenSearch service API provides access to OCI Search Service with OpenSearch."""), short_help=cli_util.override('opensearch_cluster.opensearch_cluster_root_group.short_help', """OpenSearch Service API"""))
@cli_util.help_option_group
def opensearch_cluster_root_group():
    pass


@click.command(cli_util.override('opensearch_cluster.opensearch_cluster_group.command_name', 'opensearch-cluster'), cls=CommandGroupWithAlias, help="""An OpenSearch cluster resource. An OpenSearch cluster is set of instances that provide OpenSearch functionality in OCI Search Service with OpenSearch. For more information, see [About Search Service with OpenSearch].""")
@cli_util.help_option_group
def opensearch_cluster_group():
    pass


@click.command(cli_util.override('opensearch_cluster.work_request_error_collection_group.command_name', 'work-request-error-collection'), cls=CommandGroupWithAlias, help="""The list of work request errors returned in a work request error search.""")
@cli_util.help_option_group
def work_request_error_collection_group():
    pass


@click.command(cli_util.override('opensearch_cluster.work_request_collection_group.command_name', 'work-request-collection'), cls=CommandGroupWithAlias, help="""Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.""")
@cli_util.help_option_group
def work_request_collection_group():
    pass


@click.command(cli_util.override('opensearch_cluster.opensearch_versions_collection_group.command_name', 'opensearch-versions-collection'), cls=CommandGroupWithAlias, help="""The list of OpenSearch versions returned in an OpenSearch version search.""")
@cli_util.help_option_group
def opensearch_versions_collection_group():
    pass


@click.command(cli_util.override('opensearch_cluster.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('opensearch_cluster.opensearch_cluster_collection_group.command_name', 'opensearch-cluster-collection'), cls=CommandGroupWithAlias, help="""The list of OpenSearch clusters returned in a cluster search.""")
@cli_util.help_option_group
def opensearch_cluster_collection_group():
    pass


@click.command(cli_util.override('opensearch_cluster.work_request_log_entry_collection_group.command_name', 'work-request-log-entry-collection'), cls=CommandGroupWithAlias, help="""The list of work request log entries returned in a work request log search.""")
@cli_util.help_option_group
def work_request_log_entry_collection_group():
    pass


opensearch_service_cli.opensearch_service_group.add_command(opensearch_cluster_root_group)
opensearch_cluster_root_group.add_command(opensearch_cluster_group)
opensearch_cluster_root_group.add_command(work_request_error_collection_group)
opensearch_cluster_root_group.add_command(work_request_collection_group)
opensearch_cluster_root_group.add_command(opensearch_versions_collection_group)
opensearch_cluster_root_group.add_command(work_request_group)
opensearch_cluster_root_group.add_command(opensearch_cluster_collection_group)
opensearch_cluster_root_group.add_command(work_request_log_entry_collection_group)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.backup_opensearch_cluster.command_name', 'backup'), help=u"""Backup the opensearch cluster details. \n[Command Reference](backupOpensearchCluster)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the cluster backup is located.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the cluster backup. Avoid entering confidential information.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def backup_opensearch_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, compartment_id, display_name, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.backup_opensearch_cluster(
        opensearch_cluster_id=opensearch_cluster_id,
        backup_opensearch_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.create_opensearch_cluster.command_name', 'create'), help=u"""Creates a new OpensearchCluster. \n[Command Reference](createOpensearchCluster)""")
@cli_util.option('--display-name', required=True, help=u"""The name of the cluster. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to create the cluster in.""")
@cli_util.option('--software-version', required=True, help=u"""The version of the software the cluster is running.""")
@cli_util.option('--master-node-count', required=True, type=click.INT, help=u"""The number of master nodes to configure for the cluster.""")
@cli_util.option('--master-node-host-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FLEX", "BM"]), help=u"""The instance type for the cluster's master nodes.""")
@cli_util.option('--master-node-host-ocpu-count', required=True, type=click.INT, help=u"""The number of OCPUs to configure for the cluser's master nodes.""")
@cli_util.option('--master-node-host-memory-gb', required=True, type=click.INT, help=u"""The amount of memory in GB, to configure per node for the cluster's master nodes.""")
@cli_util.option('--data-node-count', required=True, type=click.INT, help=u"""The number of data nodes to configure for the cluster.""")
@cli_util.option('--data-node-host-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FLEX", "BM"]), help=u"""TThe instance type for the cluster's data nodes.""")
@cli_util.option('--data-node-host-ocpu-count', required=True, type=click.INT, help=u"""The number of OCPUs to configure for the cluster's data nodes.""")
@cli_util.option('--data-node-host-memory-gb', required=True, type=click.INT, help=u"""The amount of memory in GB, to configure per node for the cluster's data nodes.""")
@cli_util.option('--data-node-storage-gb', required=True, type=click.INT, help=u"""The amount of storage in GB, to configure per node for the cluster's data nodes.""")
@cli_util.option('--opendashboard-node-count', required=True, type=click.INT, help=u"""The number of OpenSearch Dashboard nodes to configure for the cluster.""")
@cli_util.option('--opendashboard-node-host-ocpu-count', required=True, type=click.INT, help=u"""The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.""")
@cli_util.option('--opendashboard-node-host-memory-gb', required=True, type=click.INT, help=u"""The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the cluster's VCN.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the cluster's subnet.""")
@cli_util.option('--vcn-compartment-id', required=True, help=u"""The OCID for the compartment where the cluster's VCN is located.""")
@cli_util.option('--subnet-compartment-id', required=True, help=u"""The OCID for the compartment where the cluster's subnet is located.""")
@cli_util.option('--master-node-host-bare-metal-shape', help=u"""The bare metal shape for the cluster's master nodes.""")
@cli_util.option('--data-node-host-bare-metal-shape', help=u"""The bare metal shape for the cluster's data nodes.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_opensearch_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, software_version, master_node_count, master_node_host_type, master_node_host_ocpu_count, master_node_host_memory_gb, data_node_count, data_node_host_type, data_node_host_ocpu_count, data_node_host_memory_gb, data_node_storage_gb, opendashboard_node_count, opendashboard_node_host_ocpu_count, opendashboard_node_host_memory_gb, vcn_id, subnet_id, vcn_compartment_id, subnet_compartment_id, master_node_host_bare_metal_shape, data_node_host_bare_metal_shape, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['softwareVersion'] = software_version
    _details['masterNodeCount'] = master_node_count
    _details['masterNodeHostType'] = master_node_host_type
    _details['masterNodeHostOcpuCount'] = master_node_host_ocpu_count
    _details['masterNodeHostMemoryGB'] = master_node_host_memory_gb
    _details['dataNodeCount'] = data_node_count
    _details['dataNodeHostType'] = data_node_host_type
    _details['dataNodeHostOcpuCount'] = data_node_host_ocpu_count
    _details['dataNodeHostMemoryGB'] = data_node_host_memory_gb
    _details['dataNodeStorageGB'] = data_node_storage_gb
    _details['opendashboardNodeCount'] = opendashboard_node_count
    _details['opendashboardNodeHostOcpuCount'] = opendashboard_node_host_ocpu_count
    _details['opendashboardNodeHostMemoryGB'] = opendashboard_node_host_memory_gb
    _details['vcnId'] = vcn_id
    _details['subnetId'] = subnet_id
    _details['vcnCompartmentId'] = vcn_compartment_id
    _details['subnetCompartmentId'] = subnet_compartment_id

    if master_node_host_bare_metal_shape is not None:
        _details['masterNodeHostBareMetalShape'] = master_node_host_bare_metal_shape

    if data_node_host_bare_metal_shape is not None:
        _details['dataNodeHostBareMetalShape'] = data_node_host_bare_metal_shape

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.create_opensearch_cluster(
        create_opensearch_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.delete_opensearch_cluster.command_name', 'delete'), help=u"""Deletes a OpensearchCluster resource by identifier \n[Command Reference](deleteOpensearchCluster)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_opensearch_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.delete_opensearch_cluster(
        opensearch_cluster_id=opensearch_cluster_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.get_opensearch_cluster.command_name', 'get'), help=u"""Gets a OpensearchCluster by identifier \n[Command Reference](getOpensearchCluster)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'OpensearchCluster'})
@cli_util.wrap_exceptions
def get_opensearch_cluster(ctx, from_json, opensearch_cluster_id):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.get_opensearch_cluster(
        opensearch_cluster_id=opensearch_cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('opensearch_cluster.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@opensearch_cluster_collection_group.command(name=cli_util.override('opensearch_cluster.list_opensearch_clusters.command_name', 'list-opensearch-clusters'), help=u"""Returns a list of OpensearchClusters. \n[Command Reference](listOpensearchClusters)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only OpensearchClusters their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'OpensearchClusterCollection'})
@cli_util.wrap_exceptions
def list_opensearch_clusters(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_opensearch_clusters,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_opensearch_clusters,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_opensearch_clusters(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@opensearch_versions_collection_group.command(name=cli_util.override('opensearch_cluster.list_opensearch_versions.command_name', 'list-opensearch-versions'), help=u"""Lists the supported Opensearch versions \n[Command Reference](listOpensearchVersions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'OpensearchVersionsCollection'})
@cli_util.wrap_exceptions
def list_opensearch_versions(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_opensearch_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_opensearch_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_opensearch_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_collection_group.command(name=cli_util.override('opensearch_cluster.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_collection_group.command(name=cli_util.override('opensearch_cluster.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_collection_group.command(name=cli_util.override('opensearch_cluster.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--source-resource-id', help=u"""The ID of the source resource to list work requests.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opensearch', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, source_resource_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if source_resource_id is not None:
        kwargs['source_resource_id'] = source_resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.opensearch_cluster_restore.command_name', 'opensearch-cluster-restore'), help=u"""Restore the opensearch cluster details. \n[Command Reference](opensearchClusterRestore)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--opensearch-cluster-backup-id', required=True, help=u"""The OCID of the cluster backup to restore.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the cluster backup is located.""")
@cli_util.option('--prefix', help=u"""The prefix for the indices in the cluster backup.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def opensearch_cluster_restore(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, opensearch_cluster_backup_id, compartment_id, prefix, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['opensearchClusterBackupId'] = opensearch_cluster_backup_id
    _details['compartmentId'] = compartment_id

    if prefix is not None:
        _details['prefix'] = prefix

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.opensearch_cluster_restore(
        opensearch_cluster_id=opensearch_cluster_id,
        restore_opensearch_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.resize_opensearch_cluster_horizontal.command_name', 'resize-opensearch-cluster-horizontal'), help=u"""Resize the opensearch cluster horizontal details. \n[Command Reference](resizeOpensearchClusterHorizontal)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--master-node-count', type=click.INT, help=u"""The number of master nodes to configure for the cluster.""")
@cli_util.option('--data-node-count', type=click.INT, help=u"""The number of data nodes to configure for the cluster.""")
@cli_util.option('--opendashboard-node-count', type=click.INT, help=u"""The number of OpenSearch Dashboard nodes to configure for the cluster.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def resize_opensearch_cluster_horizontal(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, master_node_count, data_node_count, opendashboard_node_count, freeform_tags, defined_tags, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if master_node_count is not None:
        _details['masterNodeCount'] = master_node_count

    if data_node_count is not None:
        _details['dataNodeCount'] = data_node_count

    if opendashboard_node_count is not None:
        _details['opendashboardNodeCount'] = opendashboard_node_count

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.resize_opensearch_cluster_horizontal(
        opensearch_cluster_id=opensearch_cluster_id,
        resize_opensearch_cluster_horizontal_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.resize_opensearch_cluster_vertical.command_name', 'resize-opensearch-cluster-vertical'), help=u"""Resize the opensearch cluster vertical details. \n[Command Reference](resizeOpensearchClusterVertical)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--master-node-host-ocpu-count', type=click.INT, help=u"""The number of OCPUs to configure for the cluster's master nodes.""")
@cli_util.option('--master-node-host-memory-gb', type=click.INT, help=u"""The amount of memory in GB, to configure for the cluster's master nodes.""")
@cli_util.option('--data-node-host-ocpu-count', type=click.INT, help=u"""The number of OCPUs to configure for the cluster's data nodes.""")
@cli_util.option('--data-node-host-memory-gb', type=click.INT, help=u"""The amount of memory in GB, to configure for the cluster's data nodes.""")
@cli_util.option('--data-node-storage-gb', type=click.INT, help=u"""The amount of storage in GB, to configure per node for the cluster's data nodes.""")
@cli_util.option('--opendashboard-node-host-ocpu-count', type=click.INT, help=u"""The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.""")
@cli_util.option('--opendashboard-node-host-memory-gb', type=click.INT, help=u"""The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def resize_opensearch_cluster_vertical(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, master_node_host_ocpu_count, master_node_host_memory_gb, data_node_host_ocpu_count, data_node_host_memory_gb, data_node_storage_gb, opendashboard_node_host_ocpu_count, opendashboard_node_host_memory_gb, freeform_tags, defined_tags, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if master_node_host_ocpu_count is not None:
        _details['masterNodeHostOcpuCount'] = master_node_host_ocpu_count

    if master_node_host_memory_gb is not None:
        _details['masterNodeHostMemoryGB'] = master_node_host_memory_gb

    if data_node_host_ocpu_count is not None:
        _details['dataNodeHostOcpuCount'] = data_node_host_ocpu_count

    if data_node_host_memory_gb is not None:
        _details['dataNodeHostMemoryGB'] = data_node_host_memory_gb

    if data_node_storage_gb is not None:
        _details['dataNodeStorageGB'] = data_node_storage_gb

    if opendashboard_node_host_ocpu_count is not None:
        _details['opendashboardNodeHostOcpuCount'] = opendashboard_node_host_ocpu_count

    if opendashboard_node_host_memory_gb is not None:
        _details['opendashboardNodeHostMemoryGB'] = opendashboard_node_host_memory_gb

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.resize_opensearch_cluster_vertical(
        opensearch_cluster_id=opensearch_cluster_id,
        resize_opensearch_cluster_vertical_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@opensearch_cluster_group.command(name=cli_util.override('opensearch_cluster.update_opensearch_cluster.command_name', 'update'), help=u"""Updates the OpensearchCluster \n[Command Reference](updateOpensearchCluster)""")
@cli_util.option('--opensearch-cluster-id', required=True, help=u"""unique OpensearchCluster identifier""")
@cli_util.option('--display-name', required=True, help=u"""The name of the cluster. Avoid entering confidential information.""")
@cli_util.option('--software-version', help=u"""""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opensearch', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opensearch', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_opensearch_cluster(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, opensearch_cluster_id, display_name, software_version, freeform_tags, defined_tags, if_match):

    if isinstance(opensearch_cluster_id, six.string_types) and len(opensearch_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --opensearch-cluster-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if software_version is not None:
        _details['softwareVersion'] = software_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opensearch', 'opensearch_cluster', ctx)
    result = client.update_opensearch_cluster(
        opensearch_cluster_id=opensearch_cluster_id,
        update_opensearch_cluster_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)

# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
IGNORED_COMMANDS = [
    ['setup', 'autocomplete'],
    ['setup', 'bootstrap'],
    ['setup', 'config'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc'],
    ['raw-request'],
    ['session', 'authenticate'],
    ['session', 'export'],
    ['session', 'import'],
    ['session', 'refresh'],
    ['session', 'terminate'],
    ['session', 'validate'],
    ['artifacts', 'container', 'image-signature', 'sign-upload'],
    ['artifacts', 'container', 'image-signature', 'get-verify'],
    # Note this is being added b/c python sdk doesn't generate models
    # for top level enums.
    # This means that the --generate-full-command-json-input will not work
    # for these commands.
    ['cims', 'incident', 'create'],
    ['cims', 'incident', 'update'],
    # DTS commands
    ['dts', 'nfs-dataset', 'activate'],
    ['dts', 'nfs-dataset', 'create'],
    ['dts', 'nfs-dataset', 'deactivate'],
    ['dts', 'nfs-dataset', 'delete'],
    ['dts', 'nfs-dataset', 'get-seal-manifest'],
    ['dts', 'nfs-dataset', 'list'],
    ['dts', 'nfs-dataset', 'reopen'],
    ['dts', 'nfs-dataset', 'seal'],
    ['dts', 'nfs-dataset', 'seal-status'],
    ['dts', 'nfs-dataset', 'set-export'],
    ['dts', 'nfs-dataset', 'show'],
    ['dts', 'physical-appliance', 'list'],
    ['dts', 'physical-appliance', 'show'],
    ['dts', 'physical-appliance', 'unregister'],
    ['dts', 'physical-appliance', 'configure-encryption'],
    ['dts', 'physical-appliance', 'finalize'],
    ['dts', 'physical-appliance', 'initialize-authentication'],
    ['dts', 'physical-appliance', 'unlock'],
    ['dts', 'appliance', 'setup-notifications'],
    ['dts', 'job', 'verify-upload-user-credentials'],
    ['dts', 'job', 'setup-notifications'],
    ['dts', 'export', 'configure-physical-appliance'],
    ['dts', 'export', 'generate-manifest'],
    ['dts', 'export', 'request-appliance'],
    ['dts', 'export', 'create-policy'],
    ['dts', 'export', 'setup-notifications'],
    # TODO: fix this: (was commented out for DEXREQ-825)
    ['ce', 'node-pool', 'create'],
    ['ce', 'cluster', 'generate-token'],
    ['dts', 'appliance', 'show-entitlement'],
    ['os', 'replication', 'list-replication-sources'],
    ['os', 'replication', 'list-replication-policies'],
    ['os', 'replication', 'get-replication-policy'],
    ['os', 'replication', 'delete-replication-policy'],
    ['os', 'replication', 'create-replication-policy'],
    ['os', 'bucket', 'make-bucket-writable'],
    ['os', 'object', 'copy'],
    ['os', 'object', 'copy-part'],
    ['os', 'object', 'head'],
    ['os', 'object', 'merge-object-metadata'],
    ['os', 'object', 'replace-object-metadata'],
    ['os', 'retention-rule', 'update'],
    ['data-flow', 'application', 'create'],
    ['data-flow', 'application', 'update'],
    # input requires a valid file to upload
    ['data-science', 'model', 'create-model-artifact'],
    # this command expects either subnetId or vlanId optional param, therefore, cannot be tested here
    # removing it from here and adding coverage in test_compute_cli_extended.py
    ['compute', 'instance', 'attach-vnic'],
    # added to ignore as JSON can be produced
    ['ce', 'node-pool', 'update'],
    ['db', 'system', 'launch'],
    ['db', 'system', 'update'],
    ['lb', 'load-balancer', 'create'],
    ['network', 'private-endpoint', 'enable-reverse-connections'],
    ['os', 'object', 'reencrypt'],
    ['dns', 'resolver', 'update'],
    ['log-analytics', 'parser', 'list-parser-functions'],
    ['log-analytics', 'parser', 'list-parser-meta-plugins'],
    ['log-analytics', 'source', 'list-meta-source-types'],
    ['log-analytics', 'source', 'list-source-functions'],
    ['log-analytics', 'source', 'list-source-label-operators'],
    ['instance-agent', 'pluginconfig', 'plugin', 'list-instanceagent-available'],
    ['data-integration', 'task-validation', 'create-from-pipeline-task'],
    ['data-integration', 'task', 'update-pipeline-task'],
    ['data-integration', 'task', 'create-pipeline-task'],
    ['dns', 'resolver', 'update'],
    ['resource-manager', 'stack', 'copy'],
    ['log-analytics', 'upload', 'upload-log-file'],
    ['log-analytics', 'upload', 'upload-log-events-file'],
]

IGNORED_COMMANDS_DOCS = [
    ['setup', 'autocomplete'],
    ['setup', 'bootstrap'],
    ['setup', 'config'],
    ['setup', 'keys'],
    ['setup', 'repair-file-permissions'],
    ['setup', 'oci-cli-rc'],
    ['raw-request'],
    ['session', 'authenticate'],
    ['session', 'export'],
    ['session', 'import'],
    ['session', 'refresh'],
    ['session', 'terminate'],
    ['session', 'validate'],
]

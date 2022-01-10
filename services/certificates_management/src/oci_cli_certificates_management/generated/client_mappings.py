# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.certificates_management import CertificatesManagementClient

MODULE_TO_TYPE_MAPPINGS["certificates_management"] = oci.certificates_management.models.certificates_management_type_mapping
if CLIENT_MAP.get("certificates_management") is None:
    CLIENT_MAP["certificates_management"] = {}
CLIENT_MAP["certificates_management"]["certificates_management"] = CertificatesManagementClient

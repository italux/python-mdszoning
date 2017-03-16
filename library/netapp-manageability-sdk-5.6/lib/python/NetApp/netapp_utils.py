############################################################################
# This module was auto-generated on Thu Oct 13 19:24:39 2016
# by using the 'system-api-list' api call from NetApp SDK for python.  
# If you make changes to this module it will likely be broken the next time
# this file is auto-generated.  If you choose to update this file anyway,
# please ensure that you have also updated the generate-api.py script
# to include your new changes.
#
# Also worth mentioning that some of the api calls may not work properly
# and that is because there is no way to easily auto-determine what api
# calls require additional arguments.  If you find one that is broken,
# you may need to manually update this file but that is not recommended.
#
# The goal of this module is to make it easier to develop code since the
# original API requires you to know the exact API calls for interating
# with your NetApp appliance.  The other goal of this module is to ensure
# you can override it instaed of modifying it directly if you find problems.
############################################################################


import sys
from NaElement import *
from NaServer import *
import xmltodict
import unicodedata

conn = None
timeout = 10

def connect(hostname, user, password, minor_version=1, major_version=21):
    global conn
    conn = NaServer(hostname, minor_version, major_version)
    conn.set_server_type('filer')
    conn.set_transport_type('HTTP')
    conn.set_port(80)
    conn.set_style('LOGIN')
    conn.set_admin_user(user, password)
    conn.set_timeout(timeout)
    return conn

def action_test_key_optionality_defaultaction(*args):
    api_call = _invoke_api('action-test-key-optionality-defaultaction', *args)
    return api_call

def active_directory_account_get_iter(*args):
    api_call = _invoke_api('active-directory-account-get-iter', *args)
    return api_call

def aggr_add(*args):
    api_call = _invoke_api('aggr-add', *args)
    return api_call

def aggr_autobalance_aggregate_state_get_iter(*args):
    api_call = _invoke_api('aggr-autobalance-aggregate-state-get-iter', *args)
    return api_call

def aggr_autobalance_config_get(*args):
    api_call = _invoke_api('aggr-autobalance-config-get', *args)
    return api_call

def aggr_autobalance_config_modify(*args):
    api_call = _invoke_api('aggr-autobalance-config-modify', *args)
    return api_call

def aggr_autobalance_notification_get_iter(*args):
    api_call = _invoke_api('aggr-autobalance-notification-get-iter', *args)
    return api_call

def aggr_autobalance_volume_state_get_iter(*args):
    api_call = _invoke_api('aggr-autobalance-volume-state-get-iter', *args)
    return api_call

def aggr_check_spare_low(*args):
    api_call = _invoke_api('aggr-check-spare-low', *args)
    return api_call

def aggr_create(*args):
    api_call = _invoke_api('aggr-create', *args)
    return api_call

def aggr_destroy(*args):
    api_call = _invoke_api('aggr-destroy', *args)
    return api_call

def aggr_get_filer_info(*args):
    api_call = _invoke_api('aggr-get-filer-info', *args)
    return api_call

def aggr_get_iter(*args):
    api_call = _invoke_api('aggr-get-iter', *args)
    return api_call

def aggr_layout_recommendation_get_iter(*args):
    api_call = _invoke_api('aggr-layout-recommendation-get-iter', *args)
    return api_call

def aggr_mirror(*args):
    api_call = _invoke_api('aggr-mirror', *args)
    return api_call

def aggr_modify_raid_type(*args):
    api_call = _invoke_api('aggr-modify-raid-type', *args)
    return api_call

def aggr_offline(*args):
    api_call = _invoke_api('aggr-offline', *args)
    return api_call

def aggr_online(*args):
    api_call = _invoke_api('aggr-online', *args)
    return api_call

def aggr_options_list_info(*args):
    api_call = _invoke_api('aggr-options-list-info', *args)
    return api_call

def aggr_relocation(*args):
    api_call = _invoke_api('aggr-relocation', *args)
    return api_call

def aggr_relocation_status(*args):
    api_call = _invoke_api('aggr-relocation-status', *args)
    return api_call

def aggr_remove_stale_record(*args):
    api_call = _invoke_api('aggr-remove-stale-record', *args)
    return api_call

def aggr_rename(*args):
    api_call = _invoke_api('aggr-rename', *args)
    return api_call

def aggr_restrict(*args):
    api_call = _invoke_api('aggr-restrict', *args)
    return api_call

def aggr_scrub_list_info(*args):
    api_call = _invoke_api('aggr-scrub-list-info', *args)
    return api_call

def aggr_scrub_resume(*args):
    api_call = _invoke_api('aggr-scrub-resume', *args)
    return api_call

def aggr_scrub_start(*args):
    api_call = _invoke_api('aggr-scrub-start', *args)
    return api_call

def aggr_scrub_stop(*args):
    api_call = _invoke_api('aggr-scrub-stop', *args)
    return api_call

def aggr_scrub_suspend(*args):
    api_call = _invoke_api('aggr-scrub-suspend', *args)
    return api_call

def aggr_set_option(*args):
    api_call = _invoke_api('aggr-set-option', *args)
    return api_call

def aggr_space_get_iter(*args):
    api_call = _invoke_api('aggr-space-get-iter', *args)
    return api_call

def aggr_spare_get_iter(*args):
    api_call = _invoke_api('aggr-spare-get-iter', *args)
    return api_call

def aggr_status_get_iter(*args):
    api_call = _invoke_api('aggr-status-get-iter', *args)
    return api_call

def aggr_verify_list_info(*args):
    api_call = _invoke_api('aggr-verify-list-info', *args)
    return api_call

def aggr_verify_resume(*args):
    api_call = _invoke_api('aggr-verify-resume', *args)
    return api_call

def aggr_verify_start(*args):
    api_call = _invoke_api('aggr-verify-start', *args)
    return api_call

def aggr_verify_stop(*args):
    api_call = _invoke_api('aggr-verify-stop', *args)
    return api_call

def aggr_verify_suspend(*args):
    api_call = _invoke_api('aggr-verify-suspend', *args)
    return api_call

def alternate_destroy_iter_1(*args):
    api_call = _invoke_api('alternate-destroy-iter-1', *args)
    return api_call

def alternate_destroy_iter_1_inout(*args):
    api_call = _invoke_api('alternate-destroy-iter-1-inout', *args)
    return api_call

def alternate_get_1(*args):
    api_call = _invoke_api('alternate-get-1', *args)
    return api_call

def alternate_get_1_inout(*args):
    api_call = _invoke_api('alternate-get-1-inout', *args)
    return api_call

def alternate_get_iter_1(*args):
    api_call = _invoke_api('alternate-get-iter-1', *args)
    return api_call

def alternate_get_iter_1_inout(*args):
    api_call = _invoke_api('alternate-get-iter-1-inout', *args)
    return api_call

def alternate_get_iter_2(*args):
    api_call = _invoke_api('alternate-get-iter-2', *args)
    return api_call

def alternate_get_iter_2_inout(*args):
    api_call = _invoke_api('alternate-get-iter-2-inout', *args)
    return api_call

def alternate_modify_iter(*args):
    api_call = _invoke_api('alternate-modify-iter', *args)
    return api_call

def alternate_modify_iter_inout(*args):
    api_call = _invoke_api('alternate-modify-iter-inout', *args)
    return api_call

def antivirus_modify(*args):
    api_call = _invoke_api('antivirus-modify', *args)
    return api_call

def audit_get(*args):
    api_call = _invoke_api('audit-get', *args)
    return api_call

def audit_modify(*args):
    api_call = _invoke_api('audit-modify', *args)
    return api_call

def autogenzapi_create(*args):
    api_call = _invoke_api('autogenzapi-create', *args)
    return api_call

def autogenzapi_destroy(*args):
    api_call = _invoke_api('autogenzapi-destroy', *args)
    return api_call

def autogenzapi_get_iter(*args):
    api_call = _invoke_api('autogenzapi-get-iter', *args)
    return api_call

def autogenzapi_modify(*args):
    api_call = _invoke_api('autogenzapi-modify', *args)
    return api_call

def autogenzapi2_get_iter(*args):
    api_call = _invoke_api('autogenzapi2-get-iter', *args)
    return api_call

def autogenzapi3_create(*args):
    api_call = _invoke_api('autogenzapi3-create', *args)
    return api_call

def autogenzapi3_destroy(*args):
    api_call = _invoke_api('autogenzapi3-destroy', *args)
    return api_call

def autogenzapi3_get_iter(*args):
    api_call = _invoke_api('autogenzapi3-get-iter', *args)
    return api_call

def autogenzapi3_method1(*args):
    api_call = _invoke_api('autogenzapi3-method1', *args)
    return api_call

def autogenzapi3_modify(*args):
    api_call = _invoke_api('autogenzapi3-modify', *args)
    return api_call

def autogenzapiaction_dummy_autozapi_action_cmd(*args):
    api_call = _invoke_api('autogenzapiaction-dummy-autozapi-action-cmd', *args)
    return api_call

def autosupport_budget_get(*args):
    api_call = _invoke_api('autosupport-budget-get', *args)
    return api_call

def autosupport_budget_get_iter(*args):
    api_call = _invoke_api('autosupport-budget-get-iter', *args)
    return api_call

def autosupport_budget_get_total_records(*args):
    api_call = _invoke_api('autosupport-budget-get-total-records', *args)
    return api_call

def autosupport_budget_modify(*args):
    api_call = _invoke_api('autosupport-budget-modify', *args)
    return api_call

def autosupport_check_connectivity(*args):
    api_call = _invoke_api('autosupport-check-connectivity', *args)
    return api_call

def autosupport_check_connectivity_iter(*args):
    api_call = _invoke_api('autosupport-check-connectivity-iter', *args)
    return api_call

def autosupport_check_iter(*args):
    api_call = _invoke_api('autosupport-check-iter', *args)
    return api_call

def autosupport_compliant_get(*args):
    api_call = _invoke_api('autosupport-compliant-get', *args)
    return api_call

def autosupport_compliant_get_iter(*args):
    api_call = _invoke_api('autosupport-compliant-get-iter', *args)
    return api_call

def autosupport_compliant_get_total_records(*args):
    api_call = _invoke_api('autosupport-compliant-get-total-records', *args)
    return api_call

def autosupport_config_get(*args):
    api_call = _invoke_api('autosupport-config-get', *args)
    return api_call

def autosupport_config_get_iter(*args):
    api_call = _invoke_api('autosupport-config-get-iter', *args)
    return api_call

def autosupport_config_get_total_records(*args):
    api_call = _invoke_api('autosupport-config-get-total-records', *args)
    return api_call

def autosupport_config_modify(*args):
    api_call = _invoke_api('autosupport-config-modify', *args)
    return api_call

def autosupport_destinations_get(*args):
    api_call = _invoke_api('autosupport-destinations-get', *args)
    return api_call

def autosupport_destinations_get_iter(*args):
    api_call = _invoke_api('autosupport-destinations-get-iter', *args)
    return api_call

def autosupport_destinations_get_total_records(*args):
    api_call = _invoke_api('autosupport-destinations-get-total-records', *args)
    return api_call

def autosupport_download_get(*args):
    api_call = _invoke_api('autosupport-download-get', *args)
    return api_call

def autosupport_download_get_iter(*args):
    api_call = _invoke_api('autosupport-download-get-iter', *args)
    return api_call

def autosupport_history_cancel(*args):
    api_call = _invoke_api('autosupport-history-cancel', *args)
    return api_call

def autosupport_history_get(*args):
    api_call = _invoke_api('autosupport-history-get', *args)
    return api_call

def autosupport_history_get_iter(*args):
    api_call = _invoke_api('autosupport-history-get-iter', *args)
    return api_call

def autosupport_history_get_total_records(*args):
    api_call = _invoke_api('autosupport-history-get-total-records', *args)
    return api_call

def autosupport_history_retransmit(*args):
    api_call = _invoke_api('autosupport-history-retransmit', *args)
    return api_call

def autosupport_invoke(*args):
    api_call = _invoke_api('autosupport-invoke', *args)
    return api_call

def autosupport_invoke_core_upload(*args):
    api_call = _invoke_api('autosupport-invoke-core-upload', *args)
    return api_call

def autosupport_invoke_diagnostic(*args):
    api_call = _invoke_api('autosupport-invoke-diagnostic', *args)
    return api_call

def autosupport_invoke_performance_archive(*args):
    api_call = _invoke_api('autosupport-invoke-performance-archive', *args)
    return api_call

def autosupport_invoke_splog(*args):
    api_call = _invoke_api('autosupport-invoke-splog', *args)
    return api_call

def autosupport_manifest_get_iter(*args):
    api_call = _invoke_api('autosupport-manifest-get-iter', *args)
    return api_call

def autosupport_manifest_get_total_records(*args):
    api_call = _invoke_api('autosupport-manifest-get-total-records', *args)
    return api_call

def autosupport_trigger_get(*args):
    api_call = _invoke_api('autosupport-trigger-get', *args)
    return api_call

def autosupport_trigger_get_iter(*args):
    api_call = _invoke_api('autosupport-trigger-get-iter', *args)
    return api_call

def autosupport_trigger_get_total_records(*args):
    api_call = _invoke_api('autosupport-trigger-get-total-records', *args)
    return api_call

def autosupport_trigger_modify(*args):
    api_call = _invoke_api('autosupport-trigger-modify', *args)
    return api_call

def autozapiview_get_iter(*args):
    api_call = _invoke_api('autozapiview-get-iter', *args)
    return api_call

def av_get_engine_info(*args):
    api_call = _invoke_api('av-get-engine-info', *args)
    return api_call

def av_get_engine_options(*args):
    api_call = _invoke_api('av-get-engine-options', *args)
    return api_call

def av_get_log(*args):
    api_call = _invoke_api('av-get-log', *args)
    return api_call

def av_get_remedy_info(*args):
    api_call = _invoke_api('av-get-remedy-info', *args)
    return api_call

def av_get_version_info(*args):
    api_call = _invoke_api('av-get-version-info', *args)
    return api_call

def av_log_iter(*args):
    api_call = _invoke_api('av-log-iter', *args)
    return api_call

def av_on_access_policy_get_iter(*args):
    api_call = _invoke_api('av-on-access-policy-get-iter', *args)
    return api_call

def av_on_demand_command_abort(*args):
    api_call = _invoke_api('av-on-demand-command-abort', *args)
    return api_call

def av_on_demand_command_run(*args):
    api_call = _invoke_api('av-on-demand-command-run', *args)
    return api_call

def av_on_demand_command_scan_cluster_create(*args):
    api_call = _invoke_api('av-on-demand-command-scan-cluster-create', *args)
    return api_call

def av_on_demand_command_scan_cluster_delete(*args):
    api_call = _invoke_api('av-on-demand-command-scan-cluster-delete', *args)
    return api_call

def av_on_demand_command_scan_cluster_get(*args):
    api_call = _invoke_api('av-on-demand-command-scan-cluster-get', *args)
    return api_call

def av_on_demand_command_scan_cluster_get_iter(*args):
    api_call = _invoke_api('av-on-demand-command-scan-cluster-get-iter', *args)
    return api_call

def av_on_demand_command_scan_cluster_modify(*args):
    api_call = _invoke_api('av-on-demand-command-scan-cluster-modify', *args)
    return api_call

def av_on_demand_command_scan_dir_get_iter(*args):
    api_call = _invoke_api('av-on-demand-command-scan-dir-get-iter', *args)
    return api_call

def av_on_demand_command_scan_file_get_iter(*args):
    api_call = _invoke_api('av-on-demand-command-scan-file-get-iter', *args)
    return api_call

def av_on_demand_command_scan_vserver_get_iter(*args):
    api_call = _invoke_api('av-on-demand-command-scan-vserver-get-iter', *args)
    return api_call

def av_on_demand_command_schedule(*args):
    api_call = _invoke_api('av-on-demand-command-schedule', *args)
    return api_call

def av_on_demand_command_unschedule(*args):
    api_call = _invoke_api('av-on-demand-command-unschedule', *args)
    return api_call

def av_on_demand_job_get_iter(*args):
    api_call = _invoke_api('av-on-demand-job-get-iter', *args)
    return api_call

def av_on_demand_report_get_iter(*args):
    api_call = _invoke_api('av-on-demand-report-get-iter', *args)
    return api_call

def av_on_demand_report_print(*args):
    api_call = _invoke_api('av-on-demand-report-print', *args)
    return api_call

def av_on_demand_report_upload(*args):
    api_call = _invoke_api('av-on-demand-report-upload', *args)
    return api_call

def av_set_engine_info(*args):
    api_call = _invoke_api('av-set-engine-info', *args)
    return api_call

def av_set_engine_options(*args):
    api_call = _invoke_api('av-set-engine-options', *args)
    return api_call

def av_set_log(*args):
    api_call = _invoke_api('av-set-log', *args)
    return api_call

def av_set_remedy_info(*args):
    api_call = _invoke_api('av-set-remedy-info', *args)
    return api_call

def av_set_version_info(*args):
    api_call = _invoke_api('av-set-version-info', *args)
    return api_call

def av_start_update(*args):
    api_call = _invoke_api('av-start-update', *args)
    return api_call

def capability_can_be_enabled(*args):
    api_call = _invoke_api('capability-can-be-enabled', *args)
    return api_call

def capability_can_be_enabled_shim(*args):
    api_call = _invoke_api('capability-can-be-enabled-shim', *args)
    return api_call

def capability_can_boot_shim(*args):
    api_call = _invoke_api('capability-can-boot-shim', *args)
    return api_call

def capability_can_join_shim(*args):
    api_call = _invoke_api('capability-can-join-shim', *args)
    return api_call

def capability_disable(*args):
    api_call = _invoke_api('capability-disable', *args)
    return api_call

def capability_downgrade_commit_shim(*args):
    api_call = _invoke_api('capability-downgrade-commit-shim', *args)
    return api_call

def capability_downgrade_prepare_shim(*args):
    api_call = _invoke_api('capability-downgrade-prepare-shim', *args)
    return api_call

def capability_enable(*args):
    api_call = _invoke_api('capability-enable', *args)
    return api_call

def capability_get(*args):
    api_call = _invoke_api('capability-get', *args)
    return api_call

def capability_get_cluster_set(*args):
    api_call = _invoke_api('capability-get-cluster-set', *args)
    return api_call

def capability_get_iter(*args):
    api_call = _invoke_api('capability-get-iter', *args)
    return api_call

def capability_is_enabled(*args):
    api_call = _invoke_api('capability-is-enabled', *args)
    return api_call

def capability_is_enabled_during_downgrade_shim(*args):
    api_call = _invoke_api('capability-is-enabled-during-downgrade-shim', *args)
    return api_call

def capability_is_local_node_enable_ready(*args):
    api_call = _invoke_api('capability-is-local-node-enable-ready', *args)
    return api_call

def capability_load_manifest_shim(*args):
    api_call = _invoke_api('capability-load-manifest-shim', *args)
    return api_call

def capability_mark_local_node_enable_ready(*args):
    api_call = _invoke_api('capability-mark-local-node-enable-ready', *args)
    return api_call

def capability_node_disable(*args):
    api_call = _invoke_api('capability-node-disable', *args)
    return api_call

def capability_node_enable(*args):
    api_call = _invoke_api('capability-node-enable', *args)
    return api_call

def capability_node_has_capability(*args):
    api_call = _invoke_api('capability-node-has-capability', *args)
    return api_call

def capability_node_is_enabled(*args):
    api_call = _invoke_api('capability-node-is-enabled', *args)
    return api_call

def capability_recommend_release_shim(*args):
    api_call = _invoke_api('capability-recommend-release-shim', *args)
    return api_call

def capability_replicate_manifest_for_join_shim(*args):
    api_call = _invoke_api('capability-replicate-manifest-for-join-shim', *args)
    return api_call

def capability_software_update_check_shim(*args):
    api_call = _invoke_api('capability-software-update-check-shim', *args)
    return api_call

def cf_aggregate_giveback_status(*args):
    api_call = _invoke_api('cf-aggregate-giveback-status', *args)
    return api_call

def cf_force_takeover(*args):
    api_call = _invoke_api('cf-force-takeover', *args)
    return api_call

def cf_get_iter(*args):
    api_call = _invoke_api('cf-get-iter', *args)
    return api_call

def cf_get_partner(*args):
    api_call = _invoke_api('cf-get-partner', *args)
    return api_call

def cf_giveback(*args):
    api_call = _invoke_api('cf-giveback', *args)
    return api_call

def cf_hwassist_stats(*args):
    api_call = _invoke_api('cf-hwassist-stats', *args)
    return api_call

def cf_hwassist_stats_clear(*args):
    api_call = _invoke_api('cf-hwassist-stats-clear', *args)
    return api_call

def cf_hwassist_status(*args):
    api_call = _invoke_api('cf-hwassist-status', *args)
    return api_call

def cf_hwassist_test(*args):
    api_call = _invoke_api('cf-hwassist-test', *args)
    return api_call

def cf_mode_set(*args):
    api_call = _invoke_api('cf-mode-set', *args)
    return api_call

def cf_modify_iter(*args):
    api_call = _invoke_api('cf-modify-iter', *args)
    return api_call

def cf_service_disable(*args):
    api_call = _invoke_api('cf-service-disable', *args)
    return api_call

def cf_service_enable(*args):
    api_call = _invoke_api('cf-service-enable', *args)
    return api_call

def cf_status(*args):
    api_call = _invoke_api('cf-status', *args)
    return api_call

def cf_takeover(*args):
    api_call = _invoke_api('cf-takeover', *args)
    return api_call

def cf_takeover_status(*args):
    api_call = _invoke_api('cf-takeover-status', *args)
    return api_call

def cifs_branchcache_get_iter(*args):
    api_call = _invoke_api('cifs-branchcache-get-iter', *args)
    return api_call

def cifs_character_mapping_get_iter(*args):
    api_call = _invoke_api('cifs-character-mapping-get-iter', *args)
    return api_call

def cifs_domain_discovered_servers_get_iter(*args):
    api_call = _invoke_api('cifs-domain-discovered-servers-get-iter', *args)
    return api_call

def cifs_domain_name_mapping_search_get_iter(*args):
    api_call = _invoke_api('cifs-domain-name-mapping-search-get-iter', *args)
    return api_call

def cifs_domain_password_schedule_get_iter(*args):
    api_call = _invoke_api('cifs-domain-password-schedule-get-iter', *args)
    return api_call

def cifs_domain_preferred_dc_get_iter(*args):
    api_call = _invoke_api('cifs-domain-preferred-dc-get-iter', *args)
    return api_call

def cifs_domain_trusts_get_iter(*args):
    api_call = _invoke_api('cifs-domain-trusts-get-iter', *args)
    return api_call

def cifs_home_directory_get_iter(*args):
    api_call = _invoke_api('cifs-home-directory-get-iter', *args)
    return api_call

def cifs_home_directory_search_path_get_iter(*args):
    api_call = _invoke_api('cifs-home-directory-search-path-get-iter', *args)
    return api_call

def cifs_local_group_get_iter(*args):
    api_call = _invoke_api('cifs-local-group-get-iter', *args)
    return api_call

def cifs_local_group_members_get_iter(*args):
    api_call = _invoke_api('cifs-local-group-members-get-iter', *args)
    return api_call

def cifs_local_user_get_iter(*args):
    api_call = _invoke_api('cifs-local-user-get-iter', *args)
    return api_call

def cifs_local_user_membership_get_iter(*args):
    api_call = _invoke_api('cifs-local-user-membership-get-iter', *args)
    return api_call

def cifs_nbtstat_get_iter(*args):
    api_call = _invoke_api('cifs-nbtstat-get-iter', *args)
    return api_call

def cifs_options_get_iter(*args):
    api_call = _invoke_api('cifs-options-get-iter', *args)
    return api_call

def cifs_privilege_get_iter(*args):
    api_call = _invoke_api('cifs-privilege-get-iter', *args)
    return api_call

def cifs_security_get_iter(*args):
    api_call = _invoke_api('cifs-security-get-iter', *args)
    return api_call

def cifs_server_get_iter(*args):
    api_call = _invoke_api('cifs-server-get-iter', *args)
    return api_call

def cifs_session_file_get_iter(*args):
    api_call = _invoke_api('cifs-session-file-get-iter', *args)
    return api_call

def cifs_session_get_iter(*args):
    api_call = _invoke_api('cifs-session-get-iter', *args)
    return api_call

def cifs_shadowcopy_add_files(*args):
    api_call = _invoke_api('cifs-shadowcopy-add-files', *args)
    return api_call

def cifs_shadowcopy_ems_get_iter(*args):
    api_call = _invoke_api('cifs-shadowcopy-ems-get-iter', *args)
    return api_call

def cifs_shadowcopy_keep_snapshot(*args):
    api_call = _invoke_api('cifs-shadowcopy-keep-snapshot', *args)
    return api_call

def cifs_shadowcopy_restore_dir(*args):
    api_call = _invoke_api('cifs-shadowcopy-restore-dir', *args)
    return api_call

def cifs_share_access_control_get_iter(*args):
    api_call = _invoke_api('cifs-share-access-control-get-iter', *args)
    return api_call

def cifs_share_get_iter(*args):
    api_call = _invoke_api('cifs-share-get-iter', *args)
    return api_call

def cifs_symlink_get_iter(*args):
    api_call = _invoke_api('cifs-symlink-get-iter', *args)
    return api_call

def clock_get_clock(*args):
    api_call = _invoke_api('clock-get-clock', *args)
    return api_call

def clock_get_timezone(*args):
    api_call = _invoke_api('clock-get-timezone', *args)
    return api_call

def clone_deletion_get_iter(*args):
    api_call = _invoke_api('clone-deletion-get-iter', *args)
    return api_call

def clone_split_load_get_iter(*args):
    api_call = _invoke_api('clone-split-load-get-iter', *args)
    return api_call

def clone_split_load_modify(*args):
    api_call = _invoke_api('clone-split-load-modify', *args)
    return api_call

def clone_token_create(*args):
    api_call = _invoke_api('clone-token-create', *args)
    return api_call

def clone_token_delete(*args):
    api_call = _invoke_api('clone-token-delete', *args)
    return api_call

def clone_token_get(*args):
    api_call = _invoke_api('clone-token-get', *args)
    return api_call

def clone_token_modify_expiry_limit(*args):
    api_call = _invoke_api('clone-token-modify-expiry-limit', *args)
    return api_call

def cluster_application_record_create(*args):
    api_call = _invoke_api('cluster-application-record-create', *args)
    return api_call

def cluster_application_record_delete(*args):
    api_call = _invoke_api('cluster-application-record-delete', *args)
    return api_call

def cluster_application_record_get_iter(*args):
    api_call = _invoke_api('cluster-application-record-get-iter', *args)
    return api_call

def cluster_application_record_modify(*args):
    api_call = _invoke_api('cluster-application-record-modify', *args)
    return api_call

def cluster_contact_get(*args):
    api_call = _invoke_api('cluster-contact-get', *args)
    return api_call

def cluster_contact_modify(*args):
    api_call = _invoke_api('cluster-contact-modify', *args)
    return api_call

def cluster_create(*args):
    api_call = _invoke_api('cluster-create', *args)
    return api_call

def cluster_create_join_progress_get(*args):
    api_call = _invoke_api('cluster-create-join-progress-get', *args)
    return api_call

def cluster_ha_get(*args):
    api_call = _invoke_api('cluster-ha-get', *args)
    return api_call

def cluster_ha_modify(*args):
    api_call = _invoke_api('cluster-ha-modify', *args)
    return api_call

def cluster_identity_get(*args):
    api_call = _invoke_api('cluster-identity-get', *args)
    return api_call

def cluster_identity_modify(*args):
    api_call = _invoke_api('cluster-identity-modify', *args)
    return api_call

def cluster_image_get(*args):
    api_call = _invoke_api('cluster-image-get', *args)
    return api_call

def cluster_image_get_download_progress(*args):
    api_call = _invoke_api('cluster-image-get-download-progress', *args)
    return api_call

def cluster_image_get_iter(*args):
    api_call = _invoke_api('cluster-image-get-iter', *args)
    return api_call

def cluster_image_node_update_progress_info(*args):
    api_call = _invoke_api('cluster-image-node-update-progress-info', *args)
    return api_call

def cluster_image_package_delete(*args):
    api_call = _invoke_api('cluster-image-package-delete', *args)
    return api_call

def cluster_image_package_download(*args):
    api_call = _invoke_api('cluster-image-package-download', *args)
    return api_call

def cluster_image_package_download_abort(*args):
    api_call = _invoke_api('cluster-image-package-download-abort', *args)
    return api_call

def cluster_image_package_local_get(*args):
    api_call = _invoke_api('cluster-image-package-local-get', *args)
    return api_call

def cluster_image_package_local_get_iter(*args):
    api_call = _invoke_api('cluster-image-package-local-get-iter', *args)
    return api_call

def cluster_image_update(*args):
    api_call = _invoke_api('cluster-image-update', *args)
    return api_call

def cluster_image_update_cancel(*args):
    api_call = _invoke_api('cluster-image-update-cancel', *args)
    return api_call

def cluster_image_update_history_get_iter(*args):
    api_call = _invoke_api('cluster-image-update-history-get-iter', *args)
    return api_call

def cluster_image_update_log_get_iter(*args):
    api_call = _invoke_api('cluster-image-update-log-get-iter', *args)
    return api_call

def cluster_image_update_pause(*args):
    api_call = _invoke_api('cluster-image-update-pause', *args)
    return api_call

def cluster_image_update_progress_get_iter(*args):
    api_call = _invoke_api('cluster-image-update-progress-get-iter', *args)
    return api_call

def cluster_image_update_progress_info(*args):
    api_call = _invoke_api('cluster-image-update-progress-info', *args)
    return api_call

def cluster_image_update_resume(*args):
    api_call = _invoke_api('cluster-image-update-resume', *args)
    return api_call

def cluster_image_validate(*args):
    api_call = _invoke_api('cluster-image-validate', *args)
    return api_call

def cluster_join(*args):
    api_call = _invoke_api('cluster-join', *args)
    return api_call

def cluster_log_forward_create(*args):
    api_call = _invoke_api('cluster-log-forward-create', *args)
    return api_call

def cluster_log_forward_destroy(*args):
    api_call = _invoke_api('cluster-log-forward-destroy', *args)
    return api_call

def cluster_log_forward_get(*args):
    api_call = _invoke_api('cluster-log-forward-get', *args)
    return api_call

def cluster_log_forward_get_iter(*args):
    api_call = _invoke_api('cluster-log-forward-get-iter', *args)
    return api_call

def cluster_log_forward_modify(*args):
    api_call = _invoke_api('cluster-log-forward-modify', *args)
    return api_call

def cluster_log_forward_statistics_get(*args):
    api_call = _invoke_api('cluster-log-forward-statistics-get', *args)
    return api_call

def cluster_log_forward_statistics_get_iter(*args):
    api_call = _invoke_api('cluster-log-forward-statistics-get-iter', *args)
    return api_call

def cluster_node_get(*args):
    api_call = _invoke_api('cluster-node-get', *args)
    return api_call

def cluster_node_get_iter(*args):
    api_call = _invoke_api('cluster-node-get-iter', *args)
    return api_call

def cluster_node_modify(*args):
    api_call = _invoke_api('cluster-node-modify', *args)
    return api_call

def cluster_peer_active_address_insert(*args):
    api_call = _invoke_api('cluster-peer-active-address-insert', *args)
    return api_call

def cluster_peer_active_addresses_get(*args):
    api_call = _invoke_api('cluster-peer-active-addresses-get', *args)
    return api_call

def cluster_peer_active_addresses_register(*args):
    api_call = _invoke_api('cluster-peer-active-addresses-register', *args)
    return api_call

def cluster_peer_authn_offer_cancel(*args):
    api_call = _invoke_api('cluster-peer-authn-offer-cancel', *args)
    return api_call

def cluster_peer_authn_offer_get(*args):
    api_call = _invoke_api('cluster-peer-authn-offer-get', *args)
    return api_call

def cluster_peer_authn_offer_get_iter(*args):
    api_call = _invoke_api('cluster-peer-authn-offer-get-iter', *args)
    return api_call

def cluster_peer_authn_offer_modify(*args):
    api_call = _invoke_api('cluster-peer-authn-offer-modify', *args)
    return api_call

def cluster_peer_connection_destroy(*args):
    api_call = _invoke_api('cluster-peer-connection-destroy', *args)
    return api_call

def cluster_peer_connections_get(*args):
    api_call = _invoke_api('cluster-peer-connections-get', *args)
    return api_call

def cluster_peer_connections_get_iter(*args):
    api_call = _invoke_api('cluster-peer-connections-get-iter', *args)
    return api_call

def cluster_peer_create(*args):
    api_call = _invoke_api('cluster-peer-create', *args)
    return api_call

def cluster_peer_delete(*args):
    api_call = _invoke_api('cluster-peer-delete', *args)
    return api_call

def cluster_peer_get(*args):
    api_call = _invoke_api('cluster-peer-get', *args)
    return api_call

def cluster_peer_get_iter(*args):
    api_call = _invoke_api('cluster-peer-get-iter', *args)
    return api_call

def cluster_peer_health_info_get(*args):
    api_call = _invoke_api('cluster-peer-health-info-get', *args)
    return api_call

def cluster_peer_health_info_get_iter(*args):
    api_call = _invoke_api('cluster-peer-health-info-get-iter', *args)
    return api_call

def cluster_peer_modify(*args):
    api_call = _invoke_api('cluster-peer-modify', *args)
    return api_call

def cluster_peer_ping_cluster_peer_test_check_mtu(*args):
    api_call = _invoke_api('cluster-peer-ping-cluster-peer-test-check-mtu', *args)
    return api_call

def cluster_peer_ping_iter(*args):
    api_call = _invoke_api('cluster-peer-ping-iter', *args)
    return api_call

def cluster_peer_policy_get(*args):
    api_call = _invoke_api('cluster-peer-policy-get', *args)
    return api_call

def cluster_peer_policy_modify(*args):
    api_call = _invoke_api('cluster-peer-policy-modify', *args)
    return api_call

def cluster_peer_stable_addresses_get(*args):
    api_call = _invoke_api('cluster-peer-stable-addresses-get', *args)
    return api_call

def cluster_peer_stable_addresses_register(*args):
    api_call = _invoke_api('cluster-peer-stable-addresses-register', *args)
    return api_call

def cluster_unjoin(*args):
    api_call = _invoke_api('cluster-unjoin', *args)
    return api_call

def config_backup_copy(*args):
    api_call = _invoke_api('config-backup-copy', *args)
    return api_call

def config_backup_create(*args):
    api_call = _invoke_api('config-backup-create', *args)
    return api_call

def config_backup_delete(*args):
    api_call = _invoke_api('config-backup-delete', *args)
    return api_call

def config_backup_download(*args):
    api_call = _invoke_api('config-backup-download', *args)
    return api_call

def config_backup_info_get(*args):
    api_call = _invoke_api('config-backup-info-get', *args)
    return api_call

def config_backup_info_get_iter(*args):
    api_call = _invoke_api('config-backup-info-get-iter', *args)
    return api_call

def config_backup_rename(*args):
    api_call = _invoke_api('config-backup-rename', *args)
    return api_call

def config_backup_settings_get(*args):
    api_call = _invoke_api('config-backup-settings-get', *args)
    return api_call

def config_backup_settings_modify(*args):
    api_call = _invoke_api('config-backup-settings-modify', *args)
    return api_call

def config_backup_settings_password_set(*args):
    api_call = _invoke_api('config-backup-settings-password-set', *args)
    return api_call

def config_backup_upload(*args):
    api_call = _invoke_api('config-backup-upload', *args)
    return api_call

def core_segment_config_get(*args):
    api_call = _invoke_api('core-segment-config-get', *args)
    return api_call

def core_segment_config_modify(*args):
    api_call = _invoke_api('core-segment-config-modify', *args)
    return api_call

def core_segment_delete_all(*args):
    api_call = _invoke_api('core-segment-delete-all', *args)
    return api_call

def core_segment_destroy(*args):
    api_call = _invoke_api('core-segment-destroy', *args)
    return api_call

def core_segment_get(*args):
    api_call = _invoke_api('core-segment-get', *args)
    return api_call

def core_segment_get_iter(*args):
    api_call = _invoke_api('core-segment-get-iter', *args)
    return api_call

def core_segment_start(*args):
    api_call = _invoke_api('core-segment-start', *args)
    return api_call

def core_segment_status_get_iter(*args):
    api_call = _invoke_api('core-segment-status-get-iter', *args)
    return api_call

def core_segment_stop(*args):
    api_call = _invoke_api('core-segment-stop', *args)
    return api_call

def coredump_config_get(*args):
    api_call = _invoke_api('coredump-config-get', *args)
    return api_call

def coredump_config_get_iter(*args):
    api_call = _invoke_api('coredump-config-get-iter', *args)
    return api_call

def coredump_config_get_total_records(*args):
    api_call = _invoke_api('coredump-config-get-total-records', *args)
    return api_call

def coredump_config_modify(*args):
    api_call = _invoke_api('coredump-config-modify', *args)
    return api_call

def coredump_config_modify_iter(*args):
    api_call = _invoke_api('coredump-config-modify-iter', *args)
    return api_call

def coredump_delete_all(*args):
    api_call = _invoke_api('coredump-delete-all', *args)
    return api_call

def coredump_delete_core(*args):
    api_call = _invoke_api('coredump-delete-core', *args)
    return api_call

def coredump_delete_core_iter(*args):
    api_call = _invoke_api('coredump-delete-core-iter', *args)
    return api_call

def coredump_get(*args):
    api_call = _invoke_api('coredump-get', *args)
    return api_call

def coredump_get_iter(*args):
    api_call = _invoke_api('coredump-get-iter', *args)
    return api_call

def coredump_get_total_records(*args):
    api_call = _invoke_api('coredump-get-total-records', *args)
    return api_call

def coredump_save_all(*args):
    api_call = _invoke_api('coredump-save-all', *args)
    return api_call

def coredump_save_core(*args):
    api_call = _invoke_api('coredump-save-core', *args)
    return api_call

def coredump_save_core_iter(*args):
    api_call = _invoke_api('coredump-save-core-iter', *args)
    return api_call

def coredump_trigger(*args):
    api_call = _invoke_api('coredump-trigger', *args)
    return api_call

def coredump_upload_core(*args):
    api_call = _invoke_api('coredump-upload-core', *args)
    return api_call

def cost_center_statistics_get(*args):
    api_call = _invoke_api('cost-center-statistics-get', *args)
    return api_call

def cost_center_statistics_get_iter(*args):
    api_call = _invoke_api('cost-center-statistics-get-iter', *args)
    return api_call

def cost_center_statistics_get_total_records(*args):
    api_call = _invoke_api('cost-center-statistics-get-total-records', *args)
    return api_call

def dashboard_alarm_get(*args):
    api_call = _invoke_api('dashboard-alarm-get', *args)
    return api_call

def dashboard_alarm_get_iter(*args):
    api_call = _invoke_api('dashboard-alarm-get-iter', *args)
    return api_call

def dashboard_alarm_get_total_records(*args):
    api_call = _invoke_api('dashboard-alarm-get-total-records', *args)
    return api_call

def dashboard_alarm_threshold_get(*args):
    api_call = _invoke_api('dashboard-alarm-threshold-get', *args)
    return api_call

def dashboard_alarm_threshold_get_iter(*args):
    api_call = _invoke_api('dashboard-alarm-threshold-get-iter', *args)
    return api_call

def dashboard_alarm_threshold_get_total_records(*args):
    api_call = _invoke_api('dashboard-alarm-threshold-get-total-records', *args)
    return api_call

def dashboard_alarm_threshold_modify(*args):
    api_call = _invoke_api('dashboard-alarm-threshold-modify', *args)
    return api_call

def default_destroy_iter(*args):
    api_call = _invoke_api('default-destroy-iter', *args)
    return api_call

def default_destroy_iter_inout(*args):
    api_call = _invoke_api('default-destroy-iter-inout', *args)
    return api_call

def default_get(*args):
    api_call = _invoke_api('default-get', *args)
    return api_call

def default_get_inout(*args):
    api_call = _invoke_api('default-get-inout', *args)
    return api_call

def default_get_iter(*args):
    api_call = _invoke_api('default-get-iter', *args)
    return api_call

def default_get_iter_inout(*args):
    api_call = _invoke_api('default-get-iter-inout', *args)
    return api_call

def default_modify_iter(*args):
    api_call = _invoke_api('default-modify-iter', *args)
    return api_call

def default_modify_iter_inout(*args):
    api_call = _invoke_api('default-modify-iter-inout', *args)
    return api_call

def diagnosis_alert_definition_get(*args):
    api_call = _invoke_api('diagnosis-alert-definition-get', *args)
    return api_call

def diagnosis_alert_definition_get_iter(*args):
    api_call = _invoke_api('diagnosis-alert-definition-get-iter', *args)
    return api_call

def diagnosis_alert_get(*args):
    api_call = _invoke_api('diagnosis-alert-get', *args)
    return api_call

def diagnosis_alert_get_iter(*args):
    api_call = _invoke_api('diagnosis-alert-get-iter', *args)
    return api_call

def diagnosis_alert_modify(*args):
    api_call = _invoke_api('diagnosis-alert-modify', *args)
    return api_call

def diagnosis_config_get(*args):
    api_call = _invoke_api('diagnosis-config-get', *args)
    return api_call

def diagnosis_config_get_iter(*args):
    api_call = _invoke_api('diagnosis-config-get-iter', *args)
    return api_call

def diagnosis_delete_alert(*args):
    api_call = _invoke_api('diagnosis-delete-alert', *args)
    return api_call

def diagnosis_policy_definition_get(*args):
    api_call = _invoke_api('diagnosis-policy-definition-get', *args)
    return api_call

def diagnosis_policy_definition_get_iter(*args):
    api_call = _invoke_api('diagnosis-policy-definition-get-iter', *args)
    return api_call

def diagnosis_policy_modify(*args):
    api_call = _invoke_api('diagnosis-policy-modify', *args)
    return api_call

def diagnosis_status_get(*args):
    api_call = _invoke_api('diagnosis-status-get', *args)
    return api_call

def diagnosis_subscriptions_create(*args):
    api_call = _invoke_api('diagnosis-subscriptions-create', *args)
    return api_call

def diagnosis_subscriptions_get(*args):
    api_call = _invoke_api('diagnosis-subscriptions-get', *args)
    return api_call

def diagnosis_subscriptions_get_iter(*args):
    api_call = _invoke_api('diagnosis-subscriptions-get-iter', *args)
    return api_call

def diagnosis_subscriptions_modify(*args):
    api_call = _invoke_api('diagnosis-subscriptions-modify', *args)
    return api_call

def diagnosis_subsystem_config_get(*args):
    api_call = _invoke_api('diagnosis-subsystem-config-get', *args)
    return api_call

def diagnosis_subsystem_config_get_iter(*args):
    api_call = _invoke_api('diagnosis-subsystem-config-get-iter', *args)
    return api_call

def diagnosis_subsystem_config_modify(*args):
    api_call = _invoke_api('diagnosis-subsystem-config-modify', *args)
    return api_call

def disk_encrypt_get(*args):
    api_call = _invoke_api('disk-encrypt-get', *args)
    return api_call

def disk_encrypt_get_iter(*args):
    api_call = _invoke_api('disk-encrypt-get-iter', *args)
    return api_call

def disk_encrypt_modify(*args):
    api_call = _invoke_api('disk-encrypt-modify', *args)
    return api_call

def disk_encrypt_modify_iter(*args):
    api_call = _invoke_api('disk-encrypt-modify-iter', *args)
    return api_call

def disk_encrypt_sanitize(*args):
    api_call = _invoke_api('disk-encrypt-sanitize', *args)
    return api_call

def disk_encrypt_sanitize_iter(*args):
    api_call = _invoke_api('disk-encrypt-sanitize-iter', *args)
    return api_call

def disk_encrypt_status_get(*args):
    api_call = _invoke_api('disk-encrypt-status-get', *args)
    return api_call

def disk_encrypt_status_get_iter(*args):
    api_call = _invoke_api('disk-encrypt-status-get-iter', *args)
    return api_call

def disk_fail(*args):
    api_call = _invoke_api('disk-fail', *args)
    return api_call

def disk_remove(*args):
    api_call = _invoke_api('disk-remove', *args)
    return api_call

def disk_sanown_assign(*args):
    api_call = _invoke_api('disk-sanown-assign', *args)
    return api_call

def disk_sanown_filer_list_info(*args):
    api_call = _invoke_api('disk-sanown-filer-list-info', *args)
    return api_call

def disk_sanown_list_info(*args):
    api_call = _invoke_api('disk-sanown-list-info', *args)
    return api_call

def disk_sanown_reassign(*args):
    api_call = _invoke_api('disk-sanown-reassign', *args)
    return api_call

def disk_sanown_remove_ownership(*args):
    api_call = _invoke_api('disk-sanown-remove-ownership', *args)
    return api_call

def disk_unfail(*args):
    api_call = _invoke_api('disk-unfail', *args)
    return api_call

def disk_update_disk_fw(*args):
    api_call = _invoke_api('disk-update-disk-fw', *args)
    return api_call

def disk_zero_spares(*args):
    api_call = _invoke_api('disk-zero-spares', *args)
    return api_call

def dummy_addquery_alt_get(*args):
    api_call = _invoke_api('dummy-addquery-alt-get', *args)
    return api_call

def dummy_addquery_create(*args):
    api_call = _invoke_api('dummy-addquery-create', *args)
    return api_call

def dummy_addquery_get_iter(*args):
    api_call = _invoke_api('dummy-addquery-get-iter', *args)
    return api_call

def dummy_addquery_modify(*args):
    api_call = _invoke_api('dummy-addquery-modify', *args)
    return api_call

def dummy_async_volume_create(*args):
    api_call = _invoke_api('dummy-async-volume-create', *args)
    return api_call

def dummy_async_volume_create_args(*args):
    api_call = _invoke_api('dummy-async-volume-create-args', *args)
    return api_call

def dummy_av_get_engine_options(*args):
    api_call = _invoke_api('dummy-av-get-engine-options', *args)
    return api_call

def dummy_av_set_engine_options(*args):
    api_call = _invoke_api('dummy-av-set-engine-options', *args)
    return api_call

def dummy_fcp_create(*args):
    api_call = _invoke_api('dummy-fcp-create', *args)
    return api_call

def dummy_fcp_destroy(*args):
    api_call = _invoke_api('dummy-fcp-destroy', *args)
    return api_call

def dummy_fcp_get_iter(*args):
    api_call = _invoke_api('dummy-fcp-get-iter', *args)
    return api_call

def dummy_file_dummy_read_file(*args):
    api_call = _invoke_api('dummy-file-dummy-read-file', *args)
    return api_call

def dummy_listInfo_only_get(*args):
    api_call = _invoke_api('dummy-listInfo-only-get', *args)
    return api_call

def dummy_listInfo_only_list_info(*args):
    api_call = _invoke_api('dummy-listInfo-only-list-info', *args)
    return api_call

def dummy_quota_create(*args):
    api_call = _invoke_api('dummy-quota-create', *args)
    return api_call

def dummy_quota_destroy(*args):
    api_call = _invoke_api('dummy-quota-destroy', *args)
    return api_call

def dummy_quota_report(*args):
    api_call = _invoke_api('dummy-quota-report', *args)
    return api_call

def dummy_quota_report_no_input(*args):
    api_call = _invoke_api('dummy-quota-report-no-input', *args)
    return api_call

def dummy_storage_initiator_errors_list_info(*args):
    api_call = _invoke_api('dummy-storage-initiator-errors-list-info', *args)
    return api_call

def dummy_storage_initiator_errors_list_info_alt(*args):
    api_call = _invoke_api('dummy-storage-initiator-errors-list-info-alt', *args)
    return api_call

def dummy_storage_initiator_errors_list_info_empty(*args):
    api_call = _invoke_api('dummy-storage-initiator-errors-list-info-empty', *args)
    return api_call

def dummy_vserver_destroy_iter(*args):
    api_call = _invoke_api('dummy-vserver-destroy-iter', *args)
    return api_call

def dummy_vserver_dosomething(*args):
    api_call = _invoke_api('dummy-vserver-dosomething', *args)
    return api_call

def dummy_vserver_family_test_alt_create(*args):
    api_call = _invoke_api('dummy-vserver-family-test-alt-create', *args)
    return api_call

def dummy_vserver_family_test_alt_destroy(*args):
    api_call = _invoke_api('dummy-vserver-family-test-alt-destroy', *args)
    return api_call

def dummy_vserver_family_test_alt_get(*args):
    api_call = _invoke_api('dummy-vserver-family-test-alt-get', *args)
    return api_call

def dummy_vserver_family_test_alt_list_info(*args):
    api_call = _invoke_api('dummy-vserver-family-test-alt-list-info', *args)
    return api_call

def dummy_vserver_family_test_alt_modify(*args):
    api_call = _invoke_api('dummy-vserver-family-test-alt-modify', *args)
    return api_call

def dummy_vserver_family_test_destroy_iter(*args):
    api_call = _invoke_api('dummy-vserver-family-test-destroy-iter', *args)
    return api_call

def dummy_vserver_family_test_get_iter(*args):
    api_call = _invoke_api('dummy-vserver-family-test-get-iter', *args)
    return api_call

def dummy_vserver_family_test_list_info(*args):
    api_call = _invoke_api('dummy-vserver-family-test-list-info', *args)
    return api_call

def dummy_vserver_family_test_modify_iter(*args):
    api_call = _invoke_api('dummy-vserver-family-test-modify-iter', *args)
    return api_call

def dummy_vserver_fcp_list_get_iter(*args):
    api_call = _invoke_api('dummy-vserver-fcp-list-get-iter', *args)
    return api_call

def dummy_vserver_file_dummy_vserver_read_file_alt(*args):
    api_call = _invoke_api('dummy-vserver-file-dummy-vserver-read-file-alt', *args)
    return api_call

def dummy_vserver_get_iter(*args):
    api_call = _invoke_api('dummy-vserver-get-iter', *args)
    return api_call

def dummy_vserver_list_info(*args):
    api_call = _invoke_api('dummy-vserver-list-info', *args)
    return api_call

def dummy_vserver_list_info_1_alt(*args):
    api_call = _invoke_api('dummy-vserver-list-info-1-alt', *args)
    return api_call

def dummy_vserver_list_info_2_alt(*args):
    api_call = _invoke_api('dummy-vserver-list-info-2-alt', *args)
    return api_call

def dummy_vserver_list_info_3_alt(*args):
    api_call = _invoke_api('dummy-vserver-list-info-3-alt', *args)
    return api_call

def dummy_vserver_list_info_alt(*args):
    api_call = _invoke_api('dummy-vserver-list-info-alt', *args)
    return api_call

def dummy_vserver_modify_iter(*args):
    api_call = _invoke_api('dummy-vserver-modify-iter', *args)
    return api_call

def dummy_zapi_delete_async(*args):
    api_call = _invoke_api('dummy-zapi-delete-async', *args)
    return api_call

def dummy_zapi_delete_async_nowait(*args):
    api_call = _invoke_api('dummy-zapi-delete-async-nowait', *args)
    return api_call

def dummy_zapi_delete_async_nowait_returnsok(*args):
    api_call = _invoke_api('dummy-zapi-delete-async-nowait-returnsok', *args)
    return api_call

def dummy_zapi_jobid_async(*args):
    api_call = _invoke_api('dummy-zapi-jobid-async', *args)
    return api_call

def dummy_zapi_jobid_async_nowait(*args):
    api_call = _invoke_api('dummy-zapi-jobid-async-nowait', *args)
    return api_call

def dummy_zapi_key_attribute_specified_type(*args):
    api_call = _invoke_api('dummy-zapi-key-attribute-specified-type', *args)
    return api_call

def dummylun_create(*args):
    api_call = _invoke_api('dummylun-create', *args)
    return api_call

def dummylun_create_by_size(*args):
    api_call = _invoke_api('dummylun-create-by-size', *args)
    return api_call

def dummylun_create_by_size_alt(*args):
    api_call = _invoke_api('dummylun-create-by-size-alt', *args)
    return api_call

def dummylun_destroy_iter(*args):
    api_call = _invoke_api('dummylun-destroy-iter', *args)
    return api_call

def dummylun_get_alt(*args):
    api_call = _invoke_api('dummylun-get-alt', *args)
    return api_call

def dummylun_get_iter(*args):
    api_call = _invoke_api('dummylun-get-iter', *args)
    return api_call

def dummylun_get_iter_alt(*args):
    api_call = _invoke_api('dummylun-get-iter-alt', *args)
    return api_call

def dummylun_list_info(*args):
    api_call = _invoke_api('dummylun-list-info', *args)
    return api_call

def dummylun_list_info_alt(*args):
    api_call = _invoke_api('dummylun-list-info-alt', *args)
    return api_call

def dummylun_list_info_alt1(*args):
    api_call = _invoke_api('dummylun-list-info-alt1', *args)
    return api_call

def dummylun_list_info_alt2(*args):
    api_call = _invoke_api('dummylun-list-info-alt2', *args)
    return api_call

def ems_config_get(*args):
    api_call = _invoke_api('ems-config-get', *args)
    return api_call

def ems_config_modify(*args):
    api_call = _invoke_api('ems-config-modify', *args)
    return api_call

def ems_destination_create(*args):
    api_call = _invoke_api('ems-destination-create', *args)
    return api_call

def ems_destination_destroy(*args):
    api_call = _invoke_api('ems-destination-destroy', *args)
    return api_call

def ems_destination_destroy_iter(*args):
    api_call = _invoke_api('ems-destination-destroy-iter', *args)
    return api_call

def ems_destination_get(*args):
    api_call = _invoke_api('ems-destination-get', *args)
    return api_call

def ems_destination_get_iter(*args):
    api_call = _invoke_api('ems-destination-get-iter', *args)
    return api_call

def ems_destination_modify(*args):
    api_call = _invoke_api('ems-destination-modify', *args)
    return api_call

def ems_destination_modify_iter(*args):
    api_call = _invoke_api('ems-destination-modify-iter', *args)
    return api_call

def ems_mail_history_destroy(*args):
    api_call = _invoke_api('ems-mail-history-destroy', *args)
    return api_call

def ems_mail_history_destroy_iter(*args):
    api_call = _invoke_api('ems-mail-history-destroy-iter', *args)
    return api_call

def ems_mail_history_get(*args):
    api_call = _invoke_api('ems-mail-history-get', *args)
    return api_call

def ems_mail_history_get_iter(*args):
    api_call = _invoke_api('ems-mail-history-get-iter', *args)
    return api_call

def ems_message_get(*args):
    api_call = _invoke_api('ems-message-get', *args)
    return api_call

def ems_message_get_iter(*args):
    api_call = _invoke_api('ems-message-get-iter', *args)
    return api_call

def ems_routing_add_destination(*args):
    api_call = _invoke_api('ems-routing-add-destination', *args)
    return api_call

def ems_routing_get(*args):
    api_call = _invoke_api('ems-routing-get', *args)
    return api_call

def ems_routing_get_iter(*args):
    api_call = _invoke_api('ems-routing-get-iter', *args)
    return api_call

def ems_routing_modify(*args):
    api_call = _invoke_api('ems-routing-modify', *args)
    return api_call

def ems_routing_modify_iter(*args):
    api_call = _invoke_api('ems-routing-modify-iter', *args)
    return api_call

def ems_routing_remove_destination(*args):
    api_call = _invoke_api('ems-routing-remove-destination', *args)
    return api_call

def ems_snmp_history_destroy(*args):
    api_call = _invoke_api('ems-snmp-history-destroy', *args)
    return api_call

def ems_snmp_history_destroy_iter(*args):
    api_call = _invoke_api('ems-snmp-history-destroy-iter', *args)
    return api_call

def ems_snmp_history_get(*args):
    api_call = _invoke_api('ems-snmp-history-get', *args)
    return api_call

def ems_snmp_history_get_iter(*args):
    api_call = _invoke_api('ems-snmp-history-get-iter', *args)
    return api_call

def ems_status_get(*args):
    api_call = _invoke_api('ems-status-get', *args)
    return api_call

def ems_status_get_iter(*args):
    api_call = _invoke_api('ems-status-get-iter', *args)
    return api_call

def environment_sensors_get_iter(*args):
    api_call = _invoke_api('environment-sensors-get-iter', *args)
    return api_call

def event_log_get_iter(*args):
    api_call = _invoke_api('event-log-get-iter', *args)
    return api_call

def export_policy_get_iter(*args):
    api_call = _invoke_api('export-policy-get-iter', *args)
    return api_call

def export_rule_get_create_defaults(*args):
    api_call = _invoke_api('export-rule-get-create-defaults', *args)
    return api_call

def export_rule_get_iter(*args):
    api_call = _invoke_api('export-rule-get-iter', *args)
    return api_call

def exports_access_cache_all_vservers_get(*args):
    api_call = _invoke_api('exports-access-cache-all-vservers-get', *args)
    return api_call

def exports_access_cache_all_vservers_modify(*args):
    api_call = _invoke_api('exports-access-cache-all-vservers-modify', *args)
    return api_call

def external_cache_policy_get(*args):
    api_call = _invoke_api('external-cache-policy-get', *args)
    return api_call

def external_cache_policy_get_iter(*args):
    api_call = _invoke_api('external-cache-policy-get-iter', *args)
    return api_call

def external_cache_policy_modify(*args):
    api_call = _invoke_api('external-cache-policy-modify', *args)
    return api_call

def external_cache_policy_modify_iter(*args):
    api_call = _invoke_api('external-cache-policy-modify-iter', *args)
    return api_call

def fc_config_adapter_disable(*args):
    api_call = _invoke_api('fc-config-adapter-disable', *args)
    return api_call

def fc_config_adapter_enable(*args):
    api_call = _invoke_api('fc-config-adapter-enable', *args)
    return api_call

def fc_config_list_info(*args):
    api_call = _invoke_api('fc-config-list-info', *args)
    return api_call

def fc_config_set_adapter_fc_type(*args):
    api_call = _invoke_api('fc-config-set-adapter-fc-type', *args)
    return api_call

def fcp_adapter_config_down(*args):
    api_call = _invoke_api('fcp-adapter-config-down', *args)
    return api_call

def fcp_adapter_config_up(*args):
    api_call = _invoke_api('fcp-adapter-config-up', *args)
    return api_call

def fcp_adapter_get_iter(*args):
    api_call = _invoke_api('fcp-adapter-get-iter', *args)
    return api_call

def fcp_adapter_set_speed(*args):
    api_call = _invoke_api('fcp-adapter-set-speed', *args)
    return api_call

def fcp_adapter_stats_get_iter(*args):
    api_call = _invoke_api('fcp-adapter-stats-get-iter', *args)
    return api_call

def fcp_initiator_get_iter(*args):
    api_call = _invoke_api('fcp-initiator-get-iter', *args)
    return api_call

def fcp_interface_get_iter(*args):
    api_call = _invoke_api('fcp-interface-get-iter', *args)
    return api_call

def fcp_port_name_get_iter(*args):
    api_call = _invoke_api('fcp-port-name-get-iter', *args)
    return api_call

def fcp_service_get_iter(*args):
    api_call = _invoke_api('fcp-service-get-iter', *args)
    return api_call

def fcp_wwpnalias_get_iter(*args):
    api_call = _invoke_api('fcp-wwpnalias-get-iter', *args)
    return api_call

def fcport_get_link_state(*args):
    api_call = _invoke_api('fcport-get-link-state', *args)
    return api_call

def feature_status_list_info(*args):
    api_call = _invoke_api('feature-status-list-info', *args)
    return api_call

def feature_usage_get_iter(*args):
    api_call = _invoke_api('feature-usage-get-iter', *args)
    return api_call

def feature_usage_summary_get_iter(*args):
    api_call = _invoke_api('feature-usage-summary-get-iter', *args)
    return api_call

def file_assign_qos(*args):
    api_call = _invoke_api('file-assign-qos', *args)
    return api_call

def file_copy_destroy(*args):
    api_call = _invoke_api('file-copy-destroy', *args)
    return api_call

def file_copy_get_iter(*args):
    api_call = _invoke_api('file-copy-get-iter', *args)
    return api_call

def file_copy_start(*args):
    api_call = _invoke_api('file-copy-start', *args)
    return api_call

def file_directory_security_ntfs_dacl_get_iter(*args):
    api_call = _invoke_api('file-directory-security-ntfs-dacl-get-iter', *args)
    return api_call

def file_directory_security_ntfs_get_iter(*args):
    api_call = _invoke_api('file-directory-security-ntfs-get-iter', *args)
    return api_call

def file_directory_security_ntfs_sacl_get_iter(*args):
    api_call = _invoke_api('file-directory-security-ntfs-sacl-get-iter', *args)
    return api_call

def file_directory_security_policy_get_iter(*args):
    api_call = _invoke_api('file-directory-security-policy-get-iter', *args)
    return api_call

def file_directory_security_policy_task_get_iter(*args):
    api_call = _invoke_api('file-directory-security-policy-task-get-iter', *args)
    return api_call

def file_move_destroy(*args):
    api_call = _invoke_api('file-move-destroy', *args)
    return api_call

def file_move_get_iter(*args):
    api_call = _invoke_api('file-move-get-iter', *args)
    return api_call

def file_move_start(*args):
    api_call = _invoke_api('file-move-start', *args)
    return api_call

def fileservice_audit_config_get_iter(*args):
    api_call = _invoke_api('fileservice-audit-config-get-iter', *args)
    return api_call

def fileservice_audit_config_get_total_records(*args):
    api_call = _invoke_api('fileservice-audit-config-get-total-records', *args)
    return api_call

def flash_device_get_iter(*args):
    api_call = _invoke_api('flash-device-get-iter', *args)
    return api_call

def flash_device_list_info(*args):
    api_call = _invoke_api('flash-device-list-info', *args)
    return api_call

def flash_get_thresholds(*args):
    api_call = _invoke_api('flash-get-thresholds', *args)
    return api_call

def flash_thresholds_get_iter(*args):
    api_call = _invoke_api('flash-thresholds-get-iter', *args)
    return api_call

def flexcache_cache_policy_create(*args):
    api_call = _invoke_api('flexcache-cache-policy-create', *args)
    return api_call

def flexcache_cache_policy_destroy(*args):
    api_call = _invoke_api('flexcache-cache-policy-destroy', *args)
    return api_call

def flexcache_cache_policy_get(*args):
    api_call = _invoke_api('flexcache-cache-policy-get', *args)
    return api_call

def flexcache_cache_policy_get_iter(*args):
    api_call = _invoke_api('flexcache-cache-policy-get-iter', *args)
    return api_call

def flexcache_cache_policy_modify(*args):
    api_call = _invoke_api('flexcache-cache-policy-modify', *args)
    return api_call

def flexcache_create(*args):
    api_call = _invoke_api('flexcache-create', *args)
    return api_call

def flexcache_delete(*args):
    api_call = _invoke_api('flexcache-delete', *args)
    return api_call

def flexcache_get_iter(*args):
    api_call = _invoke_api('flexcache-get-iter', *args)
    return api_call

def fpolicy_passthrough_read_connection_get_iter(*args):
    api_call = _invoke_api('fpolicy-passthrough-read-connection-get-iter', *args)
    return api_call

def fpolicy_policy_event_get_iter(*args):
    api_call = _invoke_api('fpolicy-policy-event-get-iter', *args)
    return api_call

def fpolicy_policy_external_engine_get_iter(*args):
    api_call = _invoke_api('fpolicy-policy-external-engine-get-iter', *args)
    return api_call

def fpolicy_policy_get_iter(*args):
    api_call = _invoke_api('fpolicy-policy-get-iter', *args)
    return api_call

def fpolicy_policy_scope_get_iter(*args):
    api_call = _invoke_api('fpolicy-policy-scope-get-iter', *args)
    return api_call

def fpolicy_policy_status_get_iter(*args):
    api_call = _invoke_api('fpolicy-policy-status-get-iter', *args)
    return api_call

def fpolicy_server_status_get_iter(*args):
    api_call = _invoke_api('fpolicy-server-status-get-iter', *args)
    return api_call

def gpo_applied_info_get_iter(*args):
    api_call = _invoke_api('gpo-applied-info-get-iter', *args)
    return api_call

def gpo_get_iter(*args):
    api_call = _invoke_api('gpo-get-iter', *args)
    return api_call

def gpo_gpresult_info_get_iter(*args):
    api_call = _invoke_api('gpo-gpresult-info-get-iter', *args)
    return api_call

def gpo_restricted_group_applied_info_get_iter(*args):
    api_call = _invoke_api('gpo-restricted-group-applied-info-get-iter', *args)
    return api_call

def gpo_restricted_group_defined_info_get_iter(*args):
    api_call = _invoke_api('gpo-restricted-group-defined-info-get-iter', *args)
    return api_call

def group_mapping_get_iter(*args):
    api_call = _invoke_api('group-mapping-get-iter', *args)
    return api_call

def igroup_disable_aix_support(*args):
    api_call = _invoke_api('igroup-disable-aix-support', *args)
    return api_call

def igroup_get_iter(*args):
    api_call = _invoke_api('igroup-get-iter', *args)
    return api_call

def igroup_os_type_list(*args):
    api_call = _invoke_api('igroup-os-type-list', *args)
    return api_call

def interim_license_list_get(*args):
    api_call = _invoke_api('interim-license-list-get', *args)
    return api_call

def interim_license_remove(*args):
    api_call = _invoke_api('interim-license-remove', *args)
    return api_call

def interim_license_set(*args):
    api_call = _invoke_api('interim-license-set', *args)
    return api_call

def iscsi_connection_get_iter(*args):
    api_call = _invoke_api('iscsi-connection-get-iter', *args)
    return api_call

def iscsi_initiator_auth_get_iter(*args):
    api_call = _invoke_api('iscsi-initiator-auth-get-iter', *args)
    return api_call

def iscsi_initiator_get_iter(*args):
    api_call = _invoke_api('iscsi-initiator-get-iter', *args)
    return api_call

def iscsi_interface_accesslist_get_iter(*args):
    api_call = _invoke_api('iscsi-interface-accesslist-get-iter', *args)
    return api_call

def iscsi_interface_get_iter(*args):
    api_call = _invoke_api('iscsi-interface-get-iter', *args)
    return api_call

def iscsi_isns_get_iter(*args):
    api_call = _invoke_api('iscsi-isns-get-iter', *args)
    return api_call

def iscsi_service_get_iter(*args):
    api_call = _invoke_api('iscsi-service-get-iter', *args)
    return api_call

def iscsi_session_get_iter(*args):
    api_call = _invoke_api('iscsi-session-get-iter', *args)
    return api_call

def iscsi_stats_get_iter(*args):
    api_call = _invoke_api('iscsi-stats-get-iter', *args)
    return api_call

def iscsi_tpgroup_get_iter(*args):
    api_call = _invoke_api('iscsi-tpgroup-get-iter', *args)
    return api_call

def job_bad_erase(*args):
    api_call = _invoke_api('job-bad-erase', *args)
    return api_call

def job_bad_get_iter(*args):
    api_call = _invoke_api('job-bad-get-iter', *args)
    return api_call

def job_by_node_get_iter(*args):
    api_call = _invoke_api('job-by-node-get-iter', *args)
    return api_call

def job_completed_get_iter(*args):
    api_call = _invoke_api('job-completed-get-iter', *args)
    return api_call

def job_delete_iter(*args):
    api_call = _invoke_api('job-delete-iter', *args)
    return api_call

def job_expunge_iter(*args):
    api_call = _invoke_api('job-expunge-iter', *args)
    return api_call

def job_get_iter(*args):
    api_call = _invoke_api('job-get-iter', *args)
    return api_call

def job_history_get_iter(*args):
    api_call = _invoke_api('job-history-get-iter', *args)
    return api_call

def job_init_state_get(*args):
    api_call = _invoke_api('job-init-state-get', *args)
    return api_call

def job_init_state_get_iter(*args):
    api_call = _invoke_api('job-init-state-get-iter', *args)
    return api_call

def job_kick(*args):
    api_call = _invoke_api('job-kick', *args)
    return api_call

def job_pause_iter(*args):
    api_call = _invoke_api('job-pause-iter', *args)
    return api_call

def job_private_completed_get_iter(*args):
    api_call = _invoke_api('job-private-completed-get-iter', *args)
    return api_call

def job_private_delete_iter(*args):
    api_call = _invoke_api('job-private-delete-iter', *args)
    return api_call

def job_private_get_iter(*args):
    api_call = _invoke_api('job-private-get-iter', *args)
    return api_call

def job_private_pause_iter(*args):
    api_call = _invoke_api('job-private-pause-iter', *args)
    return api_call

def job_private_resume_iter(*args):
    api_call = _invoke_api('job-private-resume-iter', *args)
    return api_call

def job_private_soft_pause_iter(*args):
    api_call = _invoke_api('job-private-soft-pause-iter', *args)
    return api_call

def job_private_stop_iter(*args):
    api_call = _invoke_api('job-private-stop-iter', *args)
    return api_call

def job_queue_get(*args):
    api_call = _invoke_api('job-queue-get', *args)
    return api_call

def job_queue_get_iter(*args):
    api_call = _invoke_api('job-queue-get-iter', *args)
    return api_call

def job_resume_iter(*args):
    api_call = _invoke_api('job-resume-iter', *args)
    return api_call

def job_schedule_consumer_get(*args):
    api_call = _invoke_api('job-schedule-consumer-get', *args)
    return api_call

def job_schedule_consumer_get_iter(*args):
    api_call = _invoke_api('job-schedule-consumer-get-iter', *args)
    return api_call

def job_schedule_cron_create(*args):
    api_call = _invoke_api('job-schedule-cron-create', *args)
    return api_call

def job_schedule_cron_destroy(*args):
    api_call = _invoke_api('job-schedule-cron-destroy', *args)
    return api_call

def job_schedule_cron_destroy_iter(*args):
    api_call = _invoke_api('job-schedule-cron-destroy-iter', *args)
    return api_call

def job_schedule_cron_get(*args):
    api_call = _invoke_api('job-schedule-cron-get', *args)
    return api_call

def job_schedule_cron_get_iter(*args):
    api_call = _invoke_api('job-schedule-cron-get-iter', *args)
    return api_call

def job_schedule_cron_modify(*args):
    api_call = _invoke_api('job-schedule-cron-modify', *args)
    return api_call

def job_schedule_get(*args):
    api_call = _invoke_api('job-schedule-get', *args)
    return api_call

def job_schedule_get_iter(*args):
    api_call = _invoke_api('job-schedule-get-iter', *args)
    return api_call

def job_schedule_interval_create(*args):
    api_call = _invoke_api('job-schedule-interval-create', *args)
    return api_call

def job_schedule_interval_destroy(*args):
    api_call = _invoke_api('job-schedule-interval-destroy', *args)
    return api_call

def job_schedule_interval_destroy_iter(*args):
    api_call = _invoke_api('job-schedule-interval-destroy-iter', *args)
    return api_call

def job_schedule_interval_get(*args):
    api_call = _invoke_api('job-schedule-interval-get', *args)
    return api_call

def job_schedule_interval_get_iter(*args):
    api_call = _invoke_api('job-schedule-interval-get-iter', *args)
    return api_call

def job_schedule_interval_modify(*args):
    api_call = _invoke_api('job-schedule-interval-modify', *args)
    return api_call

def job_soft_pause_iter(*args):
    api_call = _invoke_api('job-soft-pause-iter', *args)
    return api_call

def job_stop_iter(*args):
    api_call = _invoke_api('job-stop-iter', *args)
    return api_call

def job_type_by_category_get(*args):
    api_call = _invoke_api('job-type-by-category-get', *args)
    return api_call

def job_type_by_category_get_iter(*args):
    api_call = _invoke_api('job-type-by-category-get-iter', *args)
    return api_call

def job_type_get(*args):
    api_call = _invoke_api('job-type-get', *args)
    return api_call

def job_type_get_iter(*args):
    api_call = _invoke_api('job-type-get-iter', *args)
    return api_call

def job_unclaim_iter(*args):
    api_call = _invoke_api('job-unclaim-iter', *args)
    return api_call

def kerberos_config_get_iter(*args):
    api_call = _invoke_api('kerberos-config-get-iter', *args)
    return api_call

def kerberos_realm_create(*args):
    api_call = _invoke_api('kerberos-realm-create', *args)
    return api_call

def kerberos_realm_delete(*args):
    api_call = _invoke_api('kerberos-realm-delete', *args)
    return api_call

def kerberos_realm_get_iter(*args):
    api_call = _invoke_api('kerberos-realm-get-iter', *args)
    return api_call

def kerberos_realm_modify(*args):
    api_call = _invoke_api('kerberos-realm-modify', *args)
    return api_call

def ldap_client_get_iter(*args):
    api_call = _invoke_api('ldap-client-get-iter', *args)
    return api_call

def ldap_client_schema_get_iter(*args):
    api_call = _invoke_api('ldap-client-schema-get-iter', *args)
    return api_call

def ldap_config_get_iter(*args):
    api_call = _invoke_api('ldap-config-get-iter', *args)
    return api_call

def license_v2_add(*args):
    api_call = _invoke_api('license-v2-add', *args)
    return api_call

def license_v2_cleanup_list_info(*args):
    api_call = _invoke_api('license-v2-cleanup-list-info', *args)
    return api_call

def license_v2_delete(*args):
    api_call = _invoke_api('license-v2-delete', *args)
    return api_call

def license_v2_delete_expired(*args):
    api_call = _invoke_api('license-v2-delete-expired', *args)
    return api_call

def license_v2_delete_unused(*args):
    api_call = _invoke_api('license-v2-delete-unused', *args)
    return api_call

def license_v2_entitlement_risk_get_iter(*args):
    api_call = _invoke_api('license-v2-entitlement-risk-get-iter', *args)
    return api_call

def license_v2_list_info(*args):
    api_call = _invoke_api('license-v2-list-info', *args)
    return api_call

def license_v2_status_list_info(*args):
    api_call = _invoke_api('license-v2-status-list-info', *args)
    return api_call

def lock_break_iter(*args):
    api_call = _invoke_api('lock-break-iter', *args)
    return api_call

def lock_get_iter(*args):
    api_call = _invoke_api('lock-get-iter', *args)
    return api_call

def lun_alignment_get_iter(*args):
    api_call = _invoke_api('lun-alignment-get-iter', *args)
    return api_call

def lun_bind_get_iter(*args):
    api_call = _invoke_api('lun-bind-get-iter', *args)
    return api_call

def lun_copy_cancel(*args):
    api_call = _invoke_api('lun-copy-cancel', *args)
    return api_call

def lun_copy_get_iter(*args):
    api_call = _invoke_api('lun-copy-get-iter', *args)
    return api_call

def lun_copy_modify(*args):
    api_call = _invoke_api('lun-copy-modify', *args)
    return api_call

def lun_copy_pause(*args):
    api_call = _invoke_api('lun-copy-pause', *args)
    return api_call

def lun_copy_resume(*args):
    api_call = _invoke_api('lun-copy-resume', *args)
    return api_call

def lun_copy_start(*args):
    api_call = _invoke_api('lun-copy-start', *args)
    return api_call

def lun_debug_get(*args):
    api_call = _invoke_api('lun-debug-get', *args)
    return api_call

def lun_get_iter(*args):
    api_call = _invoke_api('lun-get-iter', *args)
    return api_call

def lun_get_vdisk_attributes(*args):
    api_call = _invoke_api('lun-get-vdisk-attributes', *args)
    return api_call

def lun_group_internal_rebuild(*args):
    api_call = _invoke_api('lun-group-internal-rebuild', *args)
    return api_call

def lun_import_create(*args):
    api_call = _invoke_api('lun-import-create', *args)
    return api_call

def lun_import_delete(*args):
    api_call = _invoke_api('lun-import-delete', *args)
    return api_call

def lun_import_get_iter(*args):
    api_call = _invoke_api('lun-import-get-iter', *args)
    return api_call

def lun_import_pause(*args):
    api_call = _invoke_api('lun-import-pause', *args)
    return api_call

def lun_import_resume(*args):
    api_call = _invoke_api('lun-import-resume', *args)
    return api_call

def lun_import_start(*args):
    api_call = _invoke_api('lun-import-start', *args)
    return api_call

def lun_import_stop(*args):
    api_call = _invoke_api('lun-import-stop', *args)
    return api_call

def lun_import_throttle(*args):
    api_call = _invoke_api('lun-import-throttle', *args)
    return api_call

def lun_import_verify_start(*args):
    api_call = _invoke_api('lun-import-verify-start', *args)
    return api_call

def lun_import_verify_stop(*args):
    api_call = _invoke_api('lun-import-verify-stop', *args)
    return api_call

def lun_initiator_list_map_info(*args):
    api_call = _invoke_api('lun-initiator-list-map-info', *args)
    return api_call

def lun_map_get_iter(*args):
    api_call = _invoke_api('lun-map-get-iter', *args)
    return api_call

def lun_move_get_iter(*args):
    api_call = _invoke_api('lun-move-get-iter', *args)
    return api_call

def lun_os_type_list(*args):
    api_call = _invoke_api('lun-os-type-list', *args)
    return api_call

def lun_prepare_to_downgrade(*args):
    api_call = _invoke_api('lun-prepare-to-downgrade', *args)
    return api_call

def lun_stats_get_iter(*args):
    api_call = _invoke_api('lun-stats-get-iter', *args)
    return api_call

def lun_test_vdisk_size(*args):
    api_call = _invoke_api('lun-test-vdisk-size', *args)
    return api_call

def lun_transition_7mode_destroy(*args):
    api_call = _invoke_api('lun-transition-7mode-destroy', *args)
    return api_call

def lun_transition_7mode_get_iter(*args):
    api_call = _invoke_api('lun-transition-7mode-get-iter', *args)
    return api_call

def lun_transition_start(*args):
    api_call = _invoke_api('lun-transition-start', *args)
    return api_call

def lun_transition_volume_get_iter(*args):
    api_call = _invoke_api('lun-transition-volume-get-iter', *args)
    return api_call

def memoryperf_run(*args):
    api_call = _invoke_api('memoryperf-run', *args)
    return api_call

def method_for_key_optionality_default(*args):
    api_call = _invoke_api('method-for-key-optionality-default', *args)
    return api_call

def metrocluster_check_aggregate_eligibility_get(*args):
    api_call = _invoke_api('metrocluster-check-aggregate-eligibility-get', *args)
    return api_call

def metrocluster_check_aggregate_eligibility_get_iter(*args):
    api_call = _invoke_api('metrocluster-check-aggregate-eligibility-get-iter', *args)
    return api_call

def metrocluster_check_aggregate_get_iter(*args):
    api_call = _invoke_api('metrocluster-check-aggregate-get-iter', *args)
    return api_call

def metrocluster_check_capture_status_get(*args):
    api_call = _invoke_api('metrocluster-check-capture-status-get', *args)
    return api_call

def metrocluster_check_cluster_get_iter(*args):
    api_call = _invoke_api('metrocluster-check-cluster-get-iter', *args)
    return api_call

def metrocluster_check_config_replication_get(*args):
    api_call = _invoke_api('metrocluster-check-config-replication-get', *args)
    return api_call

def metrocluster_check_get_iter(*args):
    api_call = _invoke_api('metrocluster-check-get-iter', *args)
    return api_call

def metrocluster_check_lif_repair_placement(*args):
    api_call = _invoke_api('metrocluster-check-lif-repair-placement', *args)
    return api_call

def metrocluster_check_node_get_iter(*args):
    api_call = _invoke_api('metrocluster-check-node-get-iter', *args)
    return api_call

def metrocluster_check_run(*args):
    api_call = _invoke_api('metrocluster-check-run', *args)
    return api_call

def metrocluster_config_diff_get(*args):
    api_call = _invoke_api('metrocluster-config-diff-get', *args)
    return api_call

def metrocluster_config_diff_get_iter(*args):
    api_call = _invoke_api('metrocluster-config-diff-get-iter', *args)
    return api_call

def metrocluster_config_replication_cluster_storage_configuration_get(*args):
    api_call = _invoke_api('metrocluster-config-replication-cluster-storage-configuration-get', *args)
    return api_call

def metrocluster_config_replication_cluster_storage_configuration_modify(*args):
    api_call = _invoke_api('metrocluster-config-replication-cluster-storage-configuration-modify', *args)
    return api_call

def metrocluster_config_replication_resync_status_get(*args):
    api_call = _invoke_api('metrocluster-config-replication-resync-status-get', *args)
    return api_call

def metrocluster_configure(*args):
    api_call = _invoke_api('metrocluster-configure', *args)
    return api_call

def metrocluster_disable(*args):
    api_call = _invoke_api('metrocluster-disable', *args)
    return api_call

def metrocluster_get(*args):
    api_call = _invoke_api('metrocluster-get', *args)
    return api_call

def metrocluster_heal(*args):
    api_call = _invoke_api('metrocluster-heal', *args)
    return api_call

def metrocluster_interconnect_adapter_auto_reset_on_error_modify(*args):
    api_call = _invoke_api('metrocluster-interconnect-adapter-auto-reset-on-error-modify', *args)
    return api_call

def metrocluster_interconnect_adapter_get_iter(*args):
    api_call = _invoke_api('metrocluster-interconnect-adapter-get-iter', *args)
    return api_call

def metrocluster_interconnect_adapter_modify(*args):
    api_call = _invoke_api('metrocluster-interconnect-adapter-modify', *args)
    return api_call

def metrocluster_interconnect_adapter_reset(*args):
    api_call = _invoke_api('metrocluster-interconnect-adapter-reset', *args)
    return api_call

def metrocluster_interconnect_mirror_get_iter(*args):
    api_call = _invoke_api('metrocluster-interconnect-mirror-get-iter', *args)
    return api_call

def metrocluster_interconnect_mirror_modify(*args):
    api_call = _invoke_api('metrocluster-interconnect-mirror-modify', *args)
    return api_call

def metrocluster_interconnect_mirror_multipath_get_iter(*args):
    api_call = _invoke_api('metrocluster-interconnect-mirror-multipath-get-iter', *args)
    return api_call

def metrocluster_is_configured(*args):
    api_call = _invoke_api('metrocluster-is-configured', *args)
    return api_call

def metrocluster_node_get_iter(*args):
    api_call = _invoke_api('metrocluster-node-get-iter', *args)
    return api_call

def metrocluster_operation_get_iter(*args):
    api_call = _invoke_api('metrocluster-operation-get-iter', *args)
    return api_call

def metrocluster_progress_table_get_iter(*args):
    api_call = _invoke_api('metrocluster-progress-table-get-iter', *args)
    return api_call

def metrocluster_show_lif_placement_failures_get_iter(*args):
    api_call = _invoke_api('metrocluster-show-lif-placement-failures-get-iter', *args)
    return api_call

def metrocluster_switchback(*args):
    api_call = _invoke_api('metrocluster-switchback', *args)
    return api_call

def metrocluster_switchover(*args):
    api_call = _invoke_api('metrocluster-switchover', *args)
    return api_call

def metrocluster_tracelog_dump(*args):
    api_call = _invoke_api('metrocluster-tracelog-dump', *args)
    return api_call

def metrocluster_unconfigure(*args):
    api_call = _invoke_api('metrocluster-unconfigure', *args)
    return api_call

def metrocluster_vserver_get_iter(*args):
    api_call = _invoke_api('metrocluster-vserver-get-iter', *args)
    return api_call

def metrocluster_vserver_resync(*args):
    api_call = _invoke_api('metrocluster-vserver-resync', *args)
    return api_call

def name_mapping_get_iter(*args):
    api_call = _invoke_api('name-mapping-get-iter', *args)
    return api_call

def name_mapping_unix_group_get_iter(*args):
    api_call = _invoke_api('name-mapping-unix-group-get-iter', *args)
    return api_call

def name_mapping_unix_user_get_iter(*args):
    api_call = _invoke_api('name-mapping-unix-user-get-iter', *args)
    return api_call

def name_service_dns_statistics_get_iter(*args):
    api_call = _invoke_api('name-service-dns-statistics-get-iter', *args)
    return api_call

def name_service_nis_binding_detail_get_iter(*args):
    api_call = _invoke_api('name-service-nis-binding-detail-get-iter', *args)
    return api_call

def name_service_nis_show_bound_iter(*args):
    api_call = _invoke_api('name-service-nis-show-bound-iter', *args)
    return api_call

def name_service_nis_statistics_get_iter(*args):
    api_call = _invoke_api('name-service-nis-statistics-get-iter', *args)
    return api_call

def name_service_unix_group_limits_get(*args):
    api_call = _invoke_api('name-service-unix-group-limits-get', *args)
    return api_call

def name_service_unix_user_limits_get(*args):
    api_call = _invoke_api('name-service-unix-user-limits-get', *args)
    return api_call

def nameservice_dns_statistics_clear(*args):
    api_call = _invoke_api('nameservice-dns-statistics-clear', *args)
    return api_call

def nameservice_get_hostname_from_ipv4(*args):
    api_call = _invoke_api('nameservice-get-hostname-from-ipv4', *args)
    return api_call

def nameservice_get_ip_from_hostname(*args):
    api_call = _invoke_api('nameservice-get-ip-from-hostname', *args)
    return api_call

def nameservice_get_ipv4_from_hostname(*args):
    api_call = _invoke_api('nameservice-get-ipv4-from-hostname', *args)
    return api_call

def nameservice_nis_statistics_clear(*args):
    api_call = _invoke_api('nameservice-nis-statistics-clear', *args)
    return api_call

def nameservice_nsswitch_get_iter(*args):
    api_call = _invoke_api('nameservice-nsswitch-get-iter', *args)
    return api_call

def net_active_routes_get_iter(*args):
    api_call = _invoke_api('net-active-routes-get-iter', *args)
    return api_call

def net_arp_active_entry_destroy(*args):
    api_call = _invoke_api('net-arp-active-entry-destroy', *args)
    return api_call

def net_arp_active_entry_get(*args):
    api_call = _invoke_api('net-arp-active-entry-get', *args)
    return api_call

def net_arp_active_entry_get_iter(*args):
    api_call = _invoke_api('net-arp-active-entry-get-iter', *args)
    return api_call

def net_arp_create(*args):
    api_call = _invoke_api('net-arp-create', *args)
    return api_call

def net_arp_destroy(*args):
    api_call = _invoke_api('net-arp-destroy', *args)
    return api_call

def net_arp_get(*args):
    api_call = _invoke_api('net-arp-get', *args)
    return api_call

def net_arp_get_iter(*args):
    api_call = _invoke_api('net-arp-get-iter', *args)
    return api_call

def net_check_failover(*args):
    api_call = _invoke_api('net-check-failover', *args)
    return api_call

def net_cluster_ping(*args):
    api_call = _invoke_api('net-cluster-ping', *args)
    return api_call

def net_cluster_ping6(*args):
    api_call = _invoke_api('net-cluster-ping6', *args)
    return api_call

def net_connections_receive_window_size_get(*args):
    api_call = _invoke_api('net-connections-receive-window-size-get', *args)
    return api_call

def net_connections_receive_window_size_get_iter(*args):
    api_call = _invoke_api('net-connections-receive-window-size-get-iter', *args)
    return api_call

def net_connections_receive_window_size_modify(*args):
    api_call = _invoke_api('net-connections-receive-window-size-modify', *args)
    return api_call

def net_ddns_get_iter(*args):
    api_call = _invoke_api('net-ddns-get-iter', *args)
    return api_call

def net_device_discovery_get_iter(*args):
    api_call = _invoke_api('net-device-discovery-get-iter', *args)
    return api_call

def net_disable_readonly(*args):
    api_call = _invoke_api('net-disable-readonly', *args)
    return api_call

def net_dns_get_iter(*args):
    api_call = _invoke_api('net-dns-get-iter', *args)
    return api_call

def net_enable_readonly(*args):
    api_call = _invoke_api('net-enable-readonly', *args)
    return api_call

def net_failover_group_add_targets(*args):
    api_call = _invoke_api('net-failover-group-add-targets', *args)
    return api_call

def net_failover_group_create(*args):
    api_call = _invoke_api('net-failover-group-create', *args)
    return api_call

def net_failover_group_destroy(*args):
    api_call = _invoke_api('net-failover-group-destroy', *args)
    return api_call

def net_failover_group_get_iter(*args):
    api_call = _invoke_api('net-failover-group-get-iter', *args)
    return api_call

def net_failover_group_modify(*args):
    api_call = _invoke_api('net-failover-group-modify', *args)
    return api_call

def net_failover_group_remove_targets(*args):
    api_call = _invoke_api('net-failover-group-remove-targets', *args)
    return api_call

def net_failover_group_rename(*args):
    api_call = _invoke_api('net-failover-group-rename', *args)
    return api_call

def net_firewall_config_get(*args):
    api_call = _invoke_api('net-firewall-config-get', *args)
    return api_call

def net_firewall_config_get_iter(*args):
    api_call = _invoke_api('net-firewall-config-get-iter', *args)
    return api_call

def net_firewall_config_modify(*args):
    api_call = _invoke_api('net-firewall-config-modify', *args)
    return api_call

def net_firewall_config_modify_iter(*args):
    api_call = _invoke_api('net-firewall-config-modify-iter', *args)
    return api_call

def net_firewall_policy_create(*args):
    api_call = _invoke_api('net-firewall-policy-create', *args)
    return api_call

def net_firewall_policy_destroy(*args):
    api_call = _invoke_api('net-firewall-policy-destroy', *args)
    return api_call

def net_firewall_policy_get_iter(*args):
    api_call = _invoke_api('net-firewall-policy-get-iter', *args)
    return api_call

def net_firewall_policy_modify(*args):
    api_call = _invoke_api('net-firewall-policy-modify', *args)
    return api_call

def net_hosts_get_iter(*args):
    api_call = _invoke_api('net-hosts-get-iter', *args)
    return api_call

def net_interface_create(*args):
    api_call = _invoke_api('net-interface-create', *args)
    return api_call

def net_interface_delete(*args):
    api_call = _invoke_api('net-interface-delete', *args)
    return api_call

def net_interface_get_iter(*args):
    api_call = _invoke_api('net-interface-get-iter', *args)
    return api_call

def net_interface_migrate(*args):
    api_call = _invoke_api('net-interface-migrate', *args)
    return api_call

def net_interface_modify(*args):
    api_call = _invoke_api('net-interface-modify', *args)
    return api_call

def net_interface_modify_iter(*args):
    api_call = _invoke_api('net-interface-modify-iter', *args)
    return api_call

def net_interface_revert(*args):
    api_call = _invoke_api('net-interface-revert', *args)
    return api_call

def net_ipspaces_assign_vserver(*args):
    api_call = _invoke_api('net-ipspaces-assign-vserver', *args)
    return api_call

def net_ipspaces_create(*args):
    api_call = _invoke_api('net-ipspaces-create', *args)
    return api_call

def net_ipspaces_destroy(*args):
    api_call = _invoke_api('net-ipspaces-destroy', *args)
    return api_call

def net_ipspaces_get(*args):
    api_call = _invoke_api('net-ipspaces-get', *args)
    return api_call

def net_ipspaces_get_iter(*args):
    api_call = _invoke_api('net-ipspaces-get-iter', *args)
    return api_call

def net_ipspaces_rename(*args):
    api_call = _invoke_api('net-ipspaces-rename', *args)
    return api_call

def net_ndp_active_neighbor_destroy(*args):
    api_call = _invoke_api('net-ndp-active-neighbor-destroy', *args)
    return api_call

def net_ndp_active_neighbor_get(*args):
    api_call = _invoke_api('net-ndp-active-neighbor-get', *args)
    return api_call

def net_ndp_active_neighbor_get_iter(*args):
    api_call = _invoke_api('net-ndp-active-neighbor-get-iter', *args)
    return api_call

def net_ndp_default_router_delete_all(*args):
    api_call = _invoke_api('net-ndp-default-router-delete-all', *args)
    return api_call

def net_ndp_default_router_get(*args):
    api_call = _invoke_api('net-ndp-default-router-get', *args)
    return api_call

def net_ndp_default_router_get_iter(*args):
    api_call = _invoke_api('net-ndp-default-router-get-iter', *args)
    return api_call

def net_ndp_neighbor_get_iter(*args):
    api_call = _invoke_api('net-ndp-neighbor-get-iter', *args)
    return api_call

def net_ndp_prefix_delete_all(*args):
    api_call = _invoke_api('net-ndp-prefix-delete-all', *args)
    return api_call

def net_ndp_prefix_get(*args):
    api_call = _invoke_api('net-ndp-prefix-get', *args)
    return api_call

def net_ndp_prefix_get_iter(*args):
    api_call = _invoke_api('net-ndp-prefix-get-iter', *args)
    return api_call

def net_options_get(*args):
    api_call = _invoke_api('net-options-get', *args)
    return api_call

def net_options_modify(*args):
    api_call = _invoke_api('net-options-modify', *args)
    return api_call

def net_placement_cache_delete(*args):
    api_call = _invoke_api('net-placement-cache-delete', *args)
    return api_call

def net_placement_cache_get_iter(*args):
    api_call = _invoke_api('net-placement-cache-get-iter', *args)
    return api_call

def net_placement_discover(*args):
    api_call = _invoke_api('net-placement-discover', *args)
    return api_call

def net_port_broadcast_domain_add_ports(*args):
    api_call = _invoke_api('net-port-broadcast-domain-add-ports', *args)
    return api_call

def net_port_broadcast_domain_create(*args):
    api_call = _invoke_api('net-port-broadcast-domain-create', *args)
    return api_call

def net_port_broadcast_domain_destroy(*args):
    api_call = _invoke_api('net-port-broadcast-domain-destroy', *args)
    return api_call

def net_port_broadcast_domain_get(*args):
    api_call = _invoke_api('net-port-broadcast-domain-get', *args)
    return api_call

def net_port_broadcast_domain_get_iter(*args):
    api_call = _invoke_api('net-port-broadcast-domain-get-iter', *args)
    return api_call

def net_port_broadcast_domain_merge(*args):
    api_call = _invoke_api('net-port-broadcast-domain-merge', *args)
    return api_call

def net_port_broadcast_domain_modify(*args):
    api_call = _invoke_api('net-port-broadcast-domain-modify', *args)
    return api_call

def net_port_broadcast_domain_remove_ports(*args):
    api_call = _invoke_api('net-port-broadcast-domain-remove-ports', *args)
    return api_call

def net_port_broadcast_domain_rename(*args):
    api_call = _invoke_api('net-port-broadcast-domain-rename', *args)
    return api_call

def net_port_broadcast_domain_split(*args):
    api_call = _invoke_api('net-port-broadcast-domain-split', *args)
    return api_call

def net_port_delete(*args):
    api_call = _invoke_api('net-port-delete', *args)
    return api_call

def net_port_get(*args):
    api_call = _invoke_api('net-port-get', *args)
    return api_call

def net_port_get_iter(*args):
    api_call = _invoke_api('net-port-get-iter', *args)
    return api_call

def net_port_ifgrp_add_port(*args):
    api_call = _invoke_api('net-port-ifgrp-add-port', *args)
    return api_call

def net_port_ifgrp_create(*args):
    api_call = _invoke_api('net-port-ifgrp-create', *args)
    return api_call

def net_port_ifgrp_destroy(*args):
    api_call = _invoke_api('net-port-ifgrp-destroy', *args)
    return api_call

def net_port_ifgrp_get(*args):
    api_call = _invoke_api('net-port-ifgrp-get', *args)
    return api_call

def net_port_ifgrp_remove_port(*args):
    api_call = _invoke_api('net-port-ifgrp-remove-port', *args)
    return api_call

def net_port_modify(*args):
    api_call = _invoke_api('net-port-modify', *args)
    return api_call

def net_port_modify_iter(*args):
    api_call = _invoke_api('net-port-modify-iter', *args)
    return api_call

def net_routes_get_iter(*args):
    api_call = _invoke_api('net-routes-get-iter', *args)
    return api_call

def net_routes_lifs_get_iter(*args):
    api_call = _invoke_api('net-routes-lifs-get-iter', *args)
    return api_call

def net_routing_group_route_create(*args):
    api_call = _invoke_api('net-routing-group-route-create', *args)
    return api_call

def net_routing_group_route_destroy(*args):
    api_call = _invoke_api('net-routing-group-route-destroy', *args)
    return api_call

def net_routing_group_route_get_iter(*args):
    api_call = _invoke_api('net-routing-group-route-get-iter', *args)
    return api_call

def net_san_lif_placement_get(*args):
    api_call = _invoke_api('net-san-lif-placement-get', *args)
    return api_call

def net_subnet_add_ranges(*args):
    api_call = _invoke_api('net-subnet-add-ranges', *args)
    return api_call

def net_subnet_create(*args):
    api_call = _invoke_api('net-subnet-create', *args)
    return api_call

def net_subnet_destroy(*args):
    api_call = _invoke_api('net-subnet-destroy', *args)
    return api_call

def net_subnet_get(*args):
    api_call = _invoke_api('net-subnet-get', *args)
    return api_call

def net_subnet_get_iter(*args):
    api_call = _invoke_api('net-subnet-get-iter', *args)
    return api_call

def net_subnet_modify(*args):
    api_call = _invoke_api('net-subnet-modify', *args)
    return api_call

def net_subnet_remove_ranges(*args):
    api_call = _invoke_api('net-subnet-remove-ranges', *args)
    return api_call

def net_subnet_rename(*args):
    api_call = _invoke_api('net-subnet-rename', *args)
    return api_call

def net_traceroute6(*args):
    api_call = _invoke_api('net-traceroute6', *args)
    return api_call

def net_vlan_create(*args):
    api_call = _invoke_api('net-vlan-create', *args)
    return api_call

def net_vlan_delete(*args):
    api_call = _invoke_api('net-vlan-delete', *args)
    return api_call

def net_vlan_get(*args):
    api_call = _invoke_api('net-vlan-get', *args)
    return api_call

def net_vlan_get_iter(*args):
    api_call = _invoke_api('net-vlan-get-iter', *args)
    return api_call

def netgroups_file_delete(*args):
    api_call = _invoke_api('netgroups-file-delete', *args)
    return api_call

def netgroups_file_get(*args):
    api_call = _invoke_api('netgroups-file-get', *args)
    return api_call

def netgroups_file_get_iter(*args):
    api_call = _invoke_api('netgroups-file-get-iter', *args)
    return api_call

def nfs_all_flash_optimized_get(*args):
    api_call = _invoke_api('nfs-all-flash-optimized-get', *args)
    return api_call

def nfs_all_flash_optimized_get_iter(*args):
    api_call = _invoke_api('nfs-all-flash-optimized-get-iter', *args)
    return api_call

def nfs_service_get_create_defaults(*args):
    api_call = _invoke_api('nfs-service-get-create-defaults', *args)
    return api_call

def nfs_service_get_iter(*args):
    api_call = _invoke_api('nfs-service-get-iter', *args)
    return api_call

def nis_get_iter(*args):
    api_call = _invoke_api('nis-get-iter', *args)
    return api_call

def ntdtest_action_alt_simpleget(*args):
    api_call = _invoke_api('ntdtest-action-alt-simpleget', *args)
    return api_call

def ntdtest_action_alt_simpleget_optional(*args):
    api_call = _invoke_api('ntdtest-action-alt-simpleget-optional', *args)
    return api_call

def ntdtest_action_only_doit(*args):
    api_call = _invoke_api('ntdtest-action-only-doit', *args)
    return api_call

def ntdtest_action_only_doit_async(*args):
    api_call = _invoke_api('ntdtest-action-only-doit-async', *args)
    return api_call

def ntdtest_action_only_dothat(*args):
    api_call = _invoke_api('ntdtest-action-only-dothat', *args)
    return api_call

def ntdtest_action_simpleget(*args):
    api_call = _invoke_api('ntdtest-action-simpleget', *args)
    return api_call

def ntdtest_action_top_level_create(*args):
    api_call = _invoke_api('ntdtest-action-top-level-create', *args)
    return api_call

def ntdtest_action_top_level_create_alt(*args):
    api_call = _invoke_api('ntdtest-action-top-level-create-alt', *args)
    return api_call

def ntdtest_dnested_get(*args):
    api_call = _invoke_api('ntdtest-dnested-get', *args)
    return api_call

def ntdtest_dnested_get_iter(*args):
    api_call = _invoke_api('ntdtest-dnested-get-iter', *args)
    return api_call

def ntdtest_empty_tags_get_1(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-1', *args)
    return api_call

def ntdtest_empty_tags_get_10(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-10', *args)
    return api_call

def ntdtest_empty_tags_get_11(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-11', *args)
    return api_call

def ntdtest_empty_tags_get_12(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-12', *args)
    return api_call

def ntdtest_empty_tags_get_13(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-13', *args)
    return api_call

def ntdtest_empty_tags_get_2(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-2', *args)
    return api_call

def ntdtest_empty_tags_get_3(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-3', *args)
    return api_call

def ntdtest_empty_tags_get_4(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-4', *args)
    return api_call

def ntdtest_empty_tags_get_5(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-5', *args)
    return api_call

def ntdtest_empty_tags_get_6(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-6', *args)
    return api_call

def ntdtest_empty_tags_get_7(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-7', *args)
    return api_call

def ntdtest_empty_tags_get_8(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-8', *args)
    return api_call

def ntdtest_empty_tags_get_9(*args):
    api_call = _invoke_api('ntdtest-empty-tags-get-9', *args)
    return api_call

def ntdtest_extensive_alternate_create_1(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-create-1', *args)
    return api_call

def ntdtest_extensive_alternate_create_2(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-create-2', *args)
    return api_call

def ntdtest_extensive_alternate_destroy_1(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-destroy-1', *args)
    return api_call

def ntdtest_extensive_alternate_get_1(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-get-1', *args)
    return api_call

def ntdtest_extensive_alternate_get_2(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-get-2', *args)
    return api_call

def ntdtest_extensive_alternate_modify_1(*args):
    api_call = _invoke_api('ntdtest-extensive-alternate-modify-1', *args)
    return api_call

def ntdtest_extensive_default_create(*args):
    api_call = _invoke_api('ntdtest-extensive-default-create', *args)
    return api_call

def ntdtest_extensive_default_destroy(*args):
    api_call = _invoke_api('ntdtest-extensive-default-destroy', *args)
    return api_call

def ntdtest_extensive_default_get(*args):
    api_call = _invoke_api('ntdtest-extensive-default-get', *args)
    return api_call

def ntdtest_extensive_default_modify(*args):
    api_call = _invoke_api('ntdtest-extensive-default-modify', *args)
    return api_call

def ntdtest_extensive_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-extensive-destroy-iter', *args)
    return api_call

def ntdtest_extensive_get_iter(*args):
    api_call = _invoke_api('ntdtest-extensive-get-iter', *args)
    return api_call

def ntdtest_extensive_method1_alternate(*args):
    api_call = _invoke_api('ntdtest-extensive-method1-alternate', *args)
    return api_call

def ntdtest_extensive_method1_default(*args):
    api_call = _invoke_api('ntdtest-extensive-method1-default', *args)
    return api_call

def ntdtest_extensive_method2_alternate(*args):
    api_call = _invoke_api('ntdtest-extensive-method2-alternate', *args)
    return api_call

def ntdtest_extensive_method2_default(*args):
    api_call = _invoke_api('ntdtest-extensive-method2-default', *args)
    return api_call

def ntdtest_extensive_method3_default(*args):
    api_call = _invoke_api('ntdtest-extensive-method3-default', *args)
    return api_call

def ntdtest_extensive_method4_alt(*args):
    api_call = _invoke_api('ntdtest-extensive-method4-alt', *args)
    return api_call

def ntdtest_extensive_method4_default(*args):
    api_call = _invoke_api('ntdtest-extensive-method4-default', *args)
    return api_call

def ntdtest_extensive_method5_alternate(*args):
    api_call = _invoke_api('ntdtest-extensive-method5-alternate', *args)
    return api_call

def ntdtest_extensive_method6_alternate(*args):
    api_call = _invoke_api('ntdtest-extensive-method6-alternate', *args)
    return api_call

def ntdtest_extensive_method6_alternate_1(*args):
    api_call = _invoke_api('ntdtest-extensive-method6-alternate-1', *args)
    return api_call

def ntdtest_extensive_method6_default(*args):
    api_call = _invoke_api('ntdtest-extensive-method6-default', *args)
    return api_call

def ntdtest_extensive_modify_iter(*args):
    api_call = _invoke_api('ntdtest-extensive-modify-iter', *args)
    return api_call

def ntdtest_folding_create(*args):
    api_call = _invoke_api('ntdtest-folding-create', *args)
    return api_call

def ntdtest_folding_deep_arrayof_get_iter(*args):
    api_call = _invoke_api('ntdtest-folding-deep-arrayof-get-iter', *args)
    return api_call

def ntdtest_folding_default_get(*args):
    api_call = _invoke_api('ntdtest-folding-default-get', *args)
    return api_call

def ntdtest_folding_destroy(*args):
    api_call = _invoke_api('ntdtest-folding-destroy', *args)
    return api_call

def ntdtest_folding_get(*args):
    api_call = _invoke_api('ntdtest-folding-get', *args)
    return api_call

def ntdtest_folding_get_collapsed_and_arrayof(*args):
    api_call = _invoke_api('ntdtest-folding-get-collapsed-and-arrayof', *args)
    return api_call

def ntdtest_folding_get_deep_element(*args):
    api_call = _invoke_api('ntdtest-folding-get-deep-element', *args)
    return api_call

def ntdtest_folding_get_element_no_array(*args):
    api_call = _invoke_api('ntdtest-folding-get-element-no-array', *args)
    return api_call

def ntdtest_folding_get_full_list(*args):
    api_call = _invoke_api('ntdtest-folding-get-full-list', *args)
    return api_call

def ntdtest_folding_get_iter(*args):
    api_call = _invoke_api('ntdtest-folding-get-iter', *args)
    return api_call

def ntdtest_folding_get_iter_mixed(*args):
    api_call = _invoke_api('ntdtest-folding-get-iter-mixed', *args)
    return api_call

def ntdtest_folding_get_multiple_field_list_shallow(*args):
    api_call = _invoke_api('ntdtest-folding-get-multiple-field-list-shallow', *args)
    return api_call

def ntdtest_folding_get_multiple_field_list_top(*args):
    api_call = _invoke_api('ntdtest-folding-get-multiple-field-list-top', *args)
    return api_call

def ntdtest_folding_get_multiple_fields_list_array_and_collapsed(*args):
    api_call = _invoke_api('ntdtest-folding-get-multiple-fields-list-array-and-collapsed', *args)
    return api_call

def ntdtest_folding_get_shallow_element(*args):
    api_call = _invoke_api('ntdtest-folding-get-shallow-element', *args)
    return api_call

def ntdtest_folding_get_single_field_list(*args):
    api_call = _invoke_api('ntdtest-folding-get-single-field-list', *args)
    return api_call

def ntdtest_folding_list_info(*args):
    api_call = _invoke_api('ntdtest-folding-list-info', *args)
    return api_call

def ntdtest_folding_list_info_alt(*args):
    api_call = _invoke_api('ntdtest-folding-list-info-alt', *args)
    return api_call

def ntdtest_folding_list_info_deep_element(*args):
    api_call = _invoke_api('ntdtest-folding-list-info-deep-element', *args)
    return api_call

def ntdtest_folding_multiple_arrays_create(*args):
    api_call = _invoke_api('ntdtest-folding-multiple-arrays-create', *args)
    return api_call

def ntdtest_folding_multiple_arrays_destroy(*args):
    api_call = _invoke_api('ntdtest-folding-multiple-arrays-destroy', *args)
    return api_call

def ntdtest_folding_multiple_arrays_get_iter(*args):
    api_call = _invoke_api('ntdtest-folding-multiple-arrays-get-iter', *args)
    return api_call

def ntdtest_get(*args):
    api_call = _invoke_api('ntdtest-get', *args)
    return api_call

def ntdtest_get_iter(*args):
    api_call = _invoke_api('ntdtest-get-iter', *args)
    return api_call

def ntdtest_iterfrom_alt_create(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-create', *args)
    return api_call

def ntdtest_iterfrom_alt_destroy(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-destroy', *args)
    return api_call

def ntdtest_iterfrom_alt_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-destroy-iter', *args)
    return api_call

def ntdtest_iterfrom_alt_get(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-get', *args)
    return api_call

def ntdtest_iterfrom_alt_get_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-get-iter', *args)
    return api_call

def ntdtest_iterfrom_alt_list_info(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-list-info', *args)
    return api_call

def ntdtest_iterfrom_alt_modify(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-modify', *args)
    return api_call

def ntdtest_iterfrom_alt_modify_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-alt-modify-iter', *args)
    return api_call

def ntdtest_iterfrom_create(*args):
    api_call = _invoke_api('ntdtest-iterfrom-create', *args)
    return api_call

def ntdtest_iterfrom_destroy(*args):
    api_call = _invoke_api('ntdtest-iterfrom-destroy', *args)
    return api_call

def ntdtest_iterfrom_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-destroy-iter', *args)
    return api_call

def ntdtest_iterfrom_dupe_create(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-create', *args)
    return api_call

def ntdtest_iterfrom_dupe_destroy(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-destroy', *args)
    return api_call

def ntdtest_iterfrom_dupe_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-destroy-iter', *args)
    return api_call

def ntdtest_iterfrom_dupe_get(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-get', *args)
    return api_call

def ntdtest_iterfrom_dupe_get_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-get-iter', *args)
    return api_call

def ntdtest_iterfrom_dupe_list_info(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-list-info', *args)
    return api_call

def ntdtest_iterfrom_dupe_modify(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-modify', *args)
    return api_call

def ntdtest_iterfrom_dupe_modify_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-dupe-modify-iter', *args)
    return api_call

def ntdtest_iterfrom_get(*args):
    api_call = _invoke_api('ntdtest-iterfrom-get', *args)
    return api_call

def ntdtest_iterfrom_get_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-get-iter', *args)
    return api_call

def ntdtest_iterfrom_list_info(*args):
    api_call = _invoke_api('ntdtest-iterfrom-list-info', *args)
    return api_call

def ntdtest_iterfrom_modify(*args):
    api_call = _invoke_api('ntdtest-iterfrom-modify', *args)
    return api_call

def ntdtest_iterfrom_modify_iter(*args):
    api_call = _invoke_api('ntdtest-iterfrom-modify-iter', *args)
    return api_call

def ntdtest_iternoread_create(*args):
    api_call = _invoke_api('ntdtest-iternoread-create', *args)
    return api_call

def ntdtest_iternoread_destroy(*args):
    api_call = _invoke_api('ntdtest-iternoread-destroy', *args)
    return api_call

def ntdtest_iternoread_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-iternoread-destroy-iter', *args)
    return api_call

def ntdtest_iternoread_get(*args):
    api_call = _invoke_api('ntdtest-iternoread-get', *args)
    return api_call

def ntdtest_iternoread_get_alt(*args):
    api_call = _invoke_api('ntdtest-iternoread-get-alt', *args)
    return api_call

def ntdtest_iternoread_get_iter(*args):
    api_call = _invoke_api('ntdtest-iternoread-get-iter', *args)
    return api_call

def ntdtest_iternoread_get_iter_alt(*args):
    api_call = _invoke_api('ntdtest-iternoread-get-iter-alt', *args)
    return api_call

def ntdtest_iternoread_list_info(*args):
    api_call = _invoke_api('ntdtest-iternoread-list-info', *args)
    return api_call

def ntdtest_iternoread_modify(*args):
    api_call = _invoke_api('ntdtest-iternoread-modify', *args)
    return api_call

def ntdtest_iternoread_modify_iter(*args):
    api_call = _invoke_api('ntdtest-iternoread-modify-iter', *args)
    return api_call

def ntdtest_iterwants_get(*args):
    api_call = _invoke_api('ntdtest-iterwants-get', *args)
    return api_call

def ntdtest_iterwants_get_iter(*args):
    api_call = _invoke_api('ntdtest-iterwants-get-iter', *args)
    return api_call

def ntdtest_list_non_test_action_default(*args):
    api_call = _invoke_api('ntdtest-list-non-test-action-default', *args)
    return api_call

def ntdtest_list_non_test_method_default(*args):
    api_call = _invoke_api('ntdtest-list-non-test-method-default', *args)
    return api_call

def ntdtest_method_only_default(*args):
    api_call = _invoke_api('ntdtest-method-only-default', *args)
    return api_call

def ntdtest_method_only_method2(*args):
    api_call = _invoke_api('ntdtest-method-only-method2', *args)
    return api_call

def ntdtest_method_only_method3(*args):
    api_call = _invoke_api('ntdtest-method-only-method3', *args)
    return api_call

def ntdtest_method_only_method3_a(*args):
    api_call = _invoke_api('ntdtest-method-only-method3-a', *args)
    return api_call

def ntdtest_method_only_method3_async(*args):
    api_call = _invoke_api('ntdtest-method-only-method3-async', *args)
    return api_call

def ntdtest_method_only_method3_async_a(*args):
    api_call = _invoke_api('ntdtest-method-only-method3-async-a', *args)
    return api_call

def ntdtest_method_only_method3_async_iter(*args):
    api_call = _invoke_api('ntdtest-method-only-method3-async-iter', *args)
    return api_call

def ntdtest_method_only_method3_iter(*args):
    api_call = _invoke_api('ntdtest-method-only-method3-iter', *args)
    return api_call

def ntdtest_multiple_array_get_deep_element(*args):
    api_call = _invoke_api('ntdtest-multiple-array-get-deep-element', *args)
    return api_call

def ntdtest_multiple_array_get_shallow_element(*args):
    api_call = _invoke_api('ntdtest-multiple-array-get-shallow-element', *args)
    return api_call

def ntdtest_multiple_arrays_get_iter(*args):
    api_call = _invoke_api('ntdtest-multiple-arrays-get-iter', *args)
    return api_call

def ntdtest_multiple_default_method1_alternate(*args):
    api_call = _invoke_api('ntdtest-multiple-default-method1-alternate', *args)
    return api_call

def ntdtest_multiple_default_method1_default(*args):
    api_call = _invoke_api('ntdtest-multiple-default-method1-default', *args)
    return api_call

def ntdtest_multiple_inout_method1_alternate(*args):
    api_call = _invoke_api('ntdtest-multiple-inout-method1-alternate', *args)
    return api_call

def ntdtest_multiple_inout_method1_default(*args):
    api_call = _invoke_api('ntdtest-multiple-inout-method1-default', *args)
    return api_call

def ntdtest_multiple_with_default_create(*args):
    api_call = _invoke_api('ntdtest-multiple-with-default-create', *args)
    return api_call

def ntdtest_multiple_with_inout_create(*args):
    api_call = _invoke_api('ntdtest-multiple-with-inout-create', *args)
    return api_call

def ntdtest_nonlist_get(*args):
    api_call = _invoke_api('ntdtest-nonlist-get', *args)
    return api_call

def ntdtest_nonlist_get_iter(*args):
    api_call = _invoke_api('ntdtest-nonlist-get-iter', *args)
    return api_call

def ntdtest_shownoread_default_get(*args):
    api_call = _invoke_api('ntdtest-shownoread-default-get', *args)
    return api_call

def ntdtest_shownoread_get(*args):
    api_call = _invoke_api('ntdtest-shownoread-get', *args)
    return api_call

def ntdtest_top_level_alt_create(*args):
    api_call = _invoke_api('ntdtest-top-level-alt-create', *args)
    return api_call

def ntdtest_top_level_alt_get(*args):
    api_call = _invoke_api('ntdtest-top-level-alt-get', *args)
    return api_call

def ntdtest_top_level_default_create(*args):
    api_call = _invoke_api('ntdtest-top-level-default-create', *args)
    return api_call

def ntdtest_top_level_default_destroy(*args):
    api_call = _invoke_api('ntdtest-top-level-default-destroy', *args)
    return api_call

def ntdtest_top_level_default_get(*args):
    api_call = _invoke_api('ntdtest-top-level-default-get', *args)
    return api_call

def ntdtest_top_level_default_modify(*args):
    api_call = _invoke_api('ntdtest-top-level-default-modify', *args)
    return api_call

def ntdtest_top_level_no_inputs_create(*args):
    api_call = _invoke_api('ntdtest-top-level-no-inputs-create', *args)
    return api_call

def ntdtest_view_alternate_create_1(*args):
    api_call = _invoke_api('ntdtest-view-alternate-create-1', *args)
    return api_call

def ntdtest_view_alternate_create_2(*args):
    api_call = _invoke_api('ntdtest-view-alternate-create-2', *args)
    return api_call

def ntdtest_view_alternate_destroy_1(*args):
    api_call = _invoke_api('ntdtest-view-alternate-destroy-1', *args)
    return api_call

def ntdtest_view_alternate_get_1(*args):
    api_call = _invoke_api('ntdtest-view-alternate-get-1', *args)
    return api_call

def ntdtest_view_alternate_get_2(*args):
    api_call = _invoke_api('ntdtest-view-alternate-get-2', *args)
    return api_call

def ntdtest_view_alternate_modify_1(*args):
    api_call = _invoke_api('ntdtest-view-alternate-modify-1', *args)
    return api_call

def ntdtest_view_default_create(*args):
    api_call = _invoke_api('ntdtest-view-default-create', *args)
    return api_call

def ntdtest_view_default_destroy(*args):
    api_call = _invoke_api('ntdtest-view-default-destroy', *args)
    return api_call

def ntdtest_view_default_get(*args):
    api_call = _invoke_api('ntdtest-view-default-get', *args)
    return api_call

def ntdtest_view_default_modify(*args):
    api_call = _invoke_api('ntdtest-view-default-modify', *args)
    return api_call

def ntdtest_view_destroy_iter(*args):
    api_call = _invoke_api('ntdtest-view-destroy-iter', *args)
    return api_call

def ntdtest_view_get_iter(*args):
    api_call = _invoke_api('ntdtest-view-get-iter', *args)
    return api_call

def ntdtest_view_modify_iter(*args):
    api_call = _invoke_api('ntdtest-view-modify-iter', *args)
    return api_call

def ntp_server_create(*args):
    api_call = _invoke_api('ntp-server-create', *args)
    return api_call

def ntp_server_delete(*args):
    api_call = _invoke_api('ntp-server-delete', *args)
    return api_call

def ntp_server_get(*args):
    api_call = _invoke_api('ntp-server-get', *args)
    return api_call

def ntp_server_get_iter(*args):
    api_call = _invoke_api('ntp-server-get-iter', *args)
    return api_call

def ntp_server_modify(*args):
    api_call = _invoke_api('ntp-server-modify', *args)
    return api_call

def ntp_server_reset(*args):
    api_call = _invoke_api('ntp-server-reset', *args)
    return api_call

def ntp_server_validate(*args):
    api_call = _invoke_api('ntp-server-validate', *args)
    return api_call

def options_get_iter(*args):
    api_call = _invoke_api('options-get-iter', *args)
    return api_call

def options_modify_iter(*args):
    api_call = _invoke_api('options-modify-iter', *args)
    return api_call

def perf_archive_config_get(*args):
    api_call = _invoke_api('perf-archive-config-get', *args)
    return api_call

def perf_archive_config_modify(*args):
    api_call = _invoke_api('perf-archive-config-modify', *args)
    return api_call

def perf_archive_create(*args):
    api_call = _invoke_api('perf-archive-create', *args)
    return api_call

def perf_archive_datastore_get_iter(*args):
    api_call = _invoke_api('perf-archive-datastore-get-iter', *args)
    return api_call

def perf_archive_destroy(*args):
    api_call = _invoke_api('perf-archive-destroy', *args)
    return api_call

def perf_archive_get_iter(*args):
    api_call = _invoke_api('perf-archive-get-iter', *args)
    return api_call

def perf_archive_modify(*args):
    api_call = _invoke_api('perf-archive-modify', *args)
    return api_call

def perf_object_counter_list_info(*args):
    api_call = _invoke_api('perf-object-counter-list-info', *args)
    return api_call

def perf_object_get_instances(*args):
    api_call = _invoke_api('perf-object-get-instances', *args)
    return api_call

def perf_object_instance_list_info_iter(*args):
    api_call = _invoke_api('perf-object-instance-list-info-iter', *args)
    return api_call

def perf_object_list_info(*args):
    api_call = _invoke_api('perf-object-list-info', *args)
    return api_call

def perf_preset_create(*args):
    api_call = _invoke_api('perf-preset-create', *args)
    return api_call

def perf_preset_delete(*args):
    api_call = _invoke_api('perf-preset-delete', *args)
    return api_call

def perf_preset_detail_get(*args):
    api_call = _invoke_api('perf-preset-detail-get', *args)
    return api_call

def perf_preset_get_iter(*args):
    api_call = _invoke_api('perf-preset-get-iter', *args)
    return api_call

def perf_preset_import(*args):
    api_call = _invoke_api('perf-preset-import', *args)
    return api_call

def perf_preset_modify(*args):
    api_call = _invoke_api('perf-preset-modify', *args)
    return api_call

def portset_get_iter(*args):
    api_call = _invoke_api('portset-get-iter', *args)
    return api_call

def qos_policy_group_create(*args):
    api_call = _invoke_api('qos-policy-group-create', *args)
    return api_call

def qos_policy_group_delete(*args):
    api_call = _invoke_api('qos-policy-group-delete', *args)
    return api_call

def qos_policy_group_delete_iter(*args):
    api_call = _invoke_api('qos-policy-group-delete-iter', *args)
    return api_call

def qos_policy_group_get(*args):
    api_call = _invoke_api('qos-policy-group-get', *args)
    return api_call

def qos_policy_group_get_iter(*args):
    api_call = _invoke_api('qos-policy-group-get-iter', *args)
    return api_call

def qos_policy_group_modify(*args):
    api_call = _invoke_api('qos-policy-group-modify', *args)
    return api_call

def qos_policy_group_modify_iter(*args):
    api_call = _invoke_api('qos-policy-group-modify-iter', *args)
    return api_call

def qos_policy_group_rename(*args):
    api_call = _invoke_api('qos-policy-group-rename', *args)
    return api_call

def qos_settings_control_get(*args):
    api_call = _invoke_api('qos-settings-control-get', *args)
    return api_call

def qos_settings_control_modify(*args):
    api_call = _invoke_api('qos-settings-control-modify', *args)
    return api_call

def qos_settings_read_ahead_create(*args):
    api_call = _invoke_api('qos-settings-read-ahead-create', *args)
    return api_call

def qos_settings_read_ahead_destroy(*args):
    api_call = _invoke_api('qos-settings-read-ahead-destroy', *args)
    return api_call

def qos_settings_read_ahead_destroy_iter(*args):
    api_call = _invoke_api('qos-settings-read-ahead-destroy-iter', *args)
    return api_call

def qos_settings_read_ahead_get(*args):
    api_call = _invoke_api('qos-settings-read-ahead-get', *args)
    return api_call

def qos_settings_read_ahead_get_iter(*args):
    api_call = _invoke_api('qos-settings-read-ahead-get-iter', *args)
    return api_call

def qos_settings_read_ahead_modify(*args):
    api_call = _invoke_api('qos-settings-read-ahead-modify', *args)
    return api_call

def qos_settings_read_ahead_modify_iter(*args):
    api_call = _invoke_api('qos-settings-read-ahead-modify-iter', *args)
    return api_call

def qos_test_smf_zapi_error(*args):
    api_call = _invoke_api('qos-test-smf-zapi-error', *args)
    return api_call

def qos_workload_delete(*args):
    api_call = _invoke_api('qos-workload-delete', *args)
    return api_call

def qos_workload_delete_iter(*args):
    api_call = _invoke_api('qos-workload-delete-iter', *args)
    return api_call

def qos_workload_get(*args):
    api_call = _invoke_api('qos-workload-get', *args)
    return api_call

def qos_workload_get_iter(*args):
    api_call = _invoke_api('qos-workload-get-iter', *args)
    return api_call

def qos_workload_modify(*args):
    api_call = _invoke_api('qos-workload-modify', *args)
    return api_call

def qos_workload_modify_iter(*args):
    api_call = _invoke_api('qos-workload-modify-iter', *args)
    return api_call

def qtree_list_iter(*args):
    api_call = _invoke_api('qtree-list-iter', *args)
    return api_call

def quota_list_entries_iter(*args):
    api_call = _invoke_api('quota-list-entries-iter', *args)
    return api_call

def quota_policy_copy(*args):
    api_call = _invoke_api('quota-policy-copy', *args)
    return api_call

def quota_policy_create(*args):
    api_call = _invoke_api('quota-policy-create', *args)
    return api_call

def quota_policy_delete_iter(*args):
    api_call = _invoke_api('quota-policy-delete-iter', *args)
    return api_call

def quota_policy_get_iter(*args):
    api_call = _invoke_api('quota-policy-get-iter', *args)
    return api_call

def quota_policy_rename(*args):
    api_call = _invoke_api('quota-policy-rename', *args)
    return api_call

def quota_policy_rule_count_get_iter(*args):
    api_call = _invoke_api('quota-policy-rule-count-get-iter', *args)
    return api_call

def quota_report_iter(*args):
    api_call = _invoke_api('quota-report-iter', *args)
    return api_call

def quota_status_iter(*args):
    api_call = _invoke_api('quota-status-iter', *args)
    return api_call

def raidgroup_get_iter(*args):
    api_call = _invoke_api('raidgroup-get-iter', *args)
    return api_call

def security_certificate_ca_issued_get_iter(*args):
    api_call = _invoke_api('security-certificate-ca-issued-get-iter', *args)
    return api_call

def security_certificate_create(*args):
    api_call = _invoke_api('security-certificate-create', *args)
    return api_call

def security_certificate_delete(*args):
    api_call = _invoke_api('security-certificate-delete', *args)
    return api_call

def security_certificate_delete_iter(*args):
    api_call = _invoke_api('security-certificate-delete-iter', *args)
    return api_call

def security_certificate_file_get_iter(*args):
    api_call = _invoke_api('security-certificate-file-get-iter', *args)
    return api_call

def security_certificate_generate_csr(*args):
    api_call = _invoke_api('security-certificate-generate-csr', *args)
    return api_call

def security_certificate_get_iter(*args):
    api_call = _invoke_api('security-certificate-get-iter', *args)
    return api_call

def security_certificate_install(*args):
    api_call = _invoke_api('security-certificate-install', *args)
    return api_call

def security_certificate_revoke(*args):
    api_call = _invoke_api('security-certificate-revoke', *args)
    return api_call

def security_certificate_sign(*args):
    api_call = _invoke_api('security-certificate-sign', *args)
    return api_call

def security_key_manager_add_iter(*args):
    api_call = _invoke_api('security-key-manager-add-iter', *args)
    return api_call

def security_key_manager_create_key(*args):
    api_call = _invoke_api('security-key-manager-create-key', *args)
    return api_call

def security_key_manager_delete_iter(*args):
    api_call = _invoke_api('security-key-manager-delete-iter', *args)
    return api_call

def security_key_manager_get(*args):
    api_call = _invoke_api('security-key-manager-get', *args)
    return api_call

def security_key_manager_get_iter(*args):
    api_call = _invoke_api('security-key-manager-get-iter', *args)
    return api_call

def security_key_manager_query_get(*args):
    api_call = _invoke_api('security-key-manager-query-get', *args)
    return api_call

def security_key_manager_query_get_iter(*args):
    api_call = _invoke_api('security-key-manager-query-get-iter', *args)
    return api_call

def security_key_manager_restore_get(*args):
    api_call = _invoke_api('security-key-manager-restore-get', *args)
    return api_call

def security_key_manager_restore_get_iter(*args):
    api_call = _invoke_api('security-key-manager-restore-get-iter', *args)
    return api_call

def security_key_manager_setup(*args):
    api_call = _invoke_api('security-key-manager-setup', *args)
    return api_call

def security_login_create(*args):
    api_call = _invoke_api('security-login-create', *args)
    return api_call

def security_login_delete(*args):
    api_call = _invoke_api('security-login-delete', *args)
    return api_call

def security_login_delete_iter(*args):
    api_call = _invoke_api('security-login-delete-iter', *args)
    return api_call

def security_login_get(*args):
    api_call = _invoke_api('security-login-get', *args)
    return api_call

def security_login_get_iter(*args):
    api_call = _invoke_api('security-login-get-iter', *args)
    return api_call

def security_login_lock(*args):
    api_call = _invoke_api('security-login-lock', *args)
    return api_call

def security_login_modify(*args):
    api_call = _invoke_api('security-login-modify', *args)
    return api_call

def security_login_modify_iter(*args):
    api_call = _invoke_api('security-login-modify-iter', *args)
    return api_call

def security_login_modify_password(*args):
    api_call = _invoke_api('security-login-modify-password', *args)
    return api_call

def security_login_role_config_get(*args):
    api_call = _invoke_api('security-login-role-config-get', *args)
    return api_call

def security_login_role_config_get_iter(*args):
    api_call = _invoke_api('security-login-role-config-get-iter', *args)
    return api_call

def security_login_role_config_modify(*args):
    api_call = _invoke_api('security-login-role-config-modify', *args)
    return api_call

def security_login_role_config_modify_iter(*args):
    api_call = _invoke_api('security-login-role-config-modify-iter', *args)
    return api_call

def security_login_role_create(*args):
    api_call = _invoke_api('security-login-role-create', *args)
    return api_call

def security_login_role_delete(*args):
    api_call = _invoke_api('security-login-role-delete', *args)
    return api_call

def security_login_role_delete_iter(*args):
    api_call = _invoke_api('security-login-role-delete-iter', *args)
    return api_call

def security_login_role_get(*args):
    api_call = _invoke_api('security-login-role-get', *args)
    return api_call

def security_login_role_get_iter(*args):
    api_call = _invoke_api('security-login-role-get-iter', *args)
    return api_call

def security_login_role_modify(*args):
    api_call = _invoke_api('security-login-role-modify', *args)
    return api_call

def security_login_role_modify_iter(*args):
    api_call = _invoke_api('security-login-role-modify-iter', *args)
    return api_call

def security_login_unlock(*args):
    api_call = _invoke_api('security-login-unlock', *args)
    return api_call

def security_reset(*args):
    api_call = _invoke_api('security-reset', *args)
    return api_call

def security_ssh_add(*args):
    api_call = _invoke_api('security-ssh-add', *args)
    return api_call

def security_ssh_get_iter(*args):
    api_call = _invoke_api('security-ssh-get-iter', *args)
    return api_call

def security_ssh_remove(*args):
    api_call = _invoke_api('security-ssh-remove', *args)
    return api_call

def security_ssl_get_iter(*args):
    api_call = _invoke_api('security-ssl-get-iter', *args)
    return api_call

def security_ssl_modify(*args):
    api_call = _invoke_api('security-ssl-modify', *args)
    return api_call

def security_trace_filter_get_iter(*args):
    api_call = _invoke_api('security-trace-filter-get-iter', *args)
    return api_call

def security_trace_result_show(*args):
    api_call = _invoke_api('security-trace-result-show', *args)
    return api_call

def service_processor_api_service_get(*args):
    api_call = _invoke_api('service-processor-api-service-get', *args)
    return api_call

def service_processor_api_service_modify(*args):
    api_call = _invoke_api('service-processor-api-service-modify', *args)
    return api_call

def service_processor_api_service_renew_certificates(*args):
    api_call = _invoke_api('service-processor-api-service-renew-certificates', *args)
    return api_call

def service_processor_asup_config_get(*args):
    api_call = _invoke_api('service-processor-asup-config-get', *args)
    return api_call

def service_processor_asup_config_set(*args):
    api_call = _invoke_api('service-processor-asup-config-set', *args)
    return api_call

def service_processor_asup_invoke(*args):
    api_call = _invoke_api('service-processor-asup-invoke', *args)
    return api_call

def service_processor_auto_configuration_disable(*args):
    api_call = _invoke_api('service-processor-auto-configuration-disable', *args)
    return api_call

def service_processor_auto_configuration_enable(*args):
    api_call = _invoke_api('service-processor-auto-configuration-enable', *args)
    return api_call

def service_processor_auto_configuration_get(*args):
    api_call = _invoke_api('service-processor-auto-configuration-get', *args)
    return api_call

def service_processor_get(*args):
    api_call = _invoke_api('service-processor-get', *args)
    return api_call

def service_processor_get_iter(*args):
    api_call = _invoke_api('service-processor-get-iter', *args)
    return api_call

def service_processor_image_get(*args):
    api_call = _invoke_api('service-processor-image-get', *args)
    return api_call

def service_processor_image_modify(*args):
    api_call = _invoke_api('service-processor-image-modify', *args)
    return api_call

def service_processor_image_update(*args):
    api_call = _invoke_api('service-processor-image-update', *args)
    return api_call

def service_processor_image_update_progress_get(*args):
    api_call = _invoke_api('service-processor-image-update-progress-get', *args)
    return api_call

def service_processor_log_allocation_get(*args):
    api_call = _invoke_api('service-processor-log-allocation-get', *args)
    return api_call

def service_processor_log_allocation_get_iter(*args):
    api_call = _invoke_api('service-processor-log-allocation-get-iter', *args)
    return api_call

def service_processor_network_get(*args):
    api_call = _invoke_api('service-processor-network-get', *args)
    return api_call

def service_processor_network_get_iter(*args):
    api_call = _invoke_api('service-processor-network-get-iter', *args)
    return api_call

def service_processor_network_modify(*args):
    api_call = _invoke_api('service-processor-network-modify', *args)
    return api_call

def service_processor_network_modify_iter(*args):
    api_call = _invoke_api('service-processor-network-modify-iter', *args)
    return api_call

def service_processor_reboot(*args):
    api_call = _invoke_api('service-processor-reboot', *args)
    return api_call

def service_processor_ssh_add_allowed_addresses(*args):
    api_call = _invoke_api('service-processor-ssh-add-allowed-addresses', *args)
    return api_call

def service_processor_ssh_get(*args):
    api_call = _invoke_api('service-processor-ssh-get', *args)
    return api_call

def service_processor_ssh_remove_allowed_addresses(*args):
    api_call = _invoke_api('service-processor-ssh-remove-allowed-addresses', *args)
    return api_call

def sis_get_iter(*args):
    api_call = _invoke_api('sis-get-iter', *args)
    return api_call

def sis_policy_get_iter(*args):
    api_call = _invoke_api('sis-policy-get-iter', *args)
    return api_call

def sis_prepare_to_downgrade(*args):
    api_call = _invoke_api('sis-prepare-to-downgrade', *args)
    return api_call

def sis_status(*args):
    api_call = _invoke_api('sis-status', *args)
    return api_call

def snapmirror_abort(*args):
    api_call = _invoke_api('snapmirror-abort', *args)
    return api_call

def snapmirror_abort_async(*args):
    api_call = _invoke_api('snapmirror-abort-async', *args)
    return api_call

def snapmirror_abort_iter(*args):
    api_call = _invoke_api('snapmirror-abort-iter', *args)
    return api_call

def snapmirror_break(*args):
    api_call = _invoke_api('snapmirror-break', *args)
    return api_call

def snapmirror_break_async(*args):
    api_call = _invoke_api('snapmirror-break-async', *args)
    return api_call

def snapmirror_break_iter(*args):
    api_call = _invoke_api('snapmirror-break-iter', *args)
    return api_call

def snapmirror_cache_rebuild_relationship(*args):
    api_call = _invoke_api('snapmirror-cache-rebuild-relationship', *args)
    return api_call

def snapmirror_check(*args):
    api_call = _invoke_api('snapmirror-check', *args)
    return api_call

def snapmirror_check_iter(*args):
    api_call = _invoke_api('snapmirror-check-iter', *args)
    return api_call

def snapmirror_config_replication_cluster_storage_configuration_get(*args):
    api_call = _invoke_api('snapmirror-config-replication-cluster-storage-configuration-get', *args)
    return api_call

def snapmirror_config_replication_cluster_storage_configuration_modify(*args):
    api_call = _invoke_api('snapmirror-config-replication-cluster-storage-configuration-modify', *args)
    return api_call

def snapmirror_cr_status_aggregate_eligibility_get(*args):
    api_call = _invoke_api('snapmirror-cr-status-aggregate-eligibility-get', *args)
    return api_call

def snapmirror_cr_status_aggregate_eligibility_get_iter(*args):
    api_call = _invoke_api('snapmirror-cr-status-aggregate-eligibility-get-iter', *args)
    return api_call

def snapmirror_cr_status_comm_get(*args):
    api_call = _invoke_api('snapmirror-cr-status-comm-get', *args)
    return api_call

def snapmirror_cr_status_comm_get_iter(*args):
    api_call = _invoke_api('snapmirror-cr-status-comm-get-iter', *args)
    return api_call

def snapmirror_cr_status_get(*args):
    api_call = _invoke_api('snapmirror-cr-status-get', *args)
    return api_call

def snapmirror_create(*args):
    api_call = _invoke_api('snapmirror-create', *args)
    return api_call

def snapmirror_destroy(*args):
    api_call = _invoke_api('snapmirror-destroy', *args)
    return api_call

def snapmirror_destroy_async(*args):
    api_call = _invoke_api('snapmirror-destroy-async', *args)
    return api_call

def snapmirror_destroy_iter(*args):
    api_call = _invoke_api('snapmirror-destroy-iter', *args)
    return api_call

def snapmirror_get(*args):
    api_call = _invoke_api('snapmirror-get', *args)
    return api_call

def snapmirror_get_destination(*args):
    api_call = _invoke_api('snapmirror-get-destination', *args)
    return api_call

def snapmirror_get_destination_iter(*args):
    api_call = _invoke_api('snapmirror-get-destination-iter', *args)
    return api_call

def snapmirror_get_iter(*args):
    api_call = _invoke_api('snapmirror-get-iter', *args)
    return api_call

def snapmirror_get_total_records(*args):
    api_call = _invoke_api('snapmirror-get-total-records', *args)
    return api_call

def snapmirror_get_volume_status(*args):
    api_call = _invoke_api('snapmirror-get-volume-status', *args)
    return api_call

def snapmirror_history_get(*args):
    api_call = _invoke_api('snapmirror-history-get', *args)
    return api_call

def snapmirror_history_get_iter(*args):
    api_call = _invoke_api('snapmirror-history-get-iter', *args)
    return api_call

def snapmirror_initialize(*args):
    api_call = _invoke_api('snapmirror-initialize', *args)
    return api_call

def snapmirror_initialize_iter(*args):
    api_call = _invoke_api('snapmirror-initialize-iter', *args)
    return api_call

def snapmirror_initialize_ls_set(*args):
    api_call = _invoke_api('snapmirror-initialize-ls-set', *args)
    return api_call

def snapmirror_modify(*args):
    api_call = _invoke_api('snapmirror-modify', *args)
    return api_call

def snapmirror_modify_iter(*args):
    api_call = _invoke_api('snapmirror-modify-iter', *args)
    return api_call

def snapmirror_policy_get_iter(*args):
    api_call = _invoke_api('snapmirror-policy-get-iter', *args)
    return api_call

def snapmirror_promote(*args):
    api_call = _invoke_api('snapmirror-promote', *args)
    return api_call

def snapmirror_promote_iter(*args):
    api_call = _invoke_api('snapmirror-promote-iter', *args)
    return api_call

def snapmirror_quiesce(*args):
    api_call = _invoke_api('snapmirror-quiesce', *args)
    return api_call

def snapmirror_quiesce_iter(*args):
    api_call = _invoke_api('snapmirror-quiesce-iter', *args)
    return api_call

def snapmirror_release(*args):
    api_call = _invoke_api('snapmirror-release', *args)
    return api_call

def snapmirror_release_iter(*args):
    api_call = _invoke_api('snapmirror-release-iter', *args)
    return api_call

def snapmirror_restore(*args):
    api_call = _invoke_api('snapmirror-restore', *args)
    return api_call

def snapmirror_resume(*args):
    api_call = _invoke_api('snapmirror-resume', *args)
    return api_call

def snapmirror_resume_iter(*args):
    api_call = _invoke_api('snapmirror-resume-iter', *args)
    return api_call

def snapmirror_resync(*args):
    api_call = _invoke_api('snapmirror-resync', *args)
    return api_call

def snapmirror_resync_iter(*args):
    api_call = _invoke_api('snapmirror-resync-iter', *args)
    return api_call

def snapmirror_snapshot_owner_get(*args):
    api_call = _invoke_api('snapmirror-snapshot-owner-get', *args)
    return api_call

def snapmirror_snapshot_owner_get_snapshots(*args):
    api_call = _invoke_api('snapmirror-snapshot-owner-get-snapshots', *args)
    return api_call

def snapmirror_update(*args):
    api_call = _invoke_api('snapmirror-update', *args)
    return api_call

def snapmirror_update_iter(*args):
    api_call = _invoke_api('snapmirror-update-iter', *args)
    return api_call

def snapmirror_update_ls_set(*args):
    api_call = _invoke_api('snapmirror-update-ls-set', *args)
    return api_call

def snapshot_get_iter(*args):
    api_call = _invoke_api('snapshot-get-iter', *args)
    return api_call

def snapshot_modify_iter(*args):
    api_call = _invoke_api('snapshot-modify-iter', *args)
    return api_call

def snapshot_policy_add_schedule(*args):
    api_call = _invoke_api('snapshot-policy-add-schedule', *args)
    return api_call

def snapshot_policy_create(*args):
    api_call = _invoke_api('snapshot-policy-create', *args)
    return api_call

def snapshot_policy_delete(*args):
    api_call = _invoke_api('snapshot-policy-delete', *args)
    return api_call

def snapshot_policy_get(*args):
    api_call = _invoke_api('snapshot-policy-get', *args)
    return api_call

def snapshot_policy_get_iter(*args):
    api_call = _invoke_api('snapshot-policy-get-iter', *args)
    return api_call

def snapshot_policy_modify(*args):
    api_call = _invoke_api('snapshot-policy-modify', *args)
    return api_call

def snapshot_policy_modify_schedule(*args):
    api_call = _invoke_api('snapshot-policy-modify-schedule', *args)
    return api_call

def snapshot_policy_remove_schedule(*args):
    api_call = _invoke_api('snapshot-policy-remove-schedule', *args)
    return api_call

def snapshot_reserve_list_info(*args):
    api_call = _invoke_api('snapshot-reserve-list-info', *args)
    return api_call

def snmp_community_add(*args):
    api_call = _invoke_api('snmp-community-add', *args)
    return api_call

def snmp_community_delete(*args):
    api_call = _invoke_api('snmp-community-delete', *args)
    return api_call

def snmp_community_delete_all(*args):
    api_call = _invoke_api('snmp-community-delete-all', *args)
    return api_call

def snmp_disable(*args):
    api_call = _invoke_api('snmp-disable', *args)
    return api_call

def snmp_enable(*args):
    api_call = _invoke_api('snmp-enable', *args)
    return api_call

def snmp_get(*args):
    api_call = _invoke_api('snmp-get', *args)
    return api_call

def snmp_get_next(*args):
    api_call = _invoke_api('snmp-get-next', *args)
    return api_call

def snmp_prepare_to_downgrade(*args):
    api_call = _invoke_api('snmp-prepare-to-downgrade', *args)
    return api_call

def snmp_status(*args):
    api_call = _invoke_api('snmp-status', *args)
    return api_call

def snmp_trap_disable(*args):
    api_call = _invoke_api('snmp-trap-disable', *args)
    return api_call

def snmp_trap_enable(*args):
    api_call = _invoke_api('snmp-trap-enable', *args)
    return api_call

def snmp_traphost_add(*args):
    api_call = _invoke_api('snmp-traphost-add', *args)
    return api_call

def snmp_traphost_delete(*args):
    api_call = _invoke_api('snmp-traphost-delete', *args)
    return api_call

def ssh_prepare_to_downgrade(*args):
    api_call = _invoke_api('ssh-prepare-to-downgrade', *args)
    return api_call

def storage_adapter_enable_adapter(*args):
    api_call = _invoke_api('storage-adapter-enable-adapter', *args)
    return api_call

def storage_adapter_get_adapter_info(*args):
    api_call = _invoke_api('storage-adapter-get-adapter-info', *args)
    return api_call

def storage_adapter_get_adapter_list(*args):
    api_call = _invoke_api('storage-adapter-get-adapter-list', *args)
    return api_call

def storage_array_get_config_summary(*args):
    api_call = _invoke_api('storage-array-get-config-summary', *args)
    return api_call

def storage_array_list_info(*args):
    api_call = _invoke_api('storage-array-list-info', *args)
    return api_call

def storage_array_modify(*args):
    api_call = _invoke_api('storage-array-modify', *args)
    return api_call

def storage_array_port_modify(*args):
    api_call = _invoke_api('storage-array-port-modify', *args)
    return api_call

def storage_array_ports_list_info(*args):
    api_call = _invoke_api('storage-array-ports-list-info', *args)
    return api_call

def storage_array_rename(*args):
    api_call = _invoke_api('storage-array-rename', *args)
    return api_call

def storage_bridge_get(*args):
    api_call = _invoke_api('storage-bridge-get', *args)
    return api_call

def storage_bridge_get_iter(*args):
    api_call = _invoke_api('storage-bridge-get-iter', *args)
    return api_call

def storage_disk_get_iter(*args):
    api_call = _invoke_api('storage-disk-get-iter', *args)
    return api_call

def storage_disk_modify(*args):
    api_call = _invoke_api('storage-disk-modify', *args)
    return api_call

def storage_disk_remove_reservation(*args):
    api_call = _invoke_api('storage-disk-remove-reservation', *args)
    return api_call

def storage_initiator_balance(*args):
    api_call = _invoke_api('storage-initiator-balance', *args)
    return api_call

def storage_initiator_disk_path_list_info(*args):
    api_call = _invoke_api('storage-initiator-disk-path-list-info', *args)
    return api_call

def storage_initiator_errors_list_info(*args):
    api_call = _invoke_api('storage-initiator-errors-list-info', *args)
    return api_call

def storage_initiator_get_load(*args):
    api_call = _invoke_api('storage-initiator-get-load', *args)
    return api_call

def storage_initiator_path_list_info(*args):
    api_call = _invoke_api('storage-initiator-path-list-info', *args)
    return api_call

def storage_initiator_path_quiesce(*args):
    api_call = _invoke_api('storage-initiator-path-quiesce', *args)
    return api_call

def storage_initiator_path_resume(*args):
    api_call = _invoke_api('storage-initiator-path-resume', *args)
    return api_call

def storage_pool_add(*args):
    api_call = _invoke_api('storage-pool-add', *args)
    return api_call

def storage_pool_aggregate_get_iter(*args):
    api_call = _invoke_api('storage-pool-aggregate-get-iter', *args)
    return api_call

def storage_pool_available_capacity_get_iter(*args):
    api_call = _invoke_api('storage-pool-available-capacity-get-iter', *args)
    return api_call

def storage_pool_create(*args):
    api_call = _invoke_api('storage-pool-create', *args)
    return api_call

def storage_pool_delete(*args):
    api_call = _invoke_api('storage-pool-delete', *args)
    return api_call

def storage_pool_disk_get_iter(*args):
    api_call = _invoke_api('storage-pool-disk-get-iter', *args)
    return api_call

def storage_pool_get_iter(*args):
    api_call = _invoke_api('storage-pool-get-iter', *args)
    return api_call

def storage_pool_reassign(*args):
    api_call = _invoke_api('storage-pool-reassign', *args)
    return api_call

def storage_shelf_acp_get(*args):
    api_call = _invoke_api('storage-shelf-acp-get', *args)
    return api_call

def storage_shelf_acp_module_get(*args):
    api_call = _invoke_api('storage-shelf-acp-module-get', *args)
    return api_call

def storage_shelf_acp_module_get_iter(*args):
    api_call = _invoke_api('storage-shelf-acp-module-get-iter', *args)
    return api_call

def storage_shelf_bay_list_info(*args):
    api_call = _invoke_api('storage-shelf-bay-list-info', *args)
    return api_call

def storage_shelf_environment_list_info(*args):
    api_call = _invoke_api('storage-shelf-environment-list-info', *args)
    return api_call

def storage_shelf_error_list_info(*args):
    api_call = _invoke_api('storage-shelf-error-list-info', *args)
    return api_call

def storage_shelf_firmware_update(*args):
    api_call = _invoke_api('storage-shelf-firmware-update', *args)
    return api_call

def storage_shelf_firmware_update_info_get(*args):
    api_call = _invoke_api('storage-shelf-firmware-update-info-get', *args)
    return api_call

def storage_shelf_firmware_update_info_get_iter(*args):
    api_call = _invoke_api('storage-shelf-firmware-update-info-get-iter', *args)
    return api_call

def storage_shelf_get_shelf_info(*args):
    api_call = _invoke_api('storage-shelf-get-shelf-info', *args)
    return api_call

def storage_shelf_info_get(*args):
    api_call = _invoke_api('storage-shelf-info-get', *args)
    return api_call

def storage_shelf_info_get_iter(*args):
    api_call = _invoke_api('storage-shelf-info-get-iter', *args)
    return api_call

def storage_shelf_list_info(*args):
    api_call = _invoke_api('storage-shelf-list-info', *args)
    return api_call

def storage_shelf_storage_acp_configure(*args):
    api_call = _invoke_api('storage-shelf-storage-acp-configure', *args)
    return api_call

def storage_switch_get(*args):
    api_call = _invoke_api('storage-switch-get', *args)
    return api_call

def storage_switch_get_iter(*args):
    api_call = _invoke_api('storage-switch-get-iter', *args)
    return api_call

def storage_transition_aggregates_get_iter(*args):
    api_call = _invoke_api('storage-transition-aggregates-get-iter', *args)
    return api_call

def storage_transition_aggregates_start(*args):
    api_call = _invoke_api('storage-transition-aggregates-start', *args)
    return api_call

def storage_transition_commit_get_iter(*args):
    api_call = _invoke_api('storage-transition-commit-get-iter', *args)
    return api_call

def storage_transition_commit_start(*args):
    api_call = _invoke_api('storage-transition-commit-start', *args)
    return api_call

def storage_transition_pre_commit_begin(*args):
    api_call = _invoke_api('storage-transition-pre-commit-begin', *args)
    return api_call

def storage_transition_pre_commit_end(*args):
    api_call = _invoke_api('storage-transition-pre-commit-end', *args)
    return api_call

def storage_transition_pre_commit_get(*args):
    api_call = _invoke_api('storage-transition-pre-commit-get', *args)
    return api_call

def storage_transition_pre_commit_get_iter(*args):
    api_call = _invoke_api('storage-transition-pre-commit-get-iter', *args)
    return api_call

def storage_transition_purge_info(*args):
    api_call = _invoke_api('storage-transition-purge-info', *args)
    return api_call

def storage_transition_revert_get_iter(*args):
    api_call = _invoke_api('storage-transition-revert-get-iter', *args)
    return api_call

def storage_transition_revert_start(*args):
    api_call = _invoke_api('storage-transition-revert-start', *args)
    return api_call

def storage_transition_volumes_get_iter(*args):
    api_call = _invoke_api('storage-transition-volumes-get-iter', *args)
    return api_call

def storage_transition_volumes_start(*args):
    api_call = _invoke_api('storage-transition-volumes-start', *args)
    return api_call

def system_api_change_get_iter(*args):
    api_call = _invoke_api('system-api-change-get-iter', *args)
    return api_call

def system_api_get_elements(*args):
    api_call = _invoke_api('system-api-get-elements', *args)
    return api_call

def system_api_list(*args):
    api_call = _invoke_api('system-api-list', *args)
    return api_call

def system_api_list_types(*args):
    api_call = _invoke_api('system-api-list-types', *args)
    return api_call

def system_cli(*args):
    api_call = _invoke_api('system-cli', *args)
    return api_call

def system_get_node_info_iter(*args):
    api_call = _invoke_api('system-get-node-info-iter', *args)
    return api_call

def system_get_ontapi_version(*args):
    api_call = _invoke_api('system-get-ontapi-version', *args)
    return api_call

def system_get_vendor_info(*args):
    api_call = _invoke_api('system-get-vendor-info', *args)
    return api_call

def system_get_version(*args):
    api_call = _invoke_api('system-get-version', *args)
    return api_call

def system_image_fetch_package(*args):
    api_call = _invoke_api('system-image-fetch-package', *args)
    return api_call

def system_image_get_iter(*args):
    api_call = _invoke_api('system-image-get-iter', *args)
    return api_call

def system_image_modify(*args):
    api_call = _invoke_api('system-image-modify', *args)
    return api_call

def system_image_package_delete(*args):
    api_call = _invoke_api('system-image-package-delete', *args)
    return api_call

def system_image_package_get_iter(*args):
    api_call = _invoke_api('system-image-package-get-iter', *args)
    return api_call

def system_image_update(*args):
    api_call = _invoke_api('system-image-update', *args)
    return api_call

def system_image_update_get_abort(*args):
    api_call = _invoke_api('system-image-update-get-abort', *args)
    return api_call

def system_image_update_progress_get(*args):
    api_call = _invoke_api('system-image-update-progress-get', *args)
    return api_call

def system_manager_upgrade(*args):
    api_call = _invoke_api('system-manager-upgrade', *args)
    return api_call

def system_node_delete_backlog_get(*args):
    api_call = _invoke_api('system-node-delete-backlog-get', *args)
    return api_call

def system_node_discovery_get_iter(*args):
    api_call = _invoke_api('system-node-discovery-get-iter', *args)
    return api_call

def system_node_get(*args):
    api_call = _invoke_api('system-node-get', *args)
    return api_call

def system_node_get_iter(*args):
    api_call = _invoke_api('system-node-get-iter', *args)
    return api_call

def system_node_modify(*args):
    api_call = _invoke_api('system-node-modify', *args)
    return api_call

def system_node_power_cycle(*args):
    api_call = _invoke_api('system-node-power-cycle', *args)
    return api_call

def system_node_power_get(*args):
    api_call = _invoke_api('system-node-power-get', *args)
    return api_call

def system_node_power_off(*args):
    api_call = _invoke_api('system-node-power-off', *args)
    return api_call

def system_node_power_on(*args):
    api_call = _invoke_api('system-node-power-on', *args)
    return api_call

def system_node_reboot(*args):
    api_call = _invoke_api('system-node-reboot', *args)
    return api_call

def system_node_rename(*args):
    api_call = _invoke_api('system-node-rename', *args)
    return api_call

def system_node_reset(*args):
    api_call = _invoke_api('system-node-reset', *args)
    return api_call

def system_node_revert_to(*args):
    api_call = _invoke_api('system-node-revert-to', *args)
    return api_call

def system_node_shutdown(*args):
    api_call = _invoke_api('system-node-shutdown', *args)
    return api_call

def system_ontapi_limits_get(*args):
    api_call = _invoke_api('system-ontapi-limits-get', *args)
    return api_call

def system_ontapi_limits_set(*args):
    api_call = _invoke_api('system-ontapi-limits-set', *args)
    return api_call

def system_services_web_get(*args):
    api_call = _invoke_api('system-services-web-get', *args)
    return api_call

def system_user_capability_get_iter(*args):
    api_call = _invoke_api('system-user-capability-get-iter', *args)
    return api_call

def tape_mc_get(*args):
    api_call = _invoke_api('tape-mc-get', *args)
    return api_call

def tape_mc_get_iter(*args):
    api_call = _invoke_api('tape-mc-get-iter', *args)
    return api_call

def tape_mc_info_alias_clear(*args):
    api_call = _invoke_api('tape-mc-info-alias-clear', *args)
    return api_call

def tape_mc_info_alias_set(*args):
    api_call = _invoke_api('tape-mc-info-alias-set', *args)
    return api_call

def tape_mc_info_offline(*args):
    api_call = _invoke_api('tape-mc-info-offline', *args)
    return api_call

def tape_mc_info_online(*args):
    api_call = _invoke_api('tape-mc-info-online', *args)
    return api_call

def tape_mc_info_position(*args):
    api_call = _invoke_api('tape-mc-info-position', *args)
    return api_call

def tape_mc_info_reset(*args):
    api_call = _invoke_api('tape-mc-info-reset', *args)
    return api_call

def tape_mc_info_test_release(*args):
    api_call = _invoke_api('tape-mc-info-test-release', *args)
    return api_call

def tape_mc_info_test_reserve(*args):
    api_call = _invoke_api('tape-mc-info-test-reserve', *args)
    return api_call

def tape_mc_info_trace(*args):
    api_call = _invoke_api('tape-mc-info-trace', *args)
    return api_call

def test_intrinsic_apis_1_create(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-create', *args)
    return api_call

def test_intrinsic_apis_1_destroy(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-destroy', *args)
    return api_call

def test_intrinsic_apis_1_destroy_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-destroy-iter', *args)
    return api_call

def test_intrinsic_apis_1_get(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-get', *args)
    return api_call

def test_intrinsic_apis_1_get_create_defaults(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-get-create-defaults', *args)
    return api_call

def test_intrinsic_apis_1_get_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-get-iter', *args)
    return api_call

def test_intrinsic_apis_1_get_total_records(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-get-total-records', *args)
    return api_call

def test_intrinsic_apis_1_list_info(*args):
    api_call = _invoke_api('test-intrinsic-apis-1-list-info', *args)
    return api_call

def test_intrinsic_apis_2_create(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-create', *args)
    return api_call

def test_intrinsic_apis_2_destroy(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-destroy', *args)
    return api_call

def test_intrinsic_apis_2_destroy_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-destroy-iter', *args)
    return api_call

def test_intrinsic_apis_2_get(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-get', *args)
    return api_call

def test_intrinsic_apis_2_get_create_defaults(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-get-create-defaults', *args)
    return api_call

def test_intrinsic_apis_2_get_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-get-iter', *args)
    return api_call

def test_intrinsic_apis_2_get_total_records(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-get-total-records', *args)
    return api_call

def test_intrinsic_apis_2_list_info(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-list-info', *args)
    return api_call

def test_intrinsic_apis_2_modify(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-modify', *args)
    return api_call

def test_intrinsic_apis_2_modify_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-2-modify-iter', *args)
    return api_call

def test_intrinsic_apis_3_create(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-create', *args)
    return api_call

def test_intrinsic_apis_3_destroy(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-destroy', *args)
    return api_call

def test_intrinsic_apis_3_destroy_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-destroy-iter', *args)
    return api_call

def test_intrinsic_apis_3_get(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-get', *args)
    return api_call

def test_intrinsic_apis_3_get_create_defaults(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-get-create-defaults', *args)
    return api_call

def test_intrinsic_apis_3_get_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-get-iter', *args)
    return api_call

def test_intrinsic_apis_3_get_total_records(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-get-total-records', *args)
    return api_call

def test_intrinsic_apis_3_list_info(*args):
    api_call = _invoke_api('test-intrinsic-apis-3-list-info', *args)
    return api_call

def test_intrinsic_apis_4_create(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-create', *args)
    return api_call

def test_intrinsic_apis_4_destroy(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-destroy', *args)
    return api_call

def test_intrinsic_apis_4_destroy_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-destroy-iter', *args)
    return api_call

def test_intrinsic_apis_4_get(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-get', *args)
    return api_call

def test_intrinsic_apis_4_get_create_defaults(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-get-create-defaults', *args)
    return api_call

def test_intrinsic_apis_4_get_iter(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-get-iter', *args)
    return api_call

def test_intrinsic_apis_4_get_total_records(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-get-total-records', *args)
    return api_call

def test_intrinsic_apis_4_list_info(*args):
    api_call = _invoke_api('test-intrinsic-apis-4-list-info', *args)
    return api_call

def test_key_optionality_alt_create(*args):
    api_call = _invoke_api('test-key-optionality-alt-create', *args)
    return api_call

def test_key_optionality_alt_destroy(*args):
    api_call = _invoke_api('test-key-optionality-alt-destroy', *args)
    return api_call

def test_key_optionality_alt_get(*args):
    api_call = _invoke_api('test-key-optionality-alt-get', *args)
    return api_call

def test_key_optionality_alt_modify(*args):
    api_call = _invoke_api('test-key-optionality-alt-modify', *args)
    return api_call

def test_key_optionality_create(*args):
    api_call = _invoke_api('test-key-optionality-create', *args)
    return api_call

def test_key_optionality_destroy(*args):
    api_call = _invoke_api('test-key-optionality-destroy', *args)
    return api_call

def test_key_optionality_get(*args):
    api_call = _invoke_api('test-key-optionality-get', *args)
    return api_call

def test_key_optionality_modify(*args):
    api_call = _invoke_api('test-key-optionality-modify', *args)
    return api_call

def test_memory_stats(*args):
    api_call = _invoke_api('test-memory-stats', *args)
    return api_call

def test_password_get(*args):
    api_call = _invoke_api('test-password-get', *args)
    return api_call

def test_password_set(*args):
    api_call = _invoke_api('test-password-set', *args)
    return api_call

def test_plug_leak(*args):
    api_call = _invoke_api('test-plug-leak', *args)
    return api_call

def test_ro_action_1_readonly3(*args):
    api_call = _invoke_api('test-ro-action-1-readonly3', *args)
    return api_call

def test_ro_action_2_readonly4(*args):
    api_call = _invoke_api('test-ro-action-2-readonly4', *args)
    return api_call

def test_ro_action_3_writable3(*args):
    api_call = _invoke_api('test-ro-action-3-writable3', *args)
    return api_call

def test_ro_method_readonly1(*args):
    api_call = _invoke_api('test-ro-method-readonly1', *args)
    return api_call

def test_ro_table_readonly1(*args):
    api_call = _invoke_api('test-ro-table-readonly1', *args)
    return api_call

def test_ro_table_writable1(*args):
    api_call = _invoke_api('test-ro-table-writable1', *args)
    return api_call

def test_rw_method_writable2(*args):
    api_call = _invoke_api('test-rw-method-writable2', *args)
    return api_call

def test_schema_validator(*args):
    api_call = _invoke_api('test-schema-validator', *args)
    return api_call

def test_zapi_ro_view_1_readonly6(*args):
    api_call = _invoke_api('test-zapi-ro-view-1-readonly6', *args)
    return api_call

def test_zapi_ro_view_1_writable4(*args):
    api_call = _invoke_api('test-zapi-ro-view-1-writable4', *args)
    return api_call

def test_zapi_ro_view_5_create(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-create', *args)
    return api_call

def test_zapi_ro_view_5_destroy(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-destroy', *args)
    return api_call

def test_zapi_ro_view_5_destroy_iter(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-destroy-iter', *args)
    return api_call

def test_zapi_ro_view_5_get(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-get', *args)
    return api_call

def test_zapi_ro_view_5_get_create_defaults(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-get-create-defaults', *args)
    return api_call

def test_zapi_ro_view_5_get_iter(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-get-iter', *args)
    return api_call

def test_zapi_ro_view_5_get_total_records(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-get-total-records', *args)
    return api_call

def test_zapi_ro_view_5_list_info(*args):
    api_call = _invoke_api('test-zapi-ro-view-5-list-info', *args)
    return api_call

def test_zapi_ro_view_6_create(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-create', *args)
    return api_call

def test_zapi_ro_view_6_destroy(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-destroy', *args)
    return api_call

def test_zapi_ro_view_6_destroy_iter(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-destroy-iter', *args)
    return api_call

def test_zapi_ro_view_6_get(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-get', *args)
    return api_call

def test_zapi_ro_view_6_get_create_defaults(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-get-create-defaults', *args)
    return api_call

def test_zapi_ro_view_6_get_iter(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-get-iter', *args)
    return api_call

def test_zapi_ro_view_6_get_total_records(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-get-total-records', *args)
    return api_call

def test_zapi_ro_view_6_list_info(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-list-info', *args)
    return api_call

def test_zapi_ro_view_6_modify(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-modify', *args)
    return api_call

def test_zapi_ro_view_6_modify_iter(*args):
    api_call = _invoke_api('test-zapi-ro-view-6-modify-iter', *args)
    return api_call

def test_zapi_sleep(*args):
    api_call = _invoke_api('test-zapi-sleep', *args)
    return api_call

def test_zapi_sleep_destroy_async_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-destroy-async-iter', *args)
    return api_call

def test_zapi_sleep_destroy_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-destroy-iter', *args)
    return api_call

def test_zapi_sleep_get_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-get-iter', *args)
    return api_call

def test_zapi_sleep_method_async_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-method-async-iter', *args)
    return api_call

def test_zapi_sleep_method_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-method-iter', *args)
    return api_call

def test_zapi_sleep_modify_async_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-modify-async-iter', *args)
    return api_call

def test_zapi_sleep_modify_iter(*args):
    api_call = _invoke_api('test-zapi-sleep-modify-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_create(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-create', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_destroy(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-destroy', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_destroy_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-destroy-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_get(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-get', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_get_create_defaults(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-get-create-defaults', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_get_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-get-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_get_total_records(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-get-total-records', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_list_info(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-list-info', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_modify(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-modify', *args)
    return api_call

def test_zapi_smf_mapping_apis_async_modify_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-async-modify-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_create(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-create', *args)
    return api_call

def test_zapi_smf_mapping_apis_destroy(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-destroy', *args)
    return api_call

def test_zapi_smf_mapping_apis_destroy_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-destroy-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_get(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-get', *args)
    return api_call

def test_zapi_smf_mapping_apis_get_create_defaults(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-get-create-defaults', *args)
    return api_call

def test_zapi_smf_mapping_apis_get_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-get-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_get_total_records(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-get-total-records', *args)
    return api_call

def test_zapi_smf_mapping_apis_list_info(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-list-info', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_async_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-async-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_async_no_query(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-async-no-query', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_create(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-create', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_default(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-default', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_default_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-default-iter', *args)
    return api_call

def test_zapi_smf_mapping_apis_method_only_get(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-method-only-get', *args)
    return api_call

def test_zapi_smf_mapping_apis_modify(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-modify', *args)
    return api_call

def test_zapi_smf_mapping_apis_modify_iter(*args):
    api_call = _invoke_api('test-zapi-smf-mapping-apis-modify-iter', *args)
    return api_call

def ucm_adapter_get(*args):
    api_call = _invoke_api('ucm-adapter-get', *args)
    return api_call

def ucm_adapter_get_iter(*args):
    api_call = _invoke_api('ucm-adapter-get-iter', *args)
    return api_call

def ucm_adapter_modify(*args):
    api_call = _invoke_api('ucm-adapter-modify', *args)
    return api_call

def unit_test_ktest_run(*args):
    api_call = _invoke_api('unit-test-ktest-run', *args)
    return api_call

def virtual_machine_get_info(*args):
    api_call = _invoke_api('virtual-machine-get-info', *args)
    return api_call

def virtual_machine_system_disks_get_iter(*args):
    api_call = _invoke_api('virtual-machine-system-disks-get-iter', *args)
    return api_call

def vmservices_vsphere_credential_check(*args):
    api_call = _invoke_api('vmservices-vsphere-credential-check', *args)
    return api_call

def vmservices_vsphere_credential_get(*args):
    api_call = _invoke_api('vmservices-vsphere-credential-get', *args)
    return api_call

def vmservices_vsphere_credential_modify(*args):
    api_call = _invoke_api('vmservices-vsphere-credential-modify', *args)
    return api_call

def volume_aggregate_vacate_async(*args):
    api_call = _invoke_api('volume-aggregate-vacate-async', *args)
    return api_call

def volume_autobalance_get_iter(*args):
    api_call = _invoke_api('volume-autobalance-get-iter', *args)
    return api_call

def volume_clone_get_iter(*args):
    api_call = _invoke_api('volume-clone-get-iter', *args)
    return api_call

def volume_copy_start(*args):
    api_call = _invoke_api('volume-copy-start', *args)
    return api_call

def volume_footprint_get_iter(*args):
    api_call = _invoke_api('volume-footprint-get-iter', *args)
    return api_call

def volume_get_iter(*args):
    api_call = _invoke_api('volume-get-iter', *args)
    return api_call

def volume_modify_iter(*args):
    api_call = _invoke_api('volume-modify-iter', *args)
    return api_call

def volume_modify_iter_async(*args):
    api_call = _invoke_api('volume-modify-iter-async', *args)
    return api_call

def volume_move_get_iter(*args):
    api_call = _invoke_api('volume-move-get-iter', *args)
    return api_call

def volume_move_modify(*args):
    api_call = _invoke_api('volume-move-modify', *args)
    return api_call

def volume_move_start(*args):
    api_call = _invoke_api('volume-move-start', *args)
    return api_call

def volume_move_target_aggr_get_iter(*args):
    api_call = _invoke_api('volume-move-target-aggr-get-iter', *args)
    return api_call

def volume_move_trigger_abort(*args):
    api_call = _invoke_api('volume-move-trigger-abort', *args)
    return api_call

def volume_move_trigger_cutover(*args):
    api_call = _invoke_api('volume-move-trigger-cutover', *args)
    return api_call

def volume_recovery_queue_get(*args):
    api_call = _invoke_api('volume-recovery-queue-get', *args)
    return api_call

def volume_recovery_queue_get_iter(*args):
    api_call = _invoke_api('volume-recovery-queue-get-iter', *args)
    return api_call

def volume_recovery_queue_modify_retention(*args):
    api_call = _invoke_api('volume-recovery-queue-modify-retention', *args)
    return api_call

def volume_recovery_queue_purge(*args):
    api_call = _invoke_api('volume-recovery-queue-purge', *args)
    return api_call

def volume_recovery_queue_recover(*args):
    api_call = _invoke_api('volume-recovery-queue-recover', *args)
    return api_call

def volume_rehost(*args):
    api_call = _invoke_api('volume-rehost', *args)
    return api_call

def volume_space_get_iter(*args):
    api_call = _invoke_api('volume-space-get-iter', *args)
    return api_call

def volume_storage_service_get_iter(*args):
    api_call = _invoke_api('volume-storage-service-get-iter', *args)
    return api_call

def volume_transition(*args):
    api_call = _invoke_api('volume-transition', *args)
    return api_call

def volume_transition_prepare_to_downgrade(*args):
    api_call = _invoke_api('volume-transition-prepare-to-downgrade', *args)
    return api_call

def volume_transition_protect(*args):
    api_call = _invoke_api('volume-transition-protect', *args)
    return api_call

def vscan_active_scanner_pool_get_iter(*args):
    api_call = _invoke_api('vscan-active-scanner-pool-get-iter', *args)
    return api_call

def vscan_connection_extended_stats_get_iter(*args):
    api_call = _invoke_api('vscan-connection-extended-stats-get-iter', *args)
    return api_call

def vscan_connection_status_all_get_iter(*args):
    api_call = _invoke_api('vscan-connection-status-all-get-iter', *args)
    return api_call

def vscan_events_get_iter(*args):
    api_call = _invoke_api('vscan-events-get-iter', *args)
    return api_call

def vscan_on_access_policy_get_iter(*args):
    api_call = _invoke_api('vscan-on-access-policy-get-iter', *args)
    return api_call

def vscan_scanner_pool_get_iter(*args):
    api_call = _invoke_api('vscan-scanner-pool-get-iter', *args)
    return api_call

def vscan_status_get_iter(*args):
    api_call = _invoke_api('vscan-status-get-iter', *args)
    return api_call

def vserver_add_aggregates(*args):
    api_call = _invoke_api('vserver-add-aggregates', *args)
    return api_call

def vserver_add_protocols(*args):
    api_call = _invoke_api('vserver-add-protocols', *args)
    return api_call

def vserver_config_diff_get(*args):
    api_call = _invoke_api('vserver-config-diff-get', *args)
    return api_call

def vserver_config_diff_get_iter(*args):
    api_call = _invoke_api('vserver-config-diff-get-iter', *args)
    return api_call

def vserver_create(*args):
    api_call = _invoke_api('vserver-create', *args)
    return api_call

def vserver_destroy(*args):
    api_call = _invoke_api('vserver-destroy', *args)
    return api_call

def vserver_get_iter(*args):
    api_call = _invoke_api('vserver-get-iter', *args)
    return api_call

def vserver_login_banner_get_iter(*args):
    api_call = _invoke_api('vserver-login-banner-get-iter', *args)
    return api_call

def vserver_login_banner_modify_iter(*args):
    api_call = _invoke_api('vserver-login-banner-modify-iter', *args)
    return api_call

def vserver_modify(*args):
    api_call = _invoke_api('vserver-modify', *args)
    return api_call

def vserver_modify_iter(*args):
    api_call = _invoke_api('vserver-modify-iter', *args)
    return api_call

def vserver_motd_get_iter(*args):
    api_call = _invoke_api('vserver-motd-get-iter', *args)
    return api_call

def vserver_motd_modify_iter(*args):
    api_call = _invoke_api('vserver-motd-modify-iter', *args)
    return api_call

def vserver_peer_accept(*args):
    api_call = _invoke_api('vserver-peer-accept', *args)
    return api_call

def vserver_peer_check_peer_table(*args):
    api_call = _invoke_api('vserver-peer-check-peer-table', *args)
    return api_call

def vserver_peer_create(*args):
    api_call = _invoke_api('vserver-peer-create', *args)
    return api_call

def vserver_peer_delete(*args):
    api_call = _invoke_api('vserver-peer-delete', *args)
    return api_call

def vserver_peer_get_iter(*args):
    api_call = _invoke_api('vserver-peer-get-iter', *args)
    return api_call

def vserver_peer_modify(*args):
    api_call = _invoke_api('vserver-peer-modify', *args)
    return api_call

def vserver_peer_reject(*args):
    api_call = _invoke_api('vserver-peer-reject', *args)
    return api_call

def vserver_peer_resume(*args):
    api_call = _invoke_api('vserver-peer-resume', *args)
    return api_call

def vserver_peer_suspend(*args):
    api_call = _invoke_api('vserver-peer-suspend', *args)
    return api_call

def vserver_peer_transition_create(*args):
    api_call = _invoke_api('vserver-peer-transition-create', *args)
    return api_call

def vserver_peer_transition_destroy(*args):
    api_call = _invoke_api('vserver-peer-transition-destroy', *args)
    return api_call

def vserver_peer_transition_destroy_iter(*args):
    api_call = _invoke_api('vserver-peer-transition-destroy-iter', *args)
    return api_call

def vserver_peer_transition_get(*args):
    api_call = _invoke_api('vserver-peer-transition-get', *args)
    return api_call

def vserver_peer_transition_get_iter(*args):
    api_call = _invoke_api('vserver-peer-transition-get-iter', *args)
    return api_call

def vserver_peer_transition_modify(*args):
    api_call = _invoke_api('vserver-peer-transition-modify', *args)
    return api_call

def vserver_remove_aggregates(*args):
    api_call = _invoke_api('vserver-remove-aggregates', *args)
    return api_call

def vserver_remove_protocols(*args):
    api_call = _invoke_api('vserver-remove-protocols', *args)
    return api_call

def vserver_rename(*args):
    api_call = _invoke_api('vserver-rename', *args)
    return api_call

def vserver_saninit(*args):
    api_call = _invoke_api('vserver-saninit', *args)
    return api_call

def vserver_start(*args):
    api_call = _invoke_api('vserver-start', *args)
    return api_call

def vserver_stop(*args):
    api_call = _invoke_api('vserver-stop', *args)
    return api_call

def vserver_unlock(*args):
    api_call = _invoke_api('vserver-unlock', *args)
    return api_call

def xml_to_dict(xml):
    return xmltodict.parse(xml)

def normalize_unicode(result):
    '''
    Takes the dictionary @result from xml_to_dict and normalizes the
    unicode characters.

    Returns a new dictionary with no more unicode characters
    '''
    d = {}
    for key,value in result.iteritems():
        if isinstance(key, unicode):
            key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore')
        if isinstance(value, unicode):
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
        d[key] = value
    return d

def apicall_to_dict(api_call):
    '''
    Takes the apicall result, and transforms it into a dictionary
    '''
    xml = api_call.sprintf()
    return xml_to_dict(xml)

def _invoke_api(*args):
    api = NaElement(*args)
    call = conn.invoke_elem(api)
    if call.results_errno() != 0:
        raise IOError('Failed api call=%s, errno=%s, desc=%s'
            %(args, call.results_errno(), call.sprintf())
        )
    return call

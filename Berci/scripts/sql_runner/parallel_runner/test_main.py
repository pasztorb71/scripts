from operator import itemgetter
from unittest import TestCase

import sql_runner.parallel_runner.main


class Test(TestCase):
    def test_gen_port_databases_from_envs(self):
        expected = [['5432', 'core_analytic'], ['5432', 'core_customer'], ['5432', 'core_notification_dispatcher'],
                    ['5432', 'core_vehicle'], ['5432', 'enforcement_detection_alert'],
                    ['5432', 'enforcement_detection_observation'], ['5432', 'enforcement_detection_transit_identifier'],
                    ['5432', 'enforcement_onsite_alert_subscribe'], ['5432', 'enforcement_visual_check'],
                    ['5432', 'eobu_trip'], ['5432', 'payment_invoice'], ['5432', 'payment_transaction'],
                    ['5432', 'settlement_tro_clearing'], ['5432', 'enforcement_detection_transition'],
                    ['5432', 'enforcement_onsite_alert'], ['5432', 'enforcement_detection_image'],
                    ['5432', 'core_genos'], ['5432', 'obu_obuprovider'],
                    ['5432', 'settlement_psp_clearing'], ['5432', 'enforcement_sanctioning_presumption'],
                    ['5432', 'core_privateuser'], ['5432', 'doc_document'], ['5432', 'enforcement_detection'],
                    ['5432', 'enforcement_onsite_inspection'], ['5432', 'core_notification_email'],
                    ['5432', 'core_notification_wa'], ['5432', 'core_ticket'], ['5432', 'enforcement_exemption'],
                    ['5432', 'enforcement_sanctioning_sanction'], ['5432', 'eobu_tariff'], ['5432', 'payment_psp_proxy'],
                    ['5432', 'payment_account_info'], ['5432', 'enforcement_eligibility']]
        sorted_expected = sorted(expected, key=itemgetter(0,1))
        result = sql_runner.parallel_runner.main.gen_port_databases_from_envs(['local'])
        sorted_result = sorted(result, key=itemgetter(0, 1))
        self.assertListEqual(sorted_expected, sorted_result)

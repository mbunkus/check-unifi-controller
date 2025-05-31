#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

##  MIT License
##
##  Copyright (c) 2021 Bash Club
##
##  Permission is hereby granted, free of charge, to any person obtaining a copy
##  of this software and associated documentation files (the "Software"), to deal
##  in the Software without restriction, including without limitation the rights
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the Software is
##  furnished to do so, subject to the following conditions:
##
##  The above copyright notice and this permission notice shall be included in all
##  copies or substantial portions of the Software.
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##  SOFTWARE.

from cmk.graphing.v1 import (
    Title,
    graphs,
    metrics,
    translations,
)

UNIT_AMPERAGE         = metrics.Unit(metrics.DecimalNotation("A"), metrics.AutoPrecision(3))
UNIT_BYTES_PER_SECOND = metrics.Unit(metrics.IECNotation("B/s"))
UNIT_COUNT            = metrics.Unit(metrics.DecimalNotation(""), metrics.StrictPrecision(0))
UNIT_DB               = metrics.Unit(metrics.DecimalNotation("db"))
UNIT_NUMBER           = metrics.Unit(metrics.DecimalNotation(""), metrics.StrictPrecision(2))
UNIT_PERCENTAGE       = metrics.Unit(metrics.DecimalNotation("%"))
UNIT_TIME             = metrics.Unit(metrics.TimeNotation())
UNIT_VOLTAGE          = metrics.Unit(metrics.DecimalNotation("V"), metrics.AutoPrecision(3))
UNIT_WATTAGE          = metrics.Unit(metrics.DecimalNotation("W"), metrics.AutoPrecision(3))

metric_unifi_satisfaction = metrics.Metric(
    name="satisfaction",
    title=Title("Satisfaction"),
    unit=UNIT_PERCENTAGE,
    color=metrics.Color.DARK_YELLOW,
)

metric_unifi_poe_current = metrics.Metric(
    name="poe_current",
    title=Title("PoE Current"),
    unit=UNIT_AMPERAGE,
    color=metrics.Color.DARK_YELLOW,
)
metric_unifi_poe_voltage = metrics.Metric(
    name="poe_voltage",
    title=Title("PoE Voltage"),
    unit=UNIT_VOLTAGE,
    color=metrics.Color.PURPLE,
)
metric_unifi_poe_power = metrics.Metric(
    name="poe_power",
    title=Title("PoE Power"),
    unit=UNIT_WATTAGE,
    color=metrics.Color.ORANGE,
)

metric_unifi_user_sta = metrics.Metric(
    name="user_sta",
    title=Title("User"),
    unit=UNIT_COUNT,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_guest_sta = metrics.Metric(
    name="guest_sta",
    title=Title("Guest"),
    unit=UNIT_COUNT,
    color=metrics.Color.LIGHT_PURPLE,
)

graph_unifi_user_sta_combined = graphs.Graph(
    name="user_sta_combined",
    title=Title("User"),
    simple_lines=[
        "user_sta",
        "guest_sta",
    ],
)

metric_unifi_lan_user_sta = metrics.Metric(
    name="lan_user_sta",
    title=Title("LAN User"),
    unit=UNIT_COUNT,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_lan_guest_sta = metrics.Metric(
    name="lan_guest_sta",
    title=Title("LAN Guest"),
    unit=UNIT_COUNT,
    color=metrics.Color.LIGHT_PURPLE,
)

graph_unifi_lan_user_sta_combined = graphs.Graph(
    name="lan_user_sta_combined",
    title=Title("LAN-User"),
    simple_lines=[
        "lan_user_sta",
        "lan_guest_sta",
    ],
)


metric_unifi_lan_active_sw = metrics.Metric(
    name="lan_active_sw",
    title=Title("Active Switches"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_lan_total_sw = metrics.Metric(
    name="lan_total_sw",
    title=Title("Total Switches"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_PURPLE,
)

graph_unifi_lan_active_sw_combined = graphs.Graph(
    name="lan_active_sw_combined",
    title=Title("Active Switches"),
    simple_lines=[
        "lan_active_sw",
        "lan_total_sw",
    ],
)
metric_unifi_wlan_active_ap = metrics.Metric(
    name="wlan_active_ap",
    title=Title("Active Accesspoints"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_wlan_total_ap = metrics.Metric(
    name="wlan_total_ap",
    title=Title("Total Accesspoints"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_PURPLE,
)

graph_unifi_wlan_active_ap_combined = graphs.Graph(
    name="wlan_active_ap_combined",
    title=Title("Active Accesspoints"),
    simple_lines=[
        "wlan_active_ap",
        "wlan_total_ap",
    ],
)

metric_unifi_wlan_user_sta = metrics.Metric(
    name="wlan_user_sta",
    title=Title("WLAN User"),
    unit=UNIT_COUNT,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_wlan_guest_sta = metrics.Metric(
    name="wlan_guest_sta",
    title=Title("WLAN Guest"),
    unit=UNIT_COUNT,
    color=metrics.Color.LIGHT_PURPLE,
)
metric_unifi_wlan_iot_sta = metrics.Metric(
    name="wlan_iot_sta",
    title=Title("WLAN IoT Devices"),
    unit=UNIT_COUNT,
    color=metrics.Color.DARK_ORANGE,
)

graph_unifi_wlan_user_sta_combined = graphs.Graph(
    name="wlan_user_sta_combined",
    title=Title("WLAN-User"),
    simple_lines=[
        "wlan_user_sta",
        "wlan_guest_sta",
        "wlan_iot_sta",
    ],
)

metric_unifi_wlan_24Ghz_num_user = metrics.Metric(
    name="wlan_24Ghz_num_user",
    title=Title("User 2.4Ghz"),
    unit=UNIT_COUNT,
    color=metrics.Color.DARK_PURPLE,
)
metric_unifi_wlan_5Ghz_num_user = metrics.Metric(
    name="wlan_5Ghz_num_user",
    title=Title("User 5Ghz"),
    unit=UNIT_COUNT,
    color=metrics.Color.LIGHT_PURPLE,
)

graph_unifi_wlan_user_band_combined = graphs.Graph(
    name="wlan_user_band_combined",
    title=Title("WLAN User"),
    simple_lines=[
        "wlan_24Ghz_num_user",
        "wlan_5Ghz_num_user",
    ],
)

#na_avg_client_signal
#ng_avg_client_signal


metric_unifi_wlan_if_in_octets = metrics.Metric(
    name="wlan_if_in_octets",
    title=Title("Input Octets"),
    unit=UNIT_BYTES_PER_SECOND,
    color=metrics.Color.GREEN,
)
metric_unifi_wlan_if_out_octets = metrics.Metric(
    name="wlan_if_out_octets",
    title=Title("Output Octets"),
    unit=UNIT_BYTES_PER_SECOND,
    color=metrics.Color.BLUE,
)
graph_unifi_wlan_bandwidth_translated = graphs.Graph(
    name="wlan_bandwidth_translated",
    title=Title("Bandwidth WLAN"),
    simple_lines=[
        "wlan_if_in_octets",
        "wlan_if_out_octets",
    ],
)


metric_unifi_na_avg_client_signal = metrics.Metric(
    name="na_avg_client_signal",
    title=Title("Average Signal 5Ghz"),
    unit=UNIT_DB,
    color=metrics.Color.RED,
)
metric_unifi_ng_avg_client_signal = metrics.Metric(
    name="ng_avg_client_signal",
    title=Title("Average Signal 2.4Ghz"),
    unit=UNIT_DB,
    color=metrics.Color.GREEN,
)
graph_unifi_avg_client_signal_combined = graphs.Graph(
    name="avg_client_signal_combined",
    title=Title("Average Client Signal"),
    simple_lines=[
        "na_avg_client_signal",
        "ng_avg_client_signal",
    ],
)

metric_unifi_unifi_uptime = metrics.Metric(
    name="unifi_uptime",
    title=Title("Uptime"),
    unit=UNIT_TIME,
    color=metrics.Color.YELLOW,
)

translation_unifi_interfaces = translations.Translation(
    name="unifi_interfaces",
    check_commands=[translations.PassiveCheck("unifi_network_ports_if")],
    translations={
        "in": translations.RenameToAndScaleBy("if_in_bps", 8),
        "out": translations.RenameToAndScaleBy("if_out_bps", 8),
        "total": translations.RenameToAndScaleBy("if_total_bps", 8),
        "indisc": translations.RenameTo("if_in_discards"),
        "inerr": translations.RenameTo("if_in_errors"),
        "outdisc": translations.RenameTo("if_out_discards"),
        "outerr": translations.RenameTo("if_out_errors"),
        "inmcast": translations.RenameTo("if_in_mcast"),
        "inbcast": translations.RenameTo("if_in_bcast"),
        "outmcast": translations.RenameTo("if_out_mcast"),
        "outbcast": translations.RenameTo("if_out_bcast"),
        "inucast": translations.RenameTo("if_in_unicast"),
        "innucast": translations.RenameTo("if_in_non_unicast"),
        "outucast": translations.RenameTo("if_out_unicast"),
        "outnucast": translations.RenameTo("if_out_non_unicast"),
    },
)

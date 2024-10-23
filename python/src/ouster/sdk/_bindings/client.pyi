"""
Copyright (c) 2021, Ouster, Inc.
All rights reserved.

Type annotations for the sensor client python bindings.

This is a mypy stub file defining just the type signatures of the module
generated by pybind11. It was generated using the ``stubgen`` utility and then
modified.

Note:
    This file should be updated whenever the bindings are modified.

"""
# flake8: noqa (linter complains about scoping, but afaict mypy doesn't care)

import numpy as np
from numpy import ndarray
from typing import (Any, ClassVar, Dict, Iterator, List, Optional, overload, Tuple)

from ouster.sdk.client.data import (BufferT, ColHeader, FieldDType, FieldTypes)


SHORT_HTTP_REQUEST_TIMEOUT_SECONDS: int
LONG_HTTP_REQUEST_TIMEOUT_SECONDS: int


class PacketValidationFailure:
    NONE: ClassVar[PacketValidationFailure]
    ID: ClassVar[PacketValidationFailure]
    PACKET_SIZE: ClassVar[PacketValidationFailure]

    __members__: ClassVar[Dict[str, PacketValidationFailure]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> PacketValidationFailure:
        ...


class Packet:
    host_timestamp: int
    capture_timestamp: Optional[float]

    def __init__(self, size: int = ...) -> None:
        ...

    @property
    def buf(self) -> ndarray:
        ...


class LidarPacket(Packet):
    def validate(self, metadata: SensorInfo, packet_format: PacketFormat) -> PacketValidationFailure:
        ...


class ImuPacket(Packet):
    def validate(self, metadata: SensorInfo, packet_format: PacketFormat) -> PacketValidationFailure:
        ...


class SensorConnection:
    @overload
    def __init__(self,
                 hostname: str = ...,
                 lidar_port: int = ...,
                 imu_port: int = ...) -> None:
        ...

    @overload
    def __init__(self,
                 hostname: str = ...,
                 udp_dest_host: str = ...,
                 mode: LidarMode = ...,
                 timestamp_mode: TimestampMode = ...,
                 lidar_port: int = ...,
                 imu_port: int = ...,
                 timeout_sec: int = ...,
                 persist_config: bool = ...) -> None:
        ...

    def poll(self, timeout_sec: int) -> ClientState:
        ...

    def read_lidar_packet(self, packet: LidarPacket, pf: PacketFormat) -> bool:
        ...

    def read_imu_packet(self, packet: ImuPacket, pf: PacketFormat) -> bool:
        ...

    @property
    def lidar_port(self) -> int:
        ...

    @property
    def imu_port(self) -> int:
        ...

    def get_metadata(self, timeout_sec: int) -> str:
        ...

    def shutdown(self) -> None:
        ...


class SensorHttp:
    def metadata(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def sensor_info(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def get_config_params(self, active: bool, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> str:
        ...

    def set_config_params(self, key: str, value: str, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def active_config_params(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def staged_config_params(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def set_udp_dest_auto(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def beam_intrinsics(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def imu_intrinsics(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def lidar_intrinsics(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def lidar_data_format(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> dict:
        ...

    def reinitialize(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def save_config_params(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def get_user_data(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> str:
        ...

    def set_user_data(self, user_data: str, keep_on_config_delete: bool, timeout_sec: int =
    SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def delete_user_data(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def network(self, timeout_sec: int = SHORT_HTTP_REQUEST_TIMEOUT_SECONDS) -> None:
        ...

    def hostname(self) -> str:
        ...

    def firmware_version(self) -> Version:
        ...

    @staticmethod
    def create(hostname: str, timeout_sec: int = LONG_HTTP_REQUEST_TIMEOUT_SECONDS) -> SensorHttp:
        ...
 

class ClientState:
    ERROR: ClassVar[ClientState]
    EXIT: ClassVar[ClientState]
    IMU_DATA: ClassVar[ClientState]
    LIDAR_DATA: ClassVar[ClientState]
    TIMEOUT: ClassVar[ClientState]

    __members__: ClassVar[Dict[str, ClientState]]

    def __init__(self, x: int) -> None:
        ...

    def __and__(self, s: ClientState) -> int:
        ...

    def __int__(self) -> int:
        ...

    def __invert__(self) -> int:
        ...

    def __or__(self, s: ClientState) -> int:
        ...

    def __xor__(self, s: ClientState) -> int:
        ...


class ClientEventType:
    Error: ClassVar[ClientEventType]
    Exit: ClassVar[ClientEventType]
    PollTimeout: ClassVar[ClientEventType]
    ImuPacket: ClassVar[ClientEventType]
    LidarPacket: ClassVar[ClientEventType]

    def __init__(self, x: int) -> None:
        ...


class ClientEvent:
    source: int
    type: ClientEventType


class ProductInfo:
    full_product_info: str
    form_factor: str
    short_range: bool
    beam_config: str
    beam_count: int


class SensorInfo:
    sn: str
    fw_rev: str
    prod_line: str
    format: DataFormat
    beam_azimuth_angles: List[float]
    beam_altitude_angles: List[float]
    imu_to_sensor_transform: ndarray
    lidar_to_sensor_transform: ndarray
    lidar_origin_to_beam_origin_mm: float
    beam_to_lidar_transform: ndarray
    extrinsic: ndarray
    init_id: int
    build_date: str
    image_rev: str
    prod_pn: str
    status: str
    cal: SensorCalibration
    config: SensorConfig
    user_data: str

    @classmethod
    def from_default(cls, mode: LidarMode) -> SensorInfo:
        ...

    @classmethod
    def to_json_string(cls) -> str:
        ...

    @classmethod
    def get_version(self) -> Version:
        ...

    @classmethod
    def get_product_info(self) -> ProductInfo:
        ...

    @classmethod
    def has_fields_equal(self, info: SensorInfo) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, metadata: str) -> None:
        ...

    @overload
    def __init__(self, metadata: str, skip_beam_validation: bool) -> None:
        ...

    @property
    def w(self) -> int:
        ...

    @property
    def h(self) -> int:
        ...


class DataFormat:
    columns_per_frame: int
    columns_per_packet: int
    pixel_shift_by_row: List[int]
    pixels_per_column: int
    column_window: Tuple[int, int]
    udp_profile_lidar: UDPProfileLidar
    udp_profile_imu: UDPProfileIMU
    fps: int


class PacketFormat:
    def __init__(self, metadata: SensorInfo) -> None:
        ...

    @property
    def lidar_packet_size(self) -> int:
        ...

    @property
    def imu_packet_size(self) -> int:
        ...

    @property
    def udp_profile_lidar(self) -> UDPProfileLidar:
        ...

    @property
    def columns_per_packet(self) -> int:
        ...

    @property
    def pixels_per_column(self) -> int:
        ...

    @property
    def packet_header_size(self) -> int:
        ...

    @property
    def col_header_size(self) -> int:
        ...

    @property
    def col_footer_size(self) -> int:
        ...

    @property
    def col_size(self) -> int:
        ...

    @property
    def packet_footer_size(self) -> int:
        ...

    @property
    def max_frame_id(self) -> int:
        ...

    def packet_type(self, buf: BufferT) -> int:
        ...

    def frame_id(self, buf: BufferT) -> int:
        ...

    def prod_sn(self, buf: BufferT) -> int:
        ...

    def init_id(self, buf: BufferT) -> int:
        ...

    def countdown_thermal_shutdown(self, buf: BufferT) -> int:
        ...

    def countdown_shot_limiting(self, buf: BufferT) -> int:
        ...

    def thermal_shutdown(self, buf: BufferT) -> int:
        ...

    def shot_limiting(self, buf: BufferT) -> int:
        ...

    def crc(self, buf: BufferT) -> Optional[int]:
        ...

    def calculate_crc(self, buf: BufferT) -> int:
        ...

    @property
    def fields(self) -> Iterator[str]:
        ...

    def field_value_mask(self, field: str) -> int:
        ...

    def field_bitness(self, field: str) -> int:
        ...

    def packet_field(self, field: str, buf: BufferT) -> ndarray:
        ...

    def packet_header(self, header: ColHeader, buf: BufferT) -> ndarray:
        ...

    def imu_sys_ts(self, buf: BufferT) -> int:
        ...

    def imu_accel_ts(self, buf: BufferT) -> int:
        ...

    def imu_gyro_ts(self, buf: BufferT) -> int:
        ...

    def imu_av_x(self, buf: BufferT) -> float:
        ...

    def imu_av_y(self, buf: BufferT) -> float:
        ...

    def imu_av_z(self, buf: BufferT) -> float:
        ...

    def imu_la_x(self, buf: BufferT) -> float:
        ...

    def imu_la_y(self, buf: BufferT) -> float:
        ...

    def imu_la_z(self, buf: BufferT) -> float:
        ...

    @staticmethod
    def from_info(info: SensorInfo) -> PacketFormat:
        ...

    @staticmethod
    def from_metadata(info: SensorInfo) -> PacketFormat:
        ...

    @staticmethod
    def from_profile(udp_profile_lidar: UDPProfileLidar,
                     pixels_per_column: int,
                     columns_per_packet: int) -> PacketFormat:
        ...


class PacketWriter(PacketFormat):
    @staticmethod
    def from_info(info: SensorInfo) -> PacketWriter:
        ...

    @staticmethod
    def from_profile(udp_profile_lidar: UDPProfileLidar,
                     pixels_per_column: int,
                     columns_per_packet: int) -> PacketWriter:
        ...

    def set_col_timestamp(self, packet: LidarPacket, col_idx: int, ts: int) -> None:
        ...

    def set_col_measurement_id(self,
                               packet: LidarPacket,
                               col_idx: int,
                               m_id: int) -> None:
        ...

    def set_col_status(self, packet: LidarPacket, col_idx: int, status: int) -> None:
        ...

    def set_frame_id(self, packet: LidarPacket, frame_id: int) -> None:
        ...

    def set_field(self, packet: LidarPacket, chan: str, field: ndarray) -> None:
        ...


def scan_to_packets(ls: LidarScan, pw: PacketWriter, init_id: int, prod_sn: int) -> List[LidarPacket]:
    ...


class LidarMode:
    MODE_UNSPEC: ClassVar[LidarMode]
    MODE_512x10: ClassVar[LidarMode]
    MODE_512x20: ClassVar[LidarMode]
    MODE_1024x10: ClassVar[LidarMode]
    MODE_1024x20: ClassVar[LidarMode]
    MODE_2048x10: ClassVar[LidarMode]
    MODE_4096x5: ClassVar[LidarMode]

    __members__: ClassVar[Dict[str, LidarMode]]
    values: ClassVar[Iterator[LidarMode]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> LidarMode:
        ...


class TimestampMode:
    TIME_FROM_UNSPEC: ClassVar[TimestampMode]
    TIME_FROM_INTERNAL_OSC: ClassVar[TimestampMode]
    TIME_FROM_PTP_1588: ClassVar[TimestampMode]
    TIME_FROM_SYNC_PULSE_IN: ClassVar[TimestampMode]

    __members__: ClassVar[Dict[str, TimestampMode]]
    values: ClassVar[Iterator[TimestampMode]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> TimestampMode:
        ...


class OperatingMode:
    OPERATING_NORMAL: ClassVar[OperatingMode]
    OPERATING_STANDBY: ClassVar[OperatingMode]

    __members__: ClassVar[Dict[str, OperatingMode]]
    values: ClassVar[Iterator[OperatingMode]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> OperatingMode:
        ...


class MultipurposeIOMode:
    MULTIPURPOSE_OFF: ClassVar[MultipurposeIOMode]
    MULTIPURPOSE_INPUT_NMEA_UART: ClassVar[MultipurposeIOMode]
    MULTIPURPOSE_OUTPUT_FROM_INTERNAL_OSC: ClassVar[MultipurposeIOMode]
    MULTIPURPOSE_OUTPUT_FROM_SYNC_PULSE_IN: ClassVar[MultipurposeIOMode]
    MULTIPURPOSE_OUTPUT_FROM_PTP_1588: ClassVar[MultipurposeIOMode]
    MULTIPURPOSE_OUTPUT_FROM_ENCODER_ANGLE: ClassVar[MultipurposeIOMode]

    __members__: ClassVar[Dict[str, MultipurposeIOMode]]
    values: ClassVar[Iterator[MultipurposeIOMode]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> MultipurposeIOMode:
        ...


class Polarity:
    POLARITY_ACTIVE_HIGH: ClassVar[Polarity]
    POLARITY_ACTIVE_LOW: ClassVar[Polarity]

    __members__: ClassVar[Dict[str, Polarity]]
    values: ClassVar[Iterator[Polarity]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> Polarity:
        ...


class FullScaleRange:
    FSR_NORMAL: ClassVar[FullScaleRange]
    FSR_EXTENDED: ClassVar[FullScaleRange]

    __members__: ClassVar[Dict[str, FullScaleRange]]
    values: ClassVar[Iterator[FullScaleRange]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> FullScaleRange:
        ...


class ReturnOrder:
    ORDER_STRONGEST_TO_WEAKEST: ClassVar[ReturnOrder]
    ORDER_FARTHEST_TO_NEAREST: ClassVar[ReturnOrder]
    ORDER_NEAREST_TO_FARTHEST: ClassVar[ReturnOrder]

    __members__: ClassVar[Dict[str, ReturnOrder]]
    values: ClassVar[Iterator[ReturnOrder]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> ReturnOrder:
        ...


class NMEABaudRate:
    BAUD_9600: ClassVar[NMEABaudRate]
    BAUD_115200: ClassVar[NMEABaudRate]

    __members__: ClassVar[Dict[str, NMEABaudRate]]
    values: ClassVar[Iterator[NMEABaudRate]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> NMEABaudRate:
        ...


class UDPProfileLidar:
    PROFILE_LIDAR_LEGACY: ClassVar[UDPProfileLidar]
    PROFILE_LIDAR_RNG19_RFL8_SIG16_NIR16_DUAL: ClassVar[UDPProfileLidar]
    PROFILE_LIDAR_RNG19_RFL8_SIG16_NIR16: ClassVar[UDPProfileLidar]
    PROFILE_LIDAR_RNG15_RFL8_NIR8: ClassVar[UDPProfileLidar]
    PROFILE_LIDAR_FIVE_WORD_PIXEL: ClassVar[UDPProfileLidar]
    PROFILE_LIDAR_FUSA_RNG15_RFL8_NIR8_DUAL: ClassVar[UDPProfileLidar]

    __members__: ClassVar[Dict[str, UDPProfileLidar]]
    values: ClassVar[Iterator[UDPProfileLidar]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> UDPProfileLidar:
        ...


class UDPProfileIMU:
    PROFILE_IMU_LEGACY: ClassVar[UDPProfileIMU]

    __members__: ClassVar[Dict[str, UDPProfileIMU]]
    values: ClassVar[Iterator[UDPProfileIMU]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> UDPProfileIMU:
        ...


class ShotLimitingStatus:
    SHOT_LIMITING_NORMAL: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_IMMINENT: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_0_10: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_10_20: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_20_30: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_30_40: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_40_50: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_50_60: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_60_70: ClassVar[ShotLimitingStatus]
    SHOT_LIMITING_REDUCTION_70_75: ClassVar[ShotLimitingStatus]

    __members__: ClassVar[Dict[str, ShotLimitingStatus]]
    values: ClassVar[Iterator[ShotLimitingStatus]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> ShotLimitingStatus:
        ...


class ThermalShutdownStatus:
    THERMAL_SHUTDOWN_NORMAL: ClassVar[ThermalShutdownStatus]
    THERMAL_SHUTDOWN_IMMINENT: ClassVar[ThermalShutdownStatus]

    __members__: ClassVar[Dict[str, ThermalShutdownStatus]]
    values: ClassVar[Iterator[ThermalShutdownStatus]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> ThermalShutdownStatus:
        ...


class SensorCalibration:
    reflectivity_status: Optional[bool]
    reflectivity_timestamp: Optional[str]


class SensorConfig:
    udp_dest: Optional[str]
    udp_port_lidar: Optional[int]
    udp_port_imu: Optional[int]
    timestamp_mode: Optional[TimestampMode]
    lidar_mode: Optional[LidarMode]
    operating_mode: Optional[OperatingMode]
    multipurpose_io_mode: Optional[MultipurposeIOMode]
    azimuth_window: Optional[tuple]
    signal_multiplier: Optional[float]
    sync_pulse_out_angle: Optional[int]
    sync_pulse_out_pulse_width: Optional[int]
    nmea_in_polarity: Optional[Polarity]
    nmea_baud_rate: Optional[NMEABaudRate]
    nmea_ignore_valid_char: Optional[bool]
    nmea_leap_seconds: Optional[int]
    sync_pulse_in_polarity: Optional[Polarity]
    sync_pulse_out_polarity: Optional[Polarity]
    sync_pulse_out_frequency: Optional[int]
    phase_lock_enable: Optional[bool]
    phase_lock_offset: Optional[int]
    columns_per_packet: Optional[int]
    udp_profile_lidar: Optional[UDPProfileLidar]
    udp_profile_imu: Optional[UDPProfileIMU]
    min_range_threshold_cm: Optional[int]
    gyro_fsr: Optional[FullScaleRange]
    accel_fsr: Optional[FullScaleRange]
    return_order: Optional[ReturnOrder]

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, config_string: str) -> None:
        ...


class FieldClass:
    PIXEL_FIELD: ClassVar[FieldClass]
    COLUMN_FIELD: ClassVar[FieldClass]
    PACKET_FIELD: ClassVar[FieldClass]
    SCAN_FIELD: ClassVar[FieldClass]

    __members__: ClassVar[Dict[str, FieldClass]]
    values: ClassVar[Iterator[FieldClass]]

    def __init__(self, code: int) -> None:
        ...

    def __int__(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> int:
        ...

    @classmethod
    def from_string(cls, s: str) -> FieldClass:
        ...


def init_logger(log_level: str,
                log_file_path: str = ...,
                rotating: bool = ...,
                max_size_in_bytes: int = ...,
                max_files: int = ...) -> bool:
    ...


def set_config(hostname: str,
               config: SensorConfig,
               persist: bool = ...,
               udp_dest_auto: bool = ...,
               force_reinit: bool = ...) -> None:
    ...


def get_config(hostname: str, active: bool = ...) -> SensorConfig:
    ...


class Sensor:
    def __init__(self, hostname: str, desired_config: SensorConfig = ...) -> None:
        ...

    def hostname(self) -> str:
        ...

    def desired_config(self) -> SensorConfig:
        ...

    def http_client(self) -> SensorHttp:
        ...

    def fetch_metadata(self, timeout: int = ...) -> SensorInfo:
        ...


class SensorClient:
    @overload
    def __init__(self, sensors: List[Sensor], config_timeout: float = ..., buffer_time: float = ...) -> None:
        ...

    @overload
    def __init__(self, sensors: List[Sensor], metadata: List[SensorInfo], config_timeout: float = ..., buffer_time: float = ...) -> None:
        ...

    def close(self) -> None:
        ...

    def flush(self) -> None:
        ...

    def buffer_size(self) -> int:
        ...

    def dropped_packets(self) -> int:
        ...

    def get_sensor_info(self) -> List[SensorInfo]:
        ...

    def get_packet(self, lp: LidarPacket, ip: ImuPacket, timeout: float = ...) -> ClientEvent:
        ...


class SensorScanSource:
    @overload
    def __init__(self, sensors: List[Sensor], config_timeout: float = ..., queue_size: int = ..., soft_id_check: bool = ...) -> None:
        ...

    @overload
    def __init__(self, sensors: List[Sensor], infos: List[SensorInfo], config_timeout: float = ..., queue_size: int = ..., soft_id_check: bool = ...) -> None:
        ...

    @overload
    def __init__(self, sensors: List[Sensor], infos: List[SensorInfo], fields: List[List[FieldType]], config_timeout: float = ..., queue_size: int = ..., soft_id_check: bool = ...) -> None:
        ...

    def get_sensor_info(self) -> List[SensorInfo]:
        ...

    def get_scan(self, timeout_sec: float = ...) -> LidarScan:
        ...

    def id_error_count(self) -> int:
        ...

    def dropped_scans(self) -> int:
        ...

    def close(self) -> None:
        ...

    def flush(self) -> None:
        ...


class Version:
    major: int
    minor: int
    patch: int
    stage: str
    machine: str
    prerelease: str
    build: str

    def __init__(self) -> None:
        ...

    def __le__(self, v: Version) -> bool:
        ...

    def __lt__(self, v: Version) -> bool:
        ...

    @classmethod
    def from_string(cls, s: str) -> Version:
        ...


class FieldType:
    name: str
    element_type: Any
    extra_dims: Tuple[int, ...]
    field_class: FieldClass

    def __init__(self, name: str, dtype: Any, extra_dims: Tuple[int, ...] = (), field_class: FieldClass = FieldClass.PIXEL_FIELD):
        ...


class LidarScan:

    frame_id: int
    frame_status: int  # contains both shutdown and shot limiting status bits
    shutdown_countdown: int
    shot_limiting_countdown: int

    @overload
    def __init__(self, h: int, w: int) -> None:
        ...

    @overload
    def __init__(self, h: int, w: int, profile: UDPProfileLidar) -> None:
        ...

    @overload
    def __init__(self, h: int, w: int, profile: UDPProfileLidar, columns_per_packet: int) -> None:
        ...

    @overload
    def __init__(self, h: int, w: int, fields: List[FieldType], columns_per_packet: int = ...) -> None:
        ...

    @overload
    def __init__(self, scan: LidarScan) -> None:
        ...

    @overload
    def __init__(self, scan: LidarScan, fields: List[FieldType]) -> None:
        ...

    @property
    def w(self) -> int:
        ...

    @property
    def h(self) -> int:
        ...

    def thermal_shutdown(self) -> int:
        ...

    def shot_limiting(self) -> int:
        ...

    @property
    def packet_timestamp(self) -> ndarray:
        ...

    @property
    def alert_flags(self) -> ndarray:
        ...

    @overload
    def field(self, field: str) -> ndarray:
        ...

    @overload
    def field(self, name: str) -> ndarray:
        ...

    @property
    def field_types(self) -> List[FieldType]:
        ...
        
    @overload
    def add_field(self, field_type: FieldType) -> ndarray:
        ...

    @overload
    def add_field(self, name: str, array: ndarray, field_class: FieldClass = ...) -> ndarray:
        ...

    @overload
    def add_field(self, name: str, dtype: FieldDType, shape: Tuple[int, ...], field_class: FieldClass = ...) -> ndarray:
        ...

    def del_field(self, name: str) -> ndarray:
        ...

    def field_class(self, name: str) -> FieldClass:
        ...

    def has_field(self, name: str) -> bool:
        ...

    @property
    def timestamp(self) -> ndarray:
        ...

    @property
    def measurement_id(self) -> ndarray:
        ...

    @property
    def status(self) -> ndarray:
        ...

    @property
    def pose(self) -> ndarray:
        ...

    def complete(self, window: Optional[Tuple[int, int]] = ...) -> bool:
        ...

    @property
    def packet_count(self) -> int:
        ...

    @property
    def fields(self) -> Iterator[str]:
        ...

    def get_first_valid_packet_timestamp(self) -> int:
        ...

    def get_first_valid_column_timestamp(self) -> int:
        ...


def destagger_int8(field: ndarray, shifts: List[int],
                   inverse: bool) -> ndarray:
    ...


def destagger_int16(field: ndarray, shifts: List[int],
                    inverse: bool) -> ndarray:
    ...


def destagger_int32(field: ndarray, shifts: List[int],
                    inverse: bool) -> ndarray:
    ...


def destagger_int64(field: ndarray, shifts: List[int],
                    inverse: bool) -> ndarray:
    ...


def destagger_uint8(field: ndarray, shifts: List[int],
                    inverse: bool) -> ndarray:
    ...


def destagger_uint16(field: ndarray, shifts: List[int],
                     inverse: bool) -> ndarray:
    ...


def destagger_uint32(field: ndarray, shifts: List[int],
                     inverse: bool) -> ndarray:
    ...


def destagger_uint64(field: ndarray, shifts: List[int],
                     inverse: bool) -> ndarray:
    ...


def destagger_float(field: ndarray, shifts: List[int],
                    inverse: bool) -> ndarray:
    ...


def destagger_double(field: ndarray, shifts: List[int],
                     inverse: bool) -> ndarray:
    ...


class ScanBatcher:
    @overload
    def __init__(self, w: int, pf: PacketFormat) -> None:
        ...

    @overload
    def __init__(self, info: SensorInfo) -> None:
        ...

    @overload
    def __call__(self, buf: BufferT, ls: LidarScan) -> bool:
        ...

    @overload
    def __call__(self, buf: BufferT, packet_ts: int, ls: LidarScan) -> bool:
        ...

    @overload
    def __call__(self, packet: LidarPacket, ls: LidarScan) -> bool:
        ...


class XYZLut:
    def __init__(self, info: SensorInfo, use_extrinsics: bool) -> None:
        ...

    @overload
    def __call__(self, scan: LidarScan) -> ndarray:
        ...

    @overload
    def __call__(self, range: ndarray) -> ndarray:
        ...


class AutoExposure:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, lo_percentile: float, hi_percentile: float,
                 update_every: int) -> None:
        ...

    def __call__(self,
                 image: ndarray,
                 update_state: Optional[bool] = True) -> None:
        ...


class BeamUniformityCorrector:
    def __init__(self) -> None:
        ...

    def __call__(self, image: ndarray) -> None:
        ...


class FieldInfo:
    @property
    def ty_tag(self) -> FieldDType:
        ...

    def __init__(self, ty_tag: FieldDType, offset: int, mask: int, shift: int) -> None:
        ...

    offset: int
    mask: int
    shift: int


def add_custom_profile(profile_nr: int,
                       name: str,
                       fields: List[Tuple[str, FieldInfo]],
                       chan_data_size: int) -> None:
    ...


@overload
def get_field_types(info: SensorInfo) -> List[FieldType]: ...


@overload
def get_field_types(udp_profile_lidar: UDPProfileLidar) -> List[FieldType]: ...


class ValidatorEntry:
    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def get_path(self) -> str:
        ...

    def get_msg(self) -> str:
        ...


class ValidatorIssues:
    @property
    def critical(self) -> List[ValidatorEntry]:
        ...

    @property
    def warning(self) -> List[ValidatorEntry]:
        ...

    @property
    def information(self) -> List[ValidatorEntry]:
        ...


def parse_and_validate_metadata(metadata: str) -> Tuple[SensorInfo, ValidatorIssues]:
    ...                         


def dewarp(points: ndarray, poses: ndarray) -> ndarray:
    ...

def transform(points: ndarray, pose: ndarray) -> ndarray:
    ...

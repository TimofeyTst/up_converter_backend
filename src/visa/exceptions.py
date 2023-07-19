from fastapi import status

from src.exceptions import BadRequest, DetailedHTTPException
from src.visa.constants import ErrorCode


class VisaError(DetailedHTTPException):
    DETAIL = ErrorCode.VISA_ERROR


class ConnectError(BadRequest):
    DETAIL = ErrorCode.DEVICE_PORT_NOT_EXIST


class SANotExistError(BadRequest):
    DETAIL = ErrorCode.SA_NOT_EXIST_ERROR


class ManySADevicesError(BadRequest):
    DETAIL = ErrorCode.MANY_SA_DEVICES_ERROR


class ConnectedToSAError(BadRequest):
    DETAIL = ErrorCode.CONNECTED_TO_SA_ERROR


class InvalidConncetionError(BadRequest):
    DETAIL = ErrorCode.INVALID_CONNECTION_ERROR


class StateChangeError(BadRequest):
    DETAIL = ErrorCode.STATE_CHANGE_ERROR


class InvalidDeviceNameError(BadRequest):
    DETAIL = ErrorCode.INVALID_DEVICE_NAME_ERROR


class InvalidDeviceModelError(BadRequest):
    DETAIL = ErrorCode.INVALID_DEVICE_MODEL_ERROR


class CalModelSmdvaError(BadRequest):
    DETAIL = ErrorCode.CAL_MODEL_SMDVA_ERROR


class InvalidSerialNumberError(BadRequest):
    def __init__(self, device_name):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = ErrorCode.INVALID_SERIAL_NUMBER + " " + device_name


class UnknownError(DetailedHTTPException):
    DETAIL = ErrorCode.UNKNOWN_ERROR

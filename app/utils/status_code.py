from starlette import status


class ResponseSuccess:
    code = status.HTTP_200_OK
    message = "操作成功"


class ResponseError:
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "操作失败"


class ResponseUserNotExist(ResponseError):
    code = status.HTTP_404_NOT_FOUND
    message = "用户不存在"


class ResponseException(ResponseError):
    code = status.HTTP_400_BAD_REQUEST
    message = "操作异常"


class ResponseUnauthorized(ResponseError):
    code = status.HTTP_401_UNAUTHORIZED
    message = "未授权"


class ResponseForbidden(ResponseError):
    code = status.HTTP_403_FORBIDDEN
    message = "禁止访问"


class ResponseNotFound(ResponseError):
    code = status.HTTP_404_NOT_FOUND
    message = "资源未找到"


class ResponseConflict(ResponseError):
    code = status.HTTP_409_CONFLICT
    message = "资源冲突"


class ResponseGone(ResponseError):
    code = status.HTTP_410_GONE
    message = "资源已删除"


class ResponseUnprocessable(ResponseError):
    code = status.HTTP_422_UNPROCESSABLE_ENTITY
    message = "请求格式错误"


class ResponseTooManyRequests(ResponseError):
    code = status.HTTP_429_TOO_MANY_REQUESTS
    message = "请求过于频繁"


class ResponseInternalServerError(ResponseError):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "服务器内部错误"


class ResponseNotImplemented(ResponseError):
    code = status.HTTP_501_NOT_IMPLEMENTED
    message = "未实现"


class ResponseServiceUnavailable(ResponseError):
    code = status.HTTP_503_SERVICE_UNAVAILABLE
    message = "服务不可用"

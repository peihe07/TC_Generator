"""Tool layer 的自訂例外。

Tool 不丟 HTTPException；route 層負責把 ToolError 翻譯成 HTTP status。
"""

from __future__ import annotations


class ToolError(Exception):
    """Tool 執行失敗的通用例外。

    Attributes:
        message: 給使用者看的訊息
        code: 對應的錯誤代碼，用於 HTTP status 對照（預設 "bad_request"）
        details: 可選的附加資訊，會序列化到 API response
    """

    # 錯誤代碼到 HTTP status code 的對照表，route 層用
    HTTP_STATUS_MAP = {
        "bad_request": 400,
        "not_found": 404,
        "conflict": 409,
        "payload_too_large": 413,
        "unprocessable": 422,
        "budget_exceeded": 402,
        "internal": 500,
    }

    def __init__(
        self,
        message: str,
        *,
        code: str = "bad_request",
        details: dict | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    @property
    def http_status(self) -> int:
        return self.HTTP_STATUS_MAP.get(self.code, 400)

    def to_dict(self) -> dict:
        return {
            "error": self.code,
            "message": self.message,
            "details": self.details,
        }

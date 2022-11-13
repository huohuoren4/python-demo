import win32clipboard


class WinClass:
    def __init__(self) -> None:
        super().__init__()

    def get_paste(self):
        """获取复制的内容"""
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data

    def set_paste(self, data):
        """设置粘贴板的内容"""
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(data)
        win32clipboard.CloseClipboard()


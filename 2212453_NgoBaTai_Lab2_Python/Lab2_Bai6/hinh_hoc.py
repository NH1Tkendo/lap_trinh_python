class HinhHoc:
    def __init__(self, canh: float):
        self.canh = canh

    def tinhDienTich(self) -> float:
        return self.canh

    def __str__(self) -> None:
        return f"Diện tích của hình "
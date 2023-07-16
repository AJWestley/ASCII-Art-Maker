import cv2
import os


class ASCII_Artwork:
    def __init__(self) -> None:
        self.image = []
        self.ascii_image = []

    def import_adjust(
        self, path: str, ideal_width: int = 100, height_scale_factor: float = 0.6
    ):
        # import image, then greyscale and resize
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        scale_factor = ideal_width / img.shape[1]
        scaled_dimensions = (
            int(img.shape[1] * scale_factor),
            int(img.shape[0] * scale_factor * height_scale_factor),
        )

        self.image = cv2.resize(img, scaled_dimensions, interpolation=cv2.INTER_AREA)

    def translate(self, inv: bool = False):
        self.ascii_image = []
        for row in self.image:
            ascii_row = [ASCII_Artwork.pixel_to_ascii(pixel, inv) for pixel in row]
            self.ascii_image.append(ascii_row)

    def to_string(self):
        array_1D = []
        for row in self.ascii_image:
            array_1D.extend(iter(row))
            array_1D.append("\n")
        return "".join(array_1D)

    def print_ascii(self):
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print(self.to_string())

    @staticmethod
    def pixel_to_ascii(pixel_val: int, inv: bool = False) -> str:
        ascii_vals = ["%", "#", "+", "*", "=", "-", ":", ".", " "]

        # formula to get an ascii index from a pixel value
        # 0->25 = index 0 then index goes up every 30
        # if inv = true, the index is reversed
        pixel_val += 4
        i = 8 - pixel_val // 30 if inv else pixel_val // 30

        return ascii_vals[i]


if __name__ == "__main__":
    path = input("Enter image path: ")
    size = int(input("Enter desired image width: "))
    image = ASCII_Artwork()
    image.import_adjust(path, size)
    image.translate()
    image.print_ascii()

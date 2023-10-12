import cv2

def read_rgb(image, x, y):
  """Membaca nilai RGB dari pixel di titik tertentu pada citra.

  Args:
    image: Citra bitmap.
    x: Koordinat x pixel.
    y: Koordinat y pixel.

  Returns:
    Nilai RGB pixel.
  """

  # Membaca nilai pixel.
  pixel = image[y, x]

  # Mengubah nilai pixel ke nilai RGB.
  r = pixel[2]
  g = pixel[1]
  b = pixel[0]

  return r, g, b

def write_rgb(image, x, y, r, g, b):
  """Menulis nilai RGB tertentu ke sebuah titik pada citra cover image.

  Args:
    image: Citra bitmap.
    x: Koordinat x pixel.
    y: Koordinat y pixel.
    r: Nilai R pixel.
    g: Nilai G pixel.
    b: Nilai B pixel.
  """

  # Mengubah nilai RGB ke nilai pixel.
  pixel = [b, g, r]

  # Menulis nilai pixel ke citra.
  image[y, x] = pixel

if __name__ == "__main__":
  # Membaca citra cover image.
  image = cv2.imread("../Downloads/bunga.bmp")

  # Membaca nilai RGB dari pixel di titik tertentu.
  x = 100
  y = 200
  r, g, b = read_rgb(image, x, y)
  print("Nilai RGB pixel di titik (%d, %d) adalah (%d, %d, %d)" % (x, y, r, g, b))

  # Menuliskan nilai RGB tertentu ke titik pada citra cover image.
  r = 0
  g = 255
  b = 0
  write_rgb(image, x, y, r, g, b)

  # Menyimpan citra cover image yang telah diedit.
  cv2.imwrite("cover_image_edited.jpg", image)
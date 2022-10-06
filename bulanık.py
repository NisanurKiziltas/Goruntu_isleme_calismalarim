from random import gauss
import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

#blurring (detayı azaltır, gürültüyü engeller)
img = cv2.imread("manzara.jpg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal")

"""
ORTALAMA BULANIKLAŞTIRMA YÖNTEMİ
bir resmi bulanıklaştırmk için üzerinden filtre geçiyor.
"""
dst2 = cv2.blur(img, ksize= (3,3))
plt.figure(), plt.imshow(dst2),plt.axis("off"),plt.title("ortalama blur")

"""
Gaussian blur
sigma değerleri ile bulanıklaştırma
"""
gb = cv2.GaussianBlur(img, ksize=(3,3),sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gaussian")

"""
MEDYAN BLURR
"""
mb = cv2.medianBlur(img, ksize=3)
plt.figure(), plt.imshow(mb),plt.axis("off"), plt.title("median blur")

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss

    return noisy

#içe aktar normalize et
img = cv2.imread("manzara.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal")

gaussianNoiseImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoiseImage),plt.axis("off"),plt.title("gaussianNoiseImage")






plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
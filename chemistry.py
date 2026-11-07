from math import pow
from math import floor
from math import log10
from constants import c
# For all calculations rounding to 3 significant figures will be the stanard
def significant_figure(x):
  return round(x, 2-int(floor(log10(abs(x)))))

def wavelength(freq):
    return significant_figure(c / freq)


def frequency(wav):
   return significant_figure(c / wav)

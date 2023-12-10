from search import UndirectedGraph

# Define the map and its locations
map_greedy = UndirectedGraph(dict(
  BandaAceh = dict(Medan = 76.44),
  Medan = dict(BandaAceh = 76.44, Pekanbaru = 83.13, Padang = 100.00),
  Padang = dict(Medan = 100.00, Pekanbaru = 27.25, Jambi = 62.19, Bengkulu = 65.18),
  Pekanbaru = dict(Medan = 83.13, Padang = 27.25, Jambi = 56.64),
  TanjungPinang = dict(PangkalPinang = 67.02),
  Jambi = dict(Pekanbaru = 56.64, Padang = 62.19, Palembang = 27.50, Bengkulu = 45.76),
  Bengkulu = dict(Padang = 65.18, Jambi = 45.76, Palembang = 47.48, BandarLampung = 65.92),
  Palembang = dict(Jambi = 27.50, PangkalPinang = 22.57, Bengkulu = 47.48, BandarLampung = 44.64),
  BandarLampung = dict(Palembang = 44.64, Bengkulu = 65.92, Serang = 11.36),
  PangkalPinang = dict(TanjungPinang = 67.02, Palembang = 22.57),
  Serang = dict(BandarLampung = 11.36, Jakarta = 1.00),
  Jakarta = dict(Serang = 1.00, Bandung = 10.48),
  Bandung = dict(Jakarta = 10.48, Semarang = 51.25, Yogyakarta = 52.81),
  Semarang = dict(Bandung = 51.25, Yogyakarta = 3.92, Surabaya = 39.70),
  Yogyakarta = dict(Bandung = 52.81, Semarang = 3.92, Surabaya = 42.36),
  Surabaya = dict(Semarang = 39.70, Yogyakarta = 42.36)
  ))

map_astar = UndirectedGraph(dict(
  BandaAceh = dict(Medan = 47.43),
  Medan = dict(BandaAceh = 47.43, Pekanbaru = 54.05, Padang = 79.35),
  Padang = dict(Medan = 79.35, Pekanbaru = 26.77, Jambi = 53.50, Bengkulu = 51.45),
  Pekanbaru = dict(Medan = 54.05, Padang = 26.77, Jambi = 40.25),
  TanjungPinang = dict(PangkalPinang = 100.00),
  Jambi = dict(Pekanbaru = 40.25, Padang = 53.50, Palembang = 22.75, Bengkulu = 41.04),
  Bengkulu = dict(Padang = 51.45, Jambi = 41.04, Palembang = 40.96, BandarLampung = 60.67),
  Palembang = dict(Jambi = 22.75, PangkalPinang = 29.14, Bengkulu = 40.96, BandarLampung = 15.74),
  BandarLampung = dict(Palembang = 15.74, Bengkulu = 60.67, Serang = 8.33),
  PangkalPinang = dict(TanjungPinang = 100.00, Palembang = 29.14),
  Serang = dict(BandarLampung = 8.33, Jakarta = 1.00),
  Jakarta = dict(Serang = 1.00, Bandung = 4.39),
  Bandung = dict(Jakarta = 4.39, Semarang = 15.66, Yogyakarta = 32.53),
  Semarang = dict( Bandung = 15.66, Yogyakarta = 3.84, Surabaya = 13.30),
  Yogyakarta = dict(Bandung = 32.53, Semarang = 3.84, Surabaya = 14.32),
  Surabaya = dict(Semarang = 13.30, Yogyakarta = 14.32)
  ))

map_astar.locations = dict(
    BandaAceh = (5.548256326794867, 95.32375203957695),
    Medan = (3.595191911928496, 98.67222196112931),
    Palembang = (-2.9760750389921697, 104.7754307504188),
    Padang = (-0.9470848568696755, 100.417183356826),
    Bengkulu = (-3.7928444639239927, 102.26076463040094),
    Pekanbaru = (0.5070613092125984, 101.44777749360388),
    TanjungPinang = (0.9185469029856769, 104.46650731024035),
    Jambi = (-1.6101257907018853, 103.61312225472736),
    BandarLampung = (-5.447879783268549, 105.2652870845391),
    PangkalPinang = (-2.1316287170897232, 106.11692924995657),
    Serang = (-6.116933092322672, 106.15385208445778),
    Jakarta = (-6.194451015875306, 106.82292091205278),
    Bandung = (-6.917467204609942, 107.61912582176764),
    Semarang = (-7.005147994398289, 110.43812581525368),
    Yogyakarta = (-7.795582204419959, 110.3694911043283),
    Surabaya = (-7.257473307124247, 112.75208772044523),
)

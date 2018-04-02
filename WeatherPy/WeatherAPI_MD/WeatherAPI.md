

```python
# Dependencies
import json
import requests
import pandas as pd
from config import api_key
import random 
import matplotlib.pyplot as plt
from citipy import citipy
import urllib
```


```python
cities_csv = "worldcities.csv"
cities_df = pd.read_csv(cities_csv)
# cities_df = pd.cities_df1['Latitude']['Longitude']
cities_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ad</td>
      <td>andorra la vella</td>
      <td>42.500000</td>
      <td>1.516667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ad</td>
      <td>canillo</td>
      <td>42.566667</td>
      <td>1.600000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ad</td>
      <td>encamp</td>
      <td>42.533333</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ad</td>
      <td>la massana</td>
      <td>42.550000</td>
      <td>1.516667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ad</td>
      <td>les escaldes</td>
      <td>42.500000</td>
      <td>1.533333</td>
    </tr>
  </tbody>
</table>
</div>




```python
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"

city_list =[]
lat_random = []
lon_random = []
query_url = []
for i in range(1000):
    lat_random.append(random.choice(cities_df['Latitude']))
    lon_random.append(random.choice(cities_df['Longitude']))
    citiname = citipy.nearest_city(float(lat_random[i]), float(lon_random[i])).city_name
    if citiname not in city_list:
        city_list.append(citiname)

```


```python
len(city_list)
# print(name)
# print(query_url)
```




    810




```python
temp = []
humidity = []
cloud = []
wind = []
lat = []
lon = []
country = []
date = []
maxtemp = []
city_name =[]


for i, city in enumerate(city_list):
    query_url = url +"&appid=" + api_key + "&q=" + urllib.request.pathname2url(city)
#     print(query_url)
    try:
        response = requests.get(query_url).json()
        city_name.append(response['name'])
        temp.append(response['main']['temp'])
        humidity.append(response['main']['humidity'])
        cloud.append(response['clouds']['all'])
        lat.append(response['coord']['lat'])
        lon.append(response['coord']['lon'])
        wind.append(response['wind']['speed'])
        country.append(response['sys']['country'])
        date.append(response['dt'])
        maxtemp.append(response['main']['temp_max'])
        print(f"Processing Record for {city}")
    except:
        print(f"{city} Not found")
        pass


```

    Processing Record for serafimovich
    Processing Record for saint george
    Processing Record for ati
    yian Not found
    jiddah Not found
    Processing Record for minervino murge
    Processing Record for tahoua
    Processing Record for puerto cabezas
    Processing Record for yaan
    Processing Record for severo-kurilsk
    Processing Record for lepaterique
    Processing Record for midland
    Processing Record for san cristobal
    Processing Record for ozinki
    Processing Record for cockburn town
    Processing Record for jitotol
    Processing Record for grindavik
    Processing Record for hopfgarten
    Processing Record for pozorice
    Processing Record for sao filipe
    Processing Record for tekeli
    lushunkou Not found
    Processing Record for tutoia
    Processing Record for madimba
    Processing Record for fort frances
    Processing Record for georgetown
    Processing Record for thetford mines
    Processing Record for touba
    Processing Record for bodden town
    Processing Record for saryozek
    Processing Record for general roca
    Processing Record for zaysan
    Processing Record for taoudenni
    Processing Record for cabo san lucas
    Processing Record for ribeira grande
    Processing Record for port hedland
    Processing Record for marzuq
    Processing Record for nordborg
    Processing Record for adancata
    Processing Record for gura sutii
    Processing Record for porto recanati
    Processing Record for nurota
    Processing Record for barillas
    Processing Record for sinnamary
    Processing Record for ronne
    Processing Record for topola
    Processing Record for horoatu crasnei
    Processing Record for jalu
    Processing Record for tekirdag
    Processing Record for carbonia
    Processing Record for lysychovo
    Processing Record for baruun-urt
    Processing Record for cheyenne
    Processing Record for truro
    Processing Record for chapais
    Processing Record for bulawayo
    Processing Record for ustka
    Processing Record for camabatela
    Processing Record for jaszkarajeno
    Processing Record for zalantun
    Processing Record for ofaqim
    Processing Record for puerto ayora
    Processing Record for gien
    Processing Record for adrano
    Processing Record for bremervorde
    Processing Record for serebryansk
    attawapiskat Not found
    Processing Record for dmytrivka
    Processing Record for namibe
    Processing Record for ust-koksa
    Processing Record for garden city
    Processing Record for mao
    Processing Record for guaymas
    Processing Record for limenaria
    mericleri Not found
    marcona Not found
    Processing Record for puerto leguizamo
    Processing Record for tabas
    Processing Record for rebricea
    juifang Not found
    Processing Record for hobyo
    Processing Record for saint anthony
    Processing Record for guerrero negro
    Processing Record for sangar
    Processing Record for aksu
    Processing Record for lodja
    Processing Record for dekar
    Processing Record for bilma
    Processing Record for bull savanna
    Processing Record for calatayud
    Processing Record for kalabo
    Processing Record for muros
    Processing Record for beeskow
    Processing Record for banswada
    Processing Record for clonakilty
    Processing Record for sesvete
    Processing Record for kutum
    Processing Record for fuyu
    Processing Record for san jose
    Processing Record for luba
    Processing Record for gorokhovets
    yenisea Not found
    Processing Record for shelbyville
    Processing Record for tallahassee
    Processing Record for havelock
    raga Not found
    Processing Record for kaele
    Processing Record for jasper
    Processing Record for bathsheba
    Processing Record for hearst
    Processing Record for jamestown
    Processing Record for guarapari
    Processing Record for nelson
    Processing Record for orange
    Processing Record for torbay
    Processing Record for verkhnevilyuysk
    Processing Record for porto torres
    Processing Record for kulevcha
    Processing Record for morar
    Processing Record for lock haven
    Processing Record for cayenne
    Processing Record for sharjah
    Processing Record for mahon
    Processing Record for rantepao
    Processing Record for batticaloa
    Processing Record for puerto colombia
    Processing Record for atar
    tsihombe Not found
    Processing Record for tongliao
    Processing Record for tarut
    Processing Record for privas
    chagda Not found
    Processing Record for altamura
    uwayl Not found
    Processing Record for opuwo
    Processing Record for djambala
    Processing Record for moravsky beroun
    Processing Record for miraflores
    Processing Record for felanitx
    Processing Record for ponta do sol
    Processing Record for fort oglethorpe
    Processing Record for luderitz
    Processing Record for fjerritslev
    dibaya Not found
    Processing Record for chaman
    bargal Not found
    Processing Record for iqaluit
    Processing Record for erenhot
    Processing Record for stephenville
    Processing Record for calabar
    Processing Record for galesong
    Processing Record for petervasara
    Processing Record for bumba
    Processing Record for kendari
    Processing Record for ife
    Processing Record for dourbali
    Processing Record for lakinsk
    Processing Record for ranghulu
    Processing Record for surt
    Processing Record for aksay
    Processing Record for goure
    atlantic city Not found
    Processing Record for concarneau
    Processing Record for jhargram
    Processing Record for mishelevka
    Processing Record for strezhevoy
    Processing Record for toora-khem
    Processing Record for mundargi
    Processing Record for laramie
    Processing Record for cantapoy
    Processing Record for bol
    Processing Record for dafeng
    urdzhar Not found
    Processing Record for nalvo
    Processing Record for afyonkarahisar
    Processing Record for saldanha
    boljarovo Not found
    Processing Record for araouane
    Processing Record for nador
    Processing Record for pittsburg
    Processing Record for coro
    Processing Record for mecca
    Processing Record for shahreza
    Processing Record for celestun
    Processing Record for hare bay
    Processing Record for pyskowice
    Processing Record for zlynka
    Processing Record for asyut
    Processing Record for omboue
    Processing Record for pula
    Processing Record for lisakovsk
    Processing Record for stolin
    Processing Record for new norfolk
    Processing Record for briancon
    Processing Record for lang suan
    Processing Record for mitchell
    Processing Record for kantang
    Processing Record for stralsund
    Processing Record for ayagoz
    Processing Record for cavarzere
    Processing Record for jinji
    Processing Record for zabid
    Processing Record for biltine
    Processing Record for korem
    Processing Record for kidal
    Processing Record for el campo
    Processing Record for dengzhou
    Processing Record for winnemucca
    Processing Record for pisco
    Processing Record for sabzevar
    Processing Record for kars
    Processing Record for kungurtug
    Processing Record for alexandroupoli
    Processing Record for jijiga
    Processing Record for spas
    Processing Record for yerofey pavlovich
    Processing Record for hof
    Processing Record for riyadh
    Processing Record for gongzhuling
    Processing Record for korablino
    Processing Record for viisoara
    Processing Record for alta floresta
    grand river south east Not found
    Processing Record for puertollano
    Processing Record for hirara
    Processing Record for figeac
    Processing Record for orlik
    Processing Record for murrhardt
    Processing Record for qingdao
    bafra Not found
    Processing Record for jiutai
    campineanca Not found
    Processing Record for ninghai
    Processing Record for walvis bay
    Processing Record for jiazi
    lolua Not found
    Processing Record for numata
    cockburn harbour Not found
    Processing Record for semey
    Processing Record for warrington
    Processing Record for fleetwood
    Processing Record for kerteminde
    Processing Record for salalah
    Processing Record for voljevac
    Processing Record for platanos
    Processing Record for moussoro
    eratinon Not found
    Processing Record for laiyang
    Processing Record for challakere
    Processing Record for tessalit
    Processing Record for fez
    Processing Record for birao
    Processing Record for ancud
    Processing Record for nantucket
    Processing Record for moose factory
    Processing Record for longkou
    Processing Record for khunzakh
    Processing Record for chunhuhub
    Processing Record for takab
    khowst Not found
    Processing Record for muscle shoals
    Processing Record for barth
    Processing Record for paralimni
    Processing Record for dutse
    Processing Record for tarquinia
    Processing Record for masloc
    Processing Record for teufen
    Processing Record for botou
    Processing Record for montbrison
    Processing Record for indian head
    Processing Record for oytal
    Processing Record for davila
    Processing Record for buracan
    Processing Record for banyo
    Processing Record for tuscaloosa
    Processing Record for west bay
    Processing Record for ekibastuz
    Processing Record for baltimore
    Processing Record for vernon
    Processing Record for gimli
    Processing Record for boras
    Processing Record for champerico
    kousseri Not found
    Processing Record for zhuanghe
    Processing Record for gamba
    Processing Record for zemio
    Processing Record for dospat
    Processing Record for pitsunda
    Processing Record for fort morgan
    Processing Record for khani
    Processing Record for bandarbeyla
    Processing Record for nikolskoye
    Processing Record for constitucion
    Processing Record for rionero in vulture
    Processing Record for oume
    Processing Record for west wendover
    Processing Record for khilok
    Processing Record for hueyotlipan
    talah Not found
    Processing Record for kastrakion
    Processing Record for arlit
    Processing Record for methoni
    Processing Record for husasau de tinca
    Processing Record for bad ischl
    Processing Record for nishihara
    Processing Record for ouadda
    Processing Record for porto san giorgio
    Processing Record for rutana
    Processing Record for los algarrobos
    Processing Record for strausberg
    Processing Record for sankt veit
    Processing Record for abnub
    Processing Record for gladenbach
    tulare Not found
    Processing Record for karpathos
    guapota Not found
    Processing Record for weihai
    Processing Record for sarlat-la-caneda
    Processing Record for galesti
    Processing Record for santander
    Processing Record for obeliai
    Processing Record for sargatskoye
    Processing Record for andros town
    Processing Record for chemax
    Processing Record for pochutla
    Processing Record for fasano
    Processing Record for otavi
    Processing Record for butaritari
    Processing Record for krasnomayskiy
    Processing Record for umea
    Processing Record for falmouth
    Processing Record for haghartsin
    Processing Record for brus laguna
    Processing Record for vondrozo
    Processing Record for troyes
    Processing Record for mont-de-marsan
    Processing Record for krk
    Processing Record for jeremie
    la raya de santa maria Not found
    Processing Record for doka
    Processing Record for wadi maliz
    Processing Record for pirgos
    Processing Record for gelibolu
    Processing Record for massakory
    Processing Record for merrill
    chikoy Not found
    Processing Record for kunya
    Processing Record for san vicente
    Processing Record for darnah
    Processing Record for nola
    dubenskiy Not found
    Processing Record for sayville
    Processing Record for denizli
    Processing Record for douglas
    Processing Record for aleksandrov gay
    Processing Record for huntersville
    Processing Record for termoli
    Processing Record for mubi
    Processing Record for wiarton
    Processing Record for aysha
    Processing Record for saint-remi
    Processing Record for adrar
    Processing Record for celendin
    Processing Record for ipswich
    Processing Record for rikitea
    Processing Record for fairhope
    Processing Record for kyzyl-suu
    Processing Record for seoul
    Processing Record for nata
    yirol Not found
    Processing Record for sabang
    Processing Record for kant
    Processing Record for elizabeth city
    Processing Record for morlaix
    buon me thuot Not found
    Processing Record for judenburg
    Processing Record for dickinson
    Processing Record for mbarara
    Processing Record for campo maior
    Processing Record for kielce
    Processing Record for nucet
    Processing Record for sigmaringen
    Processing Record for varhaug
    Processing Record for kokorevka
    Processing Record for svetlaya
    Processing Record for atuona
    Processing Record for aviles
    Processing Record for vrchlabi
    Processing Record for saint-michel-des-saints
    Processing Record for gandajika
    Processing Record for chachapoyas
    Processing Record for liepaja
    Processing Record for madona
    Processing Record for naze
    Processing Record for lompoc
    Processing Record for pindiga
    Processing Record for bakchar
    Processing Record for karatau
    Processing Record for xinmin
    Processing Record for crvenka
    Processing Record for lebedinyy
    Processing Record for xining
    Processing Record for burlington
    Processing Record for genhe
    Processing Record for katsuura
    Processing Record for teya
    Processing Record for karadaglije
    Processing Record for chaumont
    Processing Record for cabra
    Processing Record for winter springs
    Processing Record for jaslo
    Processing Record for thompson
    Processing Record for san patricio
    Processing Record for lazaro cardenas
    Processing Record for henties bay
    Processing Record for amelia
    Processing Record for prunisor
    Processing Record for capissayan
    kashi Not found
    ivajlovgrad Not found
    Processing Record for esso
    Processing Record for lausen
    Processing Record for kaduna
    Processing Record for yarada
    Processing Record for srinivaspur
    Processing Record for pustomyty
    Processing Record for yangambi
    Processing Record for zdzieszowice
    Processing Record for mwene-ditu
    Processing Record for daeni
    Processing Record for agdam
    Processing Record for carnarvon
    umm jarr Not found
    Processing Record for prinos
    Processing Record for brae
    Processing Record for sacelu
    Processing Record for terrace bay
    yunjinghong Not found
    Processing Record for puerto lempira
    Processing Record for hithadhoo
    Processing Record for dandong
    Processing Record for ushumun
    Processing Record for oranjemund
    Processing Record for yatou
    Processing Record for sur
    Processing Record for suraabad
    Processing Record for kuching
    Processing Record for weston
    Processing Record for tecoanapa
    Processing Record for bosanski samac
    Processing Record for dong hoi
    Processing Record for ipixuna
    Processing Record for josefina
    Processing Record for lusambo
    Processing Record for managua
    Processing Record for geraldton
    Processing Record for laguna
    Processing Record for vrangel
    Processing Record for wukari
    Processing Record for krasnyy luch
    Processing Record for najran
    Processing Record for pontarlier
    Processing Record for taxiarkhis
    Processing Record for sadon
    Processing Record for bara
    Processing Record for brigantine
    Processing Record for thunder bay
    Processing Record for noshiro
    Processing Record for warri
    Processing Record for kichera
    wulanhaote Not found
    Processing Record for taksimo
    Processing Record for adela
    achisay Not found
    Processing Record for kearney
    Processing Record for longonjo
    Processing Record for morecambe
    Processing Record for haian
    Processing Record for onguday
    Processing Record for tirat karmel
    Processing Record for korcula
    Processing Record for siauliai
    Processing Record for bredasdorp
    Processing Record for medina del campo
    Processing Record for lopatino
    Processing Record for lublin
    Processing Record for aberdeen
    Processing Record for boralday
    Processing Record for cobh
    Processing Record for jiblah
    Processing Record for mimarsinan
    Processing Record for shihezi
    litoral del san juan Not found
    Processing Record for alihe
    Processing Record for vydrino
    Processing Record for esperance
    Processing Record for kunszentmiklos
    Processing Record for mataura
    Processing Record for san luis
    Processing Record for suleja
    Processing Record for stupino
    Processing Record for rancho palos verdes
    Processing Record for xuddur
    Processing Record for umm kaddadah
    Processing Record for zhezkazgan
    Processing Record for kharian
    Processing Record for jumla
    Processing Record for nanortalik
    wa Not found
    Processing Record for latung
    Processing Record for coaticook
    Processing Record for xiongyue
    Processing Record for augustow
    tambura Not found
    Processing Record for salmon arm
    Processing Record for gumrak
    Processing Record for jiuquan
    Processing Record for idah
    odweyne Not found
    Processing Record for kavaratti
    Processing Record for thornbury
    Processing Record for huanren
    Processing Record for solaro
    Processing Record for tvrdosin
    kalomo Not found
    Processing Record for desesti
    Processing Record for chudniv
    Processing Record for weyburn
    Processing Record for potam
    Processing Record for kalety
    Processing Record for roela
    Processing Record for otanche
    Processing Record for kaduqli
    Processing Record for klyuchi
    yingzhong Not found
    Processing Record for nalut
    Processing Record for marsala
    Processing Record for zbarazh
    Processing Record for nawalgarh
    Processing Record for boissevain
    Processing Record for coatesville
    Processing Record for san andres
    Processing Record for moa
    villazon Not found
    Processing Record for looc
    Processing Record for kabalo
    Processing Record for kotel
    Processing Record for marawi
    Processing Record for fivizzano
    Processing Record for tumsar
    Processing Record for rovinj
    Processing Record for pavlovsk
    Processing Record for kotovo
    Processing Record for emmett
    Processing Record for opatija
    Processing Record for grasse
    Processing Record for disraeli
    Processing Record for faya
    Processing Record for okha
    Processing Record for kincardine
    Processing Record for svarstad
    Processing Record for airai
    Processing Record for ginir
    Processing Record for wajima
    Processing Record for pomabamba
    Processing Record for winterberg
    Processing Record for nanpiao
    warqla Not found
    Processing Record for dunmore town
    Processing Record for hargeysa
    Processing Record for bangao
    Processing Record for pervomayskoye
    Processing Record for great falls
    palaiokhora Not found
    Processing Record for basco
    grande-riviere Not found
    Processing Record for pedernales
    Processing Record for kachiry
    tingrela Not found
    Processing Record for bayan
    Processing Record for lucapa
    Processing Record for atasu
    cah ab Not found
    Processing Record for ergani
    Processing Record for hami
    Processing Record for leh
    Processing Record for remontnoye
    Processing Record for balao
    Processing Record for timmins
    Processing Record for umm lajj
    Processing Record for sechura
    Processing Record for kodiak
    Processing Record for ulagan
    Processing Record for montana
    Processing Record for chicama
    Processing Record for superior
    Processing Record for jimeta
    Processing Record for hamilton
    Processing Record for west fargo
    Processing Record for emba
    Processing Record for bubaque
    Processing Record for palu
    Processing Record for luanda
    Processing Record for sioux lookout
    Processing Record for owo
    Processing Record for edinet
    Processing Record for raudeberg
    Processing Record for sidhi
    karkaralinsk Not found
    yiannitsa Not found
    Processing Record for procida
    Processing Record for kishtwar
    Processing Record for beterou
    Processing Record for roseto degli abruzzi
    Processing Record for zalakomar
    bengkulu Not found
    Processing Record for kermen
    Processing Record for aldan
    Processing Record for port talbot
    Processing Record for matagami
    Processing Record for yakeshi
    Processing Record for constantine
    Processing Record for huty
    Processing Record for manfredonia
    Processing Record for mnogovershinnyy
    Processing Record for nakhon phanom
    Processing Record for resavica
    Processing Record for sterling
    Processing Record for kefalos
    Processing Record for gat
    Processing Record for awbari
    Processing Record for ceska lipa
    Processing Record for beringovskiy
    tuggurt Not found
    Processing Record for balint
    Processing Record for mambajao
    Processing Record for yarmouth
    Processing Record for bolokhovo
    Processing Record for hall
    Processing Record for port elizabeth
    Processing Record for kalmunai
    Processing Record for matara
    Processing Record for worthing
    Processing Record for paita
    Processing Record for brenham
    Processing Record for malayal
    ozgon Not found
    Processing Record for rotterdam
    Processing Record for lebu
    Processing Record for kingston
    Processing Record for bondeno
    kapoeta Not found
    Processing Record for la libertad
    Processing Record for lafiagi
    Processing Record for kamiiso
    Processing Record for tauramena
    Processing Record for morgaushi
    Processing Record for mandalgovi
    Processing Record for borcea
    tsienyane Not found
    Processing Record for tahe
    Processing Record for podu iloaiei
    Processing Record for ixtapa
    Processing Record for tomesti
    Processing Record for keelung
    Processing Record for cracow
    Processing Record for tinyahuarco
    Processing Record for lipari
    Processing Record for donskoye
    Processing Record for tibiao
    Processing Record for asnaes
    Processing Record for pritzwalk
    Processing Record for merritt island
    Processing Record for burdeos
    Processing Record for naxos
    Processing Record for gueret
    Processing Record for deep river
    Processing Record for nizhniy kuranakh
    Processing Record for urkut
    pousat Not found
    Processing Record for mega
    navapur Not found
    Processing Record for kirovohrad
    Processing Record for revelstoke
    Processing Record for biak
    Processing Record for opole
    Processing Record for pascagoula
    Processing Record for vyshkovo
    Processing Record for ogaminana
    Processing Record for senj
    Processing Record for navahrudak
    Processing Record for deoli
    villa vazquez Not found
    Processing Record for perehonivka
    Processing Record for selenginsk
    Processing Record for lomovka
    Processing Record for kununurra
    Processing Record for cache creek
    Processing Record for moron
    Processing Record for keflavik
    Processing Record for wenling
    Processing Record for hasaki
    Processing Record for hrubieszow
    Processing Record for yalta
    Processing Record for manaure
    Processing Record for markivka
    Processing Record for abeche
    tinjah Not found
    Processing Record for ust-kan
    Processing Record for dolinsk
    Processing Record for karchaghbyur
    Processing Record for ferme-neuve
    Processing Record for armenta
    Processing Record for kingsport
    Processing Record for key largo
    Processing Record for buje
    Processing Record for mayskiy
    Processing Record for rapid valley
    Processing Record for dzilam gonzalez
    Processing Record for zhigansk
    Processing Record for ormiston
    Processing Record for villa carmen
    Processing Record for mongo
    Processing Record for sarangani
    Processing Record for aketi
    Processing Record for bad hofgastein
    Processing Record for kisangani
    Processing Record for west lafayette
    Processing Record for bunesti
    Processing Record for solotvyn
    bokspits Not found
    Processing Record for qeshm
    Processing Record for tsagan aman
    Processing Record for plunge
    Processing Record for santa marta
    Processing Record for bay roberts
    Processing Record for kamien pomorski
    Processing Record for mahebourg
    Processing Record for quibdo
    Processing Record for dese
    Processing Record for saint-denis
    Processing Record for maumere
    Processing Record for sauda
    Processing Record for demir hisar
    Processing Record for alugan
    Processing Record for balkhash
    Processing Record for codrington
    Processing Record for rafraf
    Processing Record for kadoshkino
    Processing Record for dutlwe
    Processing Record for alexandria
    Processing Record for granard
    Processing Record for ishigaki
    Processing Record for eganville
    Processing Record for lasa
    Processing Record for giaginskaya
    kushmurun Not found
    Processing Record for zaragoza
    Processing Record for rokytne
    skiros Not found
    Processing Record for novouralsk
    Processing Record for polunochnoye
    Processing Record for kushima
    bardiyah Not found
    kuche Not found
    Processing Record for nicoya
    Processing Record for martinsicuro
    Processing Record for lerici
    Processing Record for dunkirk
    barbar Not found
    Processing Record for rogatica
    Processing Record for la grande
    Processing Record for shawnee
    Processing Record for beaverlodge
    Processing Record for suez
    stoyba Not found
    Processing Record for pulandian
    Processing Record for gannan
    Processing Record for nehe
    Processing Record for alsfeld
    Processing Record for frontera
    Processing Record for brindisi
    Processing Record for yarumal
    Processing Record for sokoto
    Processing Record for port-gentil
    Processing Record for nenjiang
    Processing Record for tukums
    Processing Record for amot
    Processing Record for tshikapa
    Processing Record for digras
    Processing Record for urusha
    Processing Record for javornik
    Processing Record for medenychi
    Processing Record for buenos aires
    dolbeau Not found
    Processing Record for virginia beach
    Processing Record for kaniv
    Processing Record for micheldorf
    Processing Record for caorle
    Processing Record for sayyan
    Processing Record for yashkino
    Processing Record for ploemeur
    Processing Record for port blair
    Processing Record for eau claire
    Processing Record for cowdenbeath
    Processing Record for diapaga
    Processing Record for lincoln
    Processing Record for russkaya polyana
    Processing Record for bati
    Processing Record for inongo



```python
len(maxtemp)

```




    740




```python
dictionary = {
    'cities': city_name,
    'country':country,
    'temp': temp,
    'humidity': humidity,
    'cloud': cloud,
    'wind': wind,    
    'max temp': maxtemp,
    'lat': lat,
    'long': lon
}

weather_data = pd.DataFrame(dictionary)
weather_data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cities</th>
      <th>cloud</th>
      <th>country</th>
      <th>humidity</th>
      <th>lat</th>
      <th>long</th>
      <th>max temp</th>
      <th>temp</th>
      <th>wind</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Serafimovich</td>
      <td>56</td>
      <td>RU</td>
      <td>94</td>
      <td>49.58</td>
      <td>42.73</td>
      <td>275.531</td>
      <td>275.531</td>
      <td>5.81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saint George</td>
      <td>20</td>
      <td>GR</td>
      <td>61</td>
      <td>39.45</td>
      <td>22.34</td>
      <td>282.150</td>
      <td>282.150</td>
      <td>3.60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ati</td>
      <td>0</td>
      <td>TD</td>
      <td>21</td>
      <td>13.21</td>
      <td>18.34</td>
      <td>296.806</td>
      <td>296.806</td>
      <td>4.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Minervino Murge</td>
      <td>20</td>
      <td>IT</td>
      <td>87</td>
      <td>41.09</td>
      <td>16.08</td>
      <td>281.150</td>
      <td>281.150</td>
      <td>4.10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tahoua</td>
      <td>0</td>
      <td>NE</td>
      <td>33</td>
      <td>14.89</td>
      <td>5.26</td>
      <td>293.356</td>
      <td>293.356</td>
      <td>2.31</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Puerto Cabezas</td>
      <td>40</td>
      <td>NI</td>
      <td>88</td>
      <td>14.04</td>
      <td>-83.39</td>
      <td>301.150</td>
      <td>301.150</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yaan</td>
      <td>24</td>
      <td>NG</td>
      <td>81</td>
      <td>7.38</td>
      <td>8.57</td>
      <td>299.156</td>
      <td>299.156</td>
      <td>5.26</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Severo-Kurilsk</td>
      <td>56</td>
      <td>RU</td>
      <td>100</td>
      <td>50.68</td>
      <td>156.12</td>
      <td>271.206</td>
      <td>271.206</td>
      <td>3.31</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Lepaterique</td>
      <td>75</td>
      <td>HN</td>
      <td>36</td>
      <td>14.07</td>
      <td>-87.47</td>
      <td>299.150</td>
      <td>299.150</td>
      <td>5.10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Midland</td>
      <td>48</td>
      <td>US</td>
      <td>33</td>
      <td>32.00</td>
      <td>-102.08</td>
      <td>299.150</td>
      <td>296.400</td>
      <td>8.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a scatter plot for each data type
plt.scatter(weather_data["lat"],weather_data["max temp"], marker="o")

# Incorporate the other graph properties: title and axis labels
plt.title("Max Temperature by Latitude Around the World")
plt.ylabel("Max Temperature")
plt.xlabel("Latitude")

# Turn on the grid
plt.grid(True)

# Save the figure


# Display to screen 
```


![png](output_7_0.png)



```python
# Create a scatter plot for each data type
plt.scatter(weather_data["lat"], weather_data["humidity"], marker="o")

# Incorporate the other graph properties: title and axis labels
plt.title("Humidity by Latitude Around the World")
plt.ylabel("Humidity")
plt.xlabel("Latitude")

# Turn on the grid
plt.grid(True)

# Save the figure


# Display to screen 

```


![png](output_8_0.png)



```python
# Create a scatter plot for each data type
plt.scatter(weather_data["lat"], weather_data["cloud"], marker="o")

# Incorporate the other graph properties: title and axis labels
plt.title("Cloudiness by Latitude Around the World")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")

# Turn on the grid
plt.grid(True)

# Save the figure


# Display to screen 
```


![png](output_9_0.png)



```python
# Create a scatter plot for each data type
wind_lat = plt.scatter(weather_data["lat"], weather_data["wind"],marker="o")

# Incorporate the other graph properties: title and axis labels
plt.title("Wind Speed by Latitude Around the World")
plt.ylabel("Wind")
plt.xlabel("Latitude")

# Turn on the grid
plt.grid(True)

# Save the figure
plt.savefig("wind_lat.png", format="png")

# Display to screen 
```


![png](output_10_0.png)


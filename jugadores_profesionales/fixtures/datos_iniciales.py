from jugadores_profesionales.models import Equipo, Campeonato, JugadorProfesional
from django.utils import timezone
from django.core.files import File
from pathlib import Path
import requests
from django.core.files.base import ContentFile

def descargar_y_guardar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        return ContentFile(response.content, name=nombre_archivo)
    return None

# Crear Campeonatos
lck = Campeonato.objects.create(nombre='LCK', region='Corea del Sur')
lpl = Campeonato.objects.create(nombre='LPL', region='China')
lec = Campeonato.objects.create(nombre='LEC', region='Europa')
las = Campeonato.objects.create(nombre='LAS', region='Latinoamérica Sur')

# URLs de los logos (estas son URLs de ejemplo, asegúrate de usar URLs válidas y con permisos)
LOGOS = {
    't1': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/T1_logo.png',
    'geng': 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Gen.G_logo.png',
    'kt': 'https://upload.wikimedia.org/wikipedia/commons/f/f9/KT_Rolster_logo.png',
    'dk': 'https://upload.wikimedia.org/wikipedia/commons/a/a5/DPlus_KIA_logo.png',
    'jdg': 'https://upload.wikimedia.org/wikipedia/commons/8/8c/JD_Gaming_logo.png',
    # ... más URLs de logos ...
}

# Crear Equipos de Corea (LCK)
t1 = Equipo.objects.create(nombre='T1', pais='Corea del Sur')
logo_t1 = descargar_y_guardar_imagen(LOGOS['t1'], 't1_logo.png')
if logo_t1:
    t1.logo.save('t1_logo.png', logo_t1)

gen_g = Equipo.objects.create(nombre='Gen.G', pais='Corea del Sur')
logo_geng = descargar_y_guardar_imagen(LOGOS['geng'], 'geng_logo.png')
if logo_geng:
    gen_g.logo.save('geng_logo.png', logo_geng)

kt = Equipo.objects.create(nombre='KT Rolster', pais='Corea del Sur')
kt.logo.save('kt_logo.png', File(open('media/equipos/kt_logo.png', 'rb')))

dk = Equipo.objects.create(nombre='DPlus KIA', pais='Corea del Sur')
dk.logo.save('dk_logo.png', File(open('media/equipos/dk_logo.png', 'rb')))

hle = Equipo.objects.create(nombre='Hanwha Life Esports', pais='Corea del Sur')
hle.logo.save('hle_logo.png', File(open('media/equipos/hle_logo.png', 'rb')))

# Crear Equipos de China (LPL)
jdg = Equipo.objects.create(nombre='JD Gaming', pais='China')
jdg.logo.save('jdg_logo.png', File(open('media/equipos/jdg_logo.png', 'rb')))

bilibili = Equipo.objects.create(nombre='Bilibili Gaming', pais='China')
bilibili.logo.save('bilibili_logo.png', File(open('media/equipos/bilibili_logo.png', 'rb')))

weibo = Equipo.objects.create(nombre='Weibo Gaming', pais='China')
weibo.logo.save('weibo_logo.png', File(open('media/equipos/weibo_logo.png', 'rb')))

lgd = Equipo.objects.create(nombre='LGD Gaming', pais='China')
lgd.logo.save('lgd_logo.png', File(open('media/equipos/lgd_logo.png', 'rb')))

rng = Equipo.objects.create(nombre='Royal Never Give Up', pais='China')
rng.logo.save('rng_logo.png', File(open('media/equipos/rng_logo.png', 'rb')))

# Crear Equipos de Europa (LEC)
g2 = Equipo.objects.create(nombre='G2 Esports', pais='Europa')
g2.logo.save('g2_logo.png', File(open('media/equipos/g2_logo.png', 'rb')))

fnatic = Equipo.objects.create(nombre='Fnatic', pais='Europa')
fnatic.logo.save('fnatic_logo.png', File(open('media/equipos/fnatic_logo.png', 'rb')))

mad = Equipo.objects.create(nombre='MAD Lions', pais='Europa')
mad.logo.save('mad_logo.png', File(open('media/equipos/mad_logo.png', 'rb')))

bds = Equipo.objects.create(nombre='Team BDS', pais='Europa')
bds.logo.save('bds_logo.png', File(open('media/equipos/bds_logo.png', 'rb')))

excel = Equipo.objects.create(nombre='Excel', pais='Europa')
excel.logo.save('excel_logo.png', File(open('media/equipos/excel_logo.png', 'rb')))

# Crear Equipos de LAS
isurus = Equipo.objects.create(nombre='Isurus', pais='Argentina')
isurus.logo.save('isurus_logo.png', File(open('media/equipos/isurus_logo.png', 'rb')))

infinity = Equipo.objects.create(nombre='Infinity', pais='Chile')
infinity.logo.save('infinity_logo.png', File(open('media/equipos/infinity_logo.png', 'rb')))

estral = Equipo.objects.create(nombre='Estral Esports', pais='México')
estral.logo.save('estral_logo.png', File(open('media/equipos/estral_logo.png', 'rb')))

r7 = Equipo.objects.create(nombre='Rainbow7', pais='México')
r7.logo.save('r7_logo.png', File(open('media/equipos/r7_logo.png', 'rb')))

six = Equipo.objects.create(nombre='Six Karma', pais='Colombia')
six.logo.save('six_logo.png', File(open('media/equipos/six_logo.png', 'rb')))

# Crear Jugadores LCK
JugadorProfesional.objects.create(
    nombre='Lee',
    apellido='Sang-hyeok',
    ciudad_nacimiento='Seúl',
    fecha_nacimiento=timezone.datetime(1996, 5, 7).date(),
    equipo=t1,
    campeonato=lck
)

JugadorProfesional.objects.create(
    nombre='Choi',
    apellido='Woo-je',
    ciudad_nacimiento='Seúl',
    fecha_nacimiento=timezone.datetime(2003, 8, 30).date(),
    equipo=gen_g,
    campeonato=lck
)

# Jugadores LPL
JugadorProfesional.objects.create(
    nombre='Yu',
    apellido='Wenbo',
    ciudad_nacimiento='Shanghai',
    fecha_nacimiento=timezone.datetime(1998, 12, 15).date(),
    equipo=jdg,
    campeonato=lpl
)

# Jugadores LEC
JugadorProfesional.objects.create(
    nombre='Rasmus',
    apellido='Winther',
    ciudad_nacimiento='Copenhague',
    fecha_nacimiento=timezone.datetime(1999, 11, 17).date(),
    equipo=g2,
    campeonato=lec
)

# Jugadores LAS
JugadorProfesional.objects.create(
    nombre='Brandon',
    apellido='Joel',
    ciudad_nacimiento='Santiago',
    fecha_nacimiento=timezone.datetime(2000, 3, 15).date(),
    equipo=infinity,
    campeonato=las
) 
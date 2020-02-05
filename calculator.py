from fwi import FWICLASS
import math

print('Observed Conditions @ Noon Today')
mth = 7
print('Month (1-12): {}'.format(mth))
# FFMC
ffmc0 = 91.2
print('FFMC: {}'.format(ffmc0))
# DMC
dmc0 = 48
print('DMC: {}'.format(dmc0))
# DC
dc0 = 416.1
print('DC: {}'.format(dc0))

print('Forecast Conditions @ Noon Tomorrow')
# 24 hr Precipitation (mm)
prcp = 0
print('24 hr Precipitation (mm) : {}'.format(prcp))
# Temperature ( C)
temp = 32.7
print('Temperature ( C): {}'.format(temp))
# RH (%)
rhum = 53
print('RH: {}'.format(rhum))
# Wind (km/h)
wind = 18
print('Wind (km/h): {}'.format(wind))

# Tomorrow's FWI Values
print('Tomorrow''s FWI Values')

if rhum > 100.0:
    rhum = 100.0

fwisystem = FWICLASS(temp, rhum, wind, prcp)

ffmc = fwisystem.FFMCcalc(ffmc0)
dmc = fwisystem.DMCcalc(dmc0, mth)
dc = fwisystem.DCcalc(dc0, mth)
isi = fwisystem.ISIcalc(ffmc)
bui = fwisystem.BUIcalc(dmc, dc)
fwi = fwisystem.FWIcalc(isi, bui)

print('Using code from Updated source code for calculating fire danger indices in the canadian forest fire weather index system')
print('FFMC: {}'.format(ffmc))
print('DMC: {}'.format(dmc))
print('DC: {}'.format(dc))
print('ISI: {}'.format(isi))
print('BUI: {}'.format(bui))
print('FWI: {}'.format(fwi))

dsr = 0.0272 * math.pow(fwi, 1.77)
print('DSR {} (according to Equations and FORTRAN program for the Canadian Forest Fire Weather Index System. 1985)'.format(dsr))
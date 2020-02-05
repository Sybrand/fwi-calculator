from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from fwi import FWICLASS

app = FastAPI()


class Forecast(BaseModel):
    temp: float
    rhum: float
    wind: float
    prcp: float


class Observed(BaseModel):
    month: int
    ffmc: float
    dmc: float
    dc: float


class FWIValues(BaseModel):
    ffmc: float
    dmc: float
    dc: float
    isi: float
    bui: float
    fwi: float
    dsr: float


@app.put("/fwi/calculate")
async def calc_fwi(forecast: Forecast, observed: Observed):

    # TODO: move rhum check to validation on contract.
    if forecast.rhum > 100.0:
        forecast.rhum = 100.0

    fwisystem = FWICLASS(temp=forecast.temp, rhum=forecast.rhum, wind=forecast.wind, prcp=forecast.prcp)

    ffmc = fwisystem.FFMCcalc(observed.ffmc)
    dmc = fwisystem.DMCcalc(observed.dmc, observed.month)
    dc = fwisystem.DCcalc(observed.dc, observed.month)
    isi = fwisystem.ISIcalc(ffmc)
    bui = fwisystem.BUIcalc(dmc, dc)
    fwi = fwisystem.FWIcalc(isi, bui)
    dsr = fwisystem.DSRCalc(fwi)

    return FWIValues(ffmc=ffmc, dmc=dmc, dc=dc, isi=isi, bui=bui, fwi=fwi, dsr=dsr)


@app.put("/fwi/percentile")
async def calc_percentile(data: UploadFile = File(...)):

    # starting values
    ffmc0 = 85.0
    dmc0 = 6.0
    dc0 = 15.0

    # Collect fwi values in an array.
    fwi_values = []
    # Iterate through data.
    contents = await data.read()

    return contents
    # for line in contents:
    #     print(line)
    #     mth, day, temp, rhum, wind, prcp = [float(field) for field in line.strip().lstrip('[').rstrip(']').split()]
    #     if rhum > 100.0:
    #         rhum = 100.0
    #     mth = int(mth)
    #     fwisystem = FWICLASS(temp, rhum, wind, prcp)
    #     ffmc = fwisystem.FFMCcalc(ffmc0)
    #     dmc = fwisystem.DMCcalc(dmc0, mth)
    #     dc = fwisystem.DCcalc(dc0, mth)
    #     isi = fwisystem.ISIcalc(ffmc)
    #     bui = fwisystem.BUIcalc(dmc, dc)
    #     fwi = fwisystem.FWIcalc(isi, bui)

    #     data.append(fwi)

    #     ffmc0 = ffmc
    #     dmc0 = dmc
    #     dc0 = dc

    percentile = numpy.percentile(fwi_values, 90)

    return {percentile}

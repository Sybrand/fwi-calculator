from fwi import FWICLASS


def main():
    ffmc0 = 85.0
    dmc0 = 6.0
    dc0 = 15.0
    infile = open('data.txt', 'r')
    outfile = open('fwioutput.txt', 'w')
    try:
        for line in infile:
            mth, day, temp, rhum, wind, prcp = [float(field) for field in line.strip().lstrip('[').rstrip(']').split()]
            if rhum > 100.0:
                rhum = 100.0
            mth = int(mth)
            fwisystem = FWICLASS(temp, rhum, wind, prcp)
            ffmc = fwisystem.FFMCcalc(ffmc0)
            dmc = fwisystem.DMCcalc(dmc0, mth)
            dc = fwisystem.DCcalc(dc0, mth)
            isi = fwisystem.ISIcalc(ffmc)
            bui = fwisystem.BUIcalc(dmc, dc)
            fwi = fwisystem.FWIcalc(isi, bui)

            ffmc0 = ffmc
            dmc0 = dmc
            dc0 = dc
            outfile.write("%s %s %s %s %s %s\n" % (
                str(ffmc), str(dmc), str(dc), str(isi), str(bui), str(fwi)))
    finally:
        infile.close()
        outfile.close()


main()

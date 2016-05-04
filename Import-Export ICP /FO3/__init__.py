from bika.lims.exportimport.instruments.resultsimport import InstrumentCSVResultsFileParser
from bika.lims.exportimport.instruments.instrument import GenericImport, getResultsInputFile

title = "Horiba Jobin Yvon - ICP - LimsLine"
#Ancienne class d'import pour exemple
class HoribaIcpLimsLine(InstrumentCSVResultsFileParser):

    def __init__(self, csv):
        InstrumentCSVResultsFileParser.__init__(self, csv)

    def _parseline(self, line):
        if not line.startswith("SampleID"):
            sline = [token.strip() for token in line.split(';')]
            raw = {sline[3]: {'DefaultResult': 'result',
                              'result': sline[4],
                              'DateTime': sline[1]}}
            self._addRawResult(sline[2], raw)
            return 0

def Import(context, request):
    infile = getResultsInputFile(request)
    parser = HoribaIcpLimsLine(infile)
    res = GenericImport(context, request, parser)
    return res

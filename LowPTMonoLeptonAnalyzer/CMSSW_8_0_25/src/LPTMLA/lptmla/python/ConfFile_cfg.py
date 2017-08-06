#Modulo para configuraciones de parametros
import FWCore.ParameterSet.Config as cms

#Si se quiere se puede tener un archivo aparte
# import Foo.Bar.lo_que_sea

#Inicio el proceso, que en este caso se llama SingleMu
process = cms.Process("SingleMu")

process.load("FWCore.MessageService.MessageLogger_cfi")
#Pongo 100 para no pasar en cada prueba por todos los eventos del archivo (-1)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

#Este modulo lee el archivo de entrada
process.source = cms.Source("PoolSource",
                            # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_Tranch\
eIV_v6_ext1-v1/120000/14473FEF-1ACD-E611-8C84-00266CFFBC60.root'
        )
                            )
# Configure an object that produces a new data object
#process.tracker = cms.EDProducer("TrackFinderProducer")


# Configure the object that writes an output file
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string("test2.root")
#                               )

# Note that more commonly in CMS, we call process.load(Foo.Bar.somefile_cff)
# which both performs the import and calls extend.
#process.extend(Foo.Bar.somefile_cff)

process.SMuAna = cms.EDAnalyzer(
    
    'lptmla'
    
    )

# Configure a path and endpath to run the producer and output modules
process.p = cms.Path(process.SMuAna)
#process.ep = cms.EndPath(process.out)

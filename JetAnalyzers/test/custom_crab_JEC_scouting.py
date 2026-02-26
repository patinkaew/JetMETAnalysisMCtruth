from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
#config.General.requestName = 'QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8_Run3Summer23BPix-EpsilonPU'
#config.General.requestName = 'QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8_Run3Summer23-EpsilonPU'
#config.General.requestName = 'QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8_Run3Summer23-NoPU'
#config.General.requestName = 'QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8_Run3Summer23'
#config.General.requestName = 'QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24'
#config.General.requestName = 'QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24-EpsilonPU'
config.General.requestName = 'QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24-NoPU'
config.General.workArea = 'crab_projects/jra_ntuple_v0p0'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'src/JetMETAnalysisMCtruth/JetAnalyzers/test/run_JRA_MCtruth_scouting_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.priority = 12000
#config.JobType.inputFiles = ['']

config.section_("Data")
#config.Data.inputDataset = '/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-NoPU_castor_130X_mcRun3_2023_realistic_postBPix_v2-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-EpsilonPU_castor_130X_mcRun3_2023_realistic_postBPix_v2-v2/MINIAODSIM'
#config.Data.inputDataset = '/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-EpsilonPU_castor_130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM'
#config.Data.inputDataset = '/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-NoPU_castor_130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-castor_130X_mcRun3_2023_realistic_v14-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-140X_mcRun3_2024_realistic_v26-v2/MINIAODSIM'
#config.Data.inputDataset = '/QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-EpsilonPU_140X_mcRun3_2024_realistic_v26-v2/MINIAODSIM'
config.Data.inputDataset = '/QCD_Bin-PT-15to7000_Par-PT-flat2022_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAOD-NoPU_140X_mcRun3_2024_realistic_v26-v2/MINIAODSIM'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.outLFNDirBase = '/store/group/phys_jetmet/pinkaew/'
config.Data.useParent = False # need for 2022-23
config.Data.allowNonValidInputDataset = True
#config.Data.partialDataset = True

config.section_("Site")
config.Site.whitelist = [
'T1_US_*',
'T1_ES_*',
'T1_IT_*',
'T1_FR_*',
'T1_RU_*',
'T1_DE_*',
'T2_US_*',
'T2_UK_*',
'T2_RU_*',
'T2_DE_*',
'T2_FR_*',
'T2_FI_*',
'T2_CH_*',
'T2_IT_*',
'T2_ES_*',
'T2_HU_*',
'T2_BE_*',
'T2_BR_*',
'T2_CN_*',
'T2_EE_*',
'T2_TW_*',
]
config.Site.storageSite = 'T2_CH_CERN'

#include "FWCore/Framework/interface/MakerMacros.h"
//#include "PhysicsTools/UtilAlgos/interface/SingleObjectSelector.h"
//#include "PhysicsTools/UtilAlgos/interface/PtMinSelector.h"
//#include "PhysicsTools/UtilAlgos/interface/EtaRangeSelector.h"
//#include "PhysicsTools/UtilAlgos/interface/AndSelector.h"
#include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/PtMinSelector.h"
#include "CommonTools/UtilAlgos/interface/EtaRangeSelector.h"
#include "CommonTools/UtilAlgos/interface/AndSelector.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Scouting/interface/Run3ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Run3ScoutingParticle.h"

typedef SingleObjectSelector<
  edm::View<reco::Candidate>,
  AndSelector<PtMinSelector,EtaRangeSelector>
>
EtaPtMinCandViewRefSelector;

DEFINE_FWK_MODULE(EtaPtMinCandViewRefSelector);

typedef SingleObjectSelector<
  edm::View<Run3ScoutingPFJet>,
  AndSelector<PtMinSelector, EtaRangeSelector>
>
EtaPtMinRun3ScoutingPFJetViewRefSelector;

DEFINE_FWK_MODULE(EtaPtMinRun3ScoutingPFJetViewRefSelector);

typedef SingleObjectSelector<
  edm::View<Run3ScoutingParticle>,
  AndSelector<PtMinSelector, EtaRangeSelector>
>
EtaPtMinRun3ScoutingParticleViewRefSelector;

DEFINE_FWK_MODULE(EtaPtMinRun3ScoutingParticleViewRefSelector);

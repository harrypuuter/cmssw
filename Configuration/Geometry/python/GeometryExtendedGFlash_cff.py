import FWCore.ParameterSet.Config as cms

#
# Geometry master configuration
#
# Ideal geometry, needed for simulation
from Geometry.CMSCommonData.cmsExtendedGeometryGFlashXML_cfi import *
from Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi import *
from Geometry.HcalCommonData.hcalDDDSimConstants_cff import *

# Reconstruction geometry services
from Configuration.Geometry.GeometryReco_cff import *

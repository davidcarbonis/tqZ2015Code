#A tool to pull a load of information from the mva trees. Should be all easy jazz...

from ROOT import *

import numpy as n
import random
import sys
import os
from array import array
from jetCorrectionUncertainty import JetCorrectionUncertainty

def deltaR(eta1, phi1, eta2, phi2):
    ###Returns the delta R from the eta and phi of two particles.
    dEta = eta1-eta2
    dPhi = phi1-phi2
    while ( n.fabs(dPhi) > n.pi ):
	if (dPhi > 0.0):
	    dPhi += -2*n.pi
	else:
	    dPhi += 2*n.pi
    return n.sqrt( dEta*dEta + dPhi*dPhi )

def sortOutLeptons(tree,channel):
    ###Returns two LorentzVectors containing the two z leptons. This will be VERY useful for making all of the plots.
    #Reads the position of the z leptons from variables stored at mvaTree making time, because I'm great and finally got around to doing it.
    zLep1,zLep2 = 0,0
    #Let's try commenting this out and see if everything breaks? Hopefully it won't do...
    #if tree.numElePF2PAT < 3:
    if channel == "ee":
        zLep1 = TLorentzVector(tree.elePF2PATGsfPx[tree.zLep1Index],tree.elePF2PATGsfPy[tree.zLep1Index],tree.elePF2PATGsfPz[tree.zLep1Index],tree.elePF2PATGsfE[tree.zLep1Index])
        zLep2 = TLorentzVector(tree.elePF2PATGsfPx[tree.zLep2Index],tree.elePF2PATGsfPy[tree.zLep2Index],tree.elePF2PATGsfPz[tree.zLep2Index],tree.elePF2PATGsfE[tree.zLep2Index])
    if channel == "mumu":
        zLep1 = TLorentzVector(tree.muonPF2PATPx[tree.zLep1Index],tree.muonPF2PATPy[tree.zLep1Index],tree.muonPF2PATPz[tree.zLep1Index],tree.muonPF2PATE[tree.zLep1Index])
        zLep2 = TLorentzVector(tree.muonPF2PATPx[tree.zLep2Index],tree.muonPF2PATPy[tree.zLep2Index],tree.muonPF2PATPz[tree.zLep2Index],tree.muonPF2PATE[tree.zLep2Index])
    return (zLep1,zLep2)

def sortOutHadronicW(tree,channel):

    ###Returns two LorentzVectors containing the two w quarks. This will be VERY useful for making all of the plots.
    #Reads the position of the w quarks from variables stored at mvaTree making time, because I'm great and finally got around to doing it.
    wQuark1,wQuark2 = 0,0

    wQuark1 = TLorentzVector(tree.jetPF2PATPx[tree.wQuark1Index],tree.jetPF2PATPx[tree.wQuark1Index],tree.jetPF2PATPz[tree.wQuark1Index ],tree.jetPF2PATE[tree.wQuark1Index])
    wQuark2 = TLorentzVector(tree.jetPF2PATPx[tree.wQuark2Index],tree.jetPF2PATPx[tree.wQuark2Index],tree.jetPF2PATPz[tree.wQuark2Index ],tree.jetPF2PATE[tree.wQuark2Index])
    return (wQuark1,wQuark2)

def getJets(tree,syst,jetUnc,met):
    #Makes a short list of indices of the jets in the event
    jetList = []
    jetVecList = []
    for i in range(15):
        if tree.jetInd[i] > -.5:
            jetList.append(tree.jetInd[i])
            jetVecList.append(getJetVec(tree,tree.jetInd[i],syst,jetUnc,met))
        else: continue
    return (jetList,jetVecList)

def getBjets(tree,syst,jetUnc,met,jets):
    #Return a list of the indices of the b-jets in the event
    bJetList = []
    bJetVecList = []
    for i in range(10):
        if tree.bJetInd[i] > -0.5:
            bJetList.append(tree.bJetInd[i])
            bJetVecList.append(getJetVec(tree,jets[tree.bJetInd[i]],syst,jetUnc,met))
        else:continue
#    print len(bJetList)
    return (bJetList,bJetVecList)

def getJetVec(tree, index, syst, jetUnc, metVec):
    #Gets a vector for a jet and applies jet corrections.

    newSmearValue = 1.0;
    jerSF = 0.0;
    jerSigma = 0.0;

    if (n.fabs(tree.jetPF2PATEta[index]) <= 0.5) :
        jerSF = 1.095;
        jerSigma = 0.018;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 0.8) :
        jerSF = 1.120
        jerSigma = 0.028;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 1.1) :
        jerSF = 1.097;
        jerSigma = 0.017;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 1.3) :
        jerSF = 1.103;
        jerSigma = 0.033;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 1.7) :
        jerSF = 1.118;
        jerSigma = 0.014;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 1.9) :
        jerSF = 1.100;
        jerSigma = 0.033;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 2.1) :
        jerSF = 1.162;
        jerSigma = 0.044;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 2.3) :
        jerSF = 1.160;
        jerSigma = 0.048;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 2.5) :
        jerSF = 1.161;
        jerSigma = 0.060;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 2.8) :
        jerSF = 1.209;
        jerSigma = 0.059;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 3.0) :
        jerSF = 1.564
        jerSigma = 0.321;
    elif (n.fabs(tree.jetPF2PATEta[index]) <= 3.2) :
        jerSF = 1.384;
        jerSigma = 0.033;
    else :
        jerSF = 1.216;
        jerSigma = 0.050;

    returnJet = TLorentzVector();
    if (jetUnc and tree.genJetPF2PATPT[index] > -990.) :
        if ( deltaR(tree.genJetPF2PATEta[index],tree.genJetPF2PATPhi[index],tree.jetPF2PATEta[index],tree.jetPF2PATEta[index] ) < 0.4/2.0 ):
            if (syst == 16): jerSF += jerSigma
            elif (syst == 32): jerSF -= jerSigma
            newSmearValue = max(0.0,tree.jetPF2PATPtRaw[index] + ( tree.jetPF2PATPtRaw[index]  - tree.genJetPF2PATPT[index]) * jerSF)/tree.jetPF2PATPtRaw[index]
            returnJet.SetPxPyPzE(newSmearValue*tree.jetPF2PATPx[index],newSmearValue*tree.jetPF2PATPy[index],newSmearValue*tree.jetPF2PATPz[index],newSmearValue*tree.jetPF2PATE[index])
        else :
           random.seed()
           newSmearValue = 1.0+TRandom(random.randint(0,65539)).Gaus(0.0,n.sqrt(jerSF*jerSF-1)*jerSigma)
           returnJet.SetPxPyPzE(newSmearValue*tree.jetPF2PATPx[index],newSmearValue*tree.jetPF2PATPy[index],newSmearValue*tree.jetPF2PATPz[index],newSmearValue*tree.jetPF2PATE[index])

    else : returnJet.SetPxPyPzE(tree.jetPF2PATPx[index],tree.jetPF2PATPy[index],tree.jetPF2PATPz[index],tree.jetPF2PATE[index]);

    if (newSmearValue > 0.01):
        #Propogate through the met. But only do it if the smear jet isn't 0.
        metVec.SetPx(metVec.Px()+tree.jetPF2PATPx[index])
        metVec.SetPy(metVec.Py()+tree.jetPF2PATPy[index])

    if syst == 16:
        returnJet *= 1+ jetUnc.getUncertainty(returnJet.Pt(), returnJet.Eta(),1)
    elif syst == 32:
        returnJet *= 1+ jetUnc.getUncertainty(returnJet.Pt(), returnJet.Eta(),2)

    metVec.SetPx(metVec.Px()-returnJet.Px())
    metVec.SetPy(metVec.Py()-returnJet.Py())
    return returnJet

def setupInputVars():
    #Make the variables we want to save
    inputVars = {}
    inputVars["eventWeight"] = array('f',[0.])
    inputVars["mTW"] = array('f',[0.])
    inputVars["wQuark1Pt"] = array('f',[0.])
    inputVars["wQuark1Eta"] = array('f',[0.])
    inputVars["wQuark1Phi"] = array('f',[0.])
    inputVars["wQuark2Pt"] = array('f',[0.])
    inputVars["wQuark2Eta"] = array('f',[0.])
    inputVars["wQuark2Phi"] = array('f',[0.])
    inputVars["met"] = array('f',[0.])
    inputVars["nJets"] = array('f',[0.])
    inputVars["leadJetPt"] = array('f',[0.])
    inputVars["leadJetPhi"] = array('f',[0.])
    inputVars["leadJetEta"] = array('f',[0.])
    inputVars["leadJetbTag"] = array('f',[0.])
    inputVars["secJetPt"] = array('f',[0.])
    inputVars["secJetPhi"] = array('f',[0.])
    inputVars["secJetEta"] = array('f',[0.])
    inputVars["secJetbTag"] = array('f',[0.])
    inputVars["nBjets"] = array('f',[0.])
    inputVars["bTagDisc"] = array('f',[0.])
    inputVars["lep1Pt"] = array('f',[0.])
    inputVars["lep1Eta"] = array('f',[0.])
    inputVars["lep1Phi"] = array('f',[0.])
    inputVars["lep1RelIso"] = array('f',[0.])
    inputVars["lep1D0"] = array('f',[0.])
    inputVars["lep2Pt"] = array('f',[0.])
    inputVars["lep2Eta"] = array('f',[0.])
    inputVars["lep2Phi"] = array('f',[0.])
    inputVars["lep2RelIso"] = array('f',[0.])
    inputVars["lep2D0"] = array('f',[0.])
    inputVars["lepMass"] = array('f',[0.])
    inputVars["lepPt"] = array('f',[0.])
    inputVars["lepEta"] = array('f',[0.])
    inputVars["lepPhi"] = array('f',[0.])
    inputVars["zMass"] = array('f',[0.])
    inputVars["zPt"] = array('f',[0.])
    inputVars["zEta"] = array('f',[0.])
    inputVars["zPhi"] = array('f',[0.])
    inputVars["topMass"] = array('f',[0.])
    inputVars["topPt"] = array('f',[0.])
    inputVars["topEta"] = array('f',[0.])
    inputVars["topPhi"] = array('f',[0.])
    inputVars["j1j2delR"] = array('f',[0.])
    inputVars["j1j2delPhi"] = array('f',[0.])
    inputVars["zLepdelR"] = array('f',[0.])
    inputVars["zLepdelPhi"] = array('f',[0.])
    inputVars["zlb1DelR"] = array('f',[0.])
    inputVars["zlb1DelPhi"] = array('f',[0.])
    inputVars["zlb2DelR"] = array('f',[0.])
    inputVars["zlb2DelPhi"] = array('f',[0.])
    inputVars["lepHt"] = array('f',[0.])
    inputVars["wQuarkHt"] = array('f',[0.])
    inputVars["totPt"] = array('f',[0.])
    inputVars["totEta"] = array('f',[0.])
    inputVars["totPtVec"] = array('f',[0.])
    inputVars["totVecM"] = array('f',[0.])
    inputVars["chan"] = array('i',[0])
    inputVars["totPt2Jet"] = array('f',[0.])
    inputVars["wZdelR"] = array('f',[0.])
    inputVars["wZdelPhi"] = array('f',[0.])
    inputVars["minZJetR"] = array('f',[0.])
    inputVars["minZJetPhi"] = array('f',[0.])
    inputVars["totHt"] = array('f',[0.])
    inputVars["jetHt"] = array('f',[0.])
    inputVars["totHtOverPt"] = array('f',[0.])
    return inputVars

def setupBranches(tree,varMap):
    tree.Branch("EvtWeight", varMap["eventWeight"], "EvtWeight/F")
    tree.Branch("mTW", varMap["mTW"], "mTW/F")
    tree.Branch("wQuark1Pt", varMap["wQuark1Pt"], "wQuark1Pt/F")
    tree.Branch("wQuark1Eta", varMap["wQuark1Eta"], "wQuark1Eta/F")
    tree.Branch("wQuark1Phi", varMap["wQuark1Phi"], "wQuark1Phi/F")
    tree.Branch("wQuark2Pt", varMap["wQuark2Pt"], "wQuark2Pt/F")
    tree.Branch("wQuark2Eta", varMap["wQuark2Eta"], "wQuark2Eta/F")
    tree.Branch("wQuark2Phi", varMap["wQuark2Phi"], "wQuark2Phi/F")
    tree.Branch("met",varMap["met"],"met/F")
    tree.Branch("nJets",varMap["nJets"],"nJets/F")
    tree.Branch("leadJetPt",varMap["leadJetPt"],"leadJetPt/F")
    tree.Branch("leadJetEta",varMap["leadJetEta"],"leadJetEta/F")
    tree.Branch("leadJetPhi",varMap["leadJetPhi"],"leadJetPhi/F")
    tree.Branch("leadJetbTag",varMap["leadJetbTag"],"leadJetbTag/F")
    tree.Branch("secJetPt",varMap["secJetPt"],"secJetPt/F")
    tree.Branch("secJetEta",varMap["secJetEta"],"secJetEta/F")
    tree.Branch("secJetPhi",varMap["secJetPhi"],"secJetPhi/F")
    tree.Branch("secJetbTag",varMap["secJetbTag"],"secJetbTag/F")
    tree.Branch("NBJets",varMap["nBjets"],"NBJets/F")
    tree.Branch("btagDiscri",varMap["bTagDisc"],"btagDiscri/F")
    tree.Branch("lep1Pt",varMap["lep1Pt"],"lep1Pt/F")
    tree.Branch("lep1Eta",varMap["lep1Eta"],"lep1Eta/F")
    tree.Branch("lep1Phi",varMap["lep1Phi"],"lep1Phi/F")
    tree.Branch("lep1RelIso",varMap["lep1RelIso"],"lep1RelIso/F")
    tree.Branch("lep1D0",varMap["lep1D0"],"lep1D0/F")
    tree.Branch("lep2Pt",varMap["lep2Pt"],"lep2Pt/F")
    tree.Branch("lep2Eta",varMap["lep2Eta"],"lep2Eta/F")
    tree.Branch("lep2Phi",varMap["lep2Phi"],"lep2Phi/F")
    tree.Branch("lep2RelIso",varMap["lep2RelIso"],"lep2RelIso/F")
    tree.Branch("lep2D0",varMap["lep2D0"],"lep2D0/F")
    tree.Branch("lepMass",varMap["lepMass"],"lepMass/F")
    tree.Branch("lepPt",varMap["lepPt"],"lepPt/F")
    tree.Branch("lepEta",varMap["lepEta"],"lepEta/F")
    tree.Branch("lepPhi",varMap["lepPhi"],"lepPhi/F")
    tree.Branch("zMass",varMap["zMass"],"zMass/F")
    tree.Branch("Zpt",varMap["zPt"],"Zpt/F")
    tree.Branch("Zeta",varMap["zEta"],"Zeta/F")
    tree.Branch("Zphi",varMap["zPhi"],"Zphi/F")
    tree.Branch("topMass",varMap["topMass"],"topMass/F")
    tree.Branch("topPt",varMap["topPt"],"topPt/F")
    tree.Branch("topEta",varMap["topEta"],"topEta/F")
    tree.Branch("topPhi",varMap["topPhi"],"topPhi/F")
    tree.Branch("jjdelR",varMap["j1j2delR"],"jjdelR/F")
    tree.Branch("jjdelPhi",varMap["j1j2delPhi"],"jjdelPhi/F")
    tree.Branch("zLepdelR",varMap["zLepdelR"],"zLepdelR/F")
    tree.Branch("zLepdelPhi",varMap["zLepdelPhi"],"zLepdelPhi/F")
    tree.Branch("zlb1DelR",varMap["zlb1DelR"],"zlb1DelR/F")
    tree.Branch("zlb1DelPhi",varMap["zlb1DelPhi"],"zlb1DelPhi/F")
    tree.Branch("zlb2DelR",varMap["zlb2DelR"],"zlb2DelR/F")
    tree.Branch("zlb2DelPhi",varMap["zlb2DelPhi"],"zlb2DelPhi/F")
    tree.Branch("lepHt",varMap["lepHt"],"lepHt/F")
    tree.Branch("wQuarkHt",varMap["wQuarkHt"],"wQuarkHt/F")
    tree.Branch("jetHt",varMap["jetHt"],"jetHt/F")
    tree.Branch("totHt",varMap["totHt"],"totHt/F")
    tree.Branch("totHtOverPt",varMap["totHtOverPt"],"totHtOverPt/F")
    tree.Branch("totPt",varMap["totPt"],"totPt/F")
    tree.Branch("totEta",varMap["totEta"],"totEta/F")
    tree.Branch("totPtVec",varMap["totPtVec"],"totPtVec/F")
    tree.Branch("totVecM",varMap["totVecM"],"totVecM/F")
    tree.Branch("Channel",varMap["chan"],"Channel/I")
    tree.Branch("totPt2Jet",varMap["totPt2Jet"],"totPt2Jet/F")
    tree.Branch("wzdelR",varMap["wZdelR"],"wzdelR/F")
    tree.Branch("wzdelPhi",varMap["wZdelPhi"],"wzdelPhi/F")
    tree.Branch("zjminR",varMap["minZJetR"],"zjminR/F")
    tree.Branch("zjminPhi",varMap["minZJetPhi"],"zjminPhi/F")



def fillTree(outTree, varMap, tree, label, channel, jetUnc, zPtEventWeight = 0.):
    #Fills the output tree. This is a new function because I want to access data and MC in different ways but do the same thing to them in the end.
    syst = 0
    if "__jer__plus" in label:
        syst = 4
    if "__jer__minus" in label:
        syst = 8
    if "__jes__plus" in label:
        syst = 16
    if "__jes__minus" in label:
        syst = 32
    if channel == "ee":
        varMap["chan"][0] = 1
    if channel == "mumu":
        varMap["chan"][0] = 0
    #        topMass
    #Set up those variables as branches
    for event in range(tree.GetEntries()):
            #Fill some plots here. Let's make an example mTW plot.
            #Make a config that'll do this for me? I've done these before so should be easy. Fill expressions could be a pain?
        tree.GetEntry(event)
        (zLep1,zLep2) = sortOutLeptons(tree,channel)
        metVec = TLorentzVector(tree.metPF2PATPx,tree.metPF2PATPy,0,tree.metPF2PATEt)
        (jets,jetVecs) = getJets(tree,syst,jetUnc,metVec)
        (bJets,bJetVecs) = getBjets(tree,syst,jetUnc,metVec,jets)
        (wQuark1,wQuark2) = sortOutHadronicW(tree,channel)
        #Do unclustered met stuff here now that we have all of the objects, all corrected for their various SFs etc.
        varMap["eventWeight"][0] = tree.eventWeight
        varMap["leadJetPt"][0] = jetVecs[0].Pt()
        varMap["leadJetEta"][0] = jetVecs[0].Eta()
        varMap["leadJetPhi"][0] = jetVecs[0].Phi()
        #Make all the random Pt variables I'm saving for some reason
        totPx,totPy = 0,0
        totPx += zLep1.Px() + zLep2.Px()
        totPy += zLep1.Py() + zLep2.Py()
	varMap["lep1Pt"][0] = zLep1.Pt()
	varMap["lep1Eta"][0] = zLep1.Eta()
	varMap["lep1Phi"][0] = zLep1.Phi()
        if channel == "ee":
            varMap["lep1RelIso"][0] = tree.elePF2PATComRelIsoRho[tree.zLep1Index]
	    varMap["lep1D0"][0] = tree.elePF2PATD0PV[tree.zLep1Index]
	    varMap["lep2RelIso"][0] = tree.elePF2PATComRelIsoRho[tree.zLep2Index]
	    varMap["lep2D0"][0] = tree.elePF2PATD0PV[tree.zLep2Index]
	if channel == "mumu":
            varMap["lep1RelIso"][0] = tree.muonPF2PATComRelIsodBeta[tree.zLep1Index]
	    varMap["lep1D0"][0] = tree.muonPF2PATDBPV[tree.zLep1Index]
	    varMap["lep2RelIso"][0] = tree.muonPF2PATComRelIsodBeta[tree.zLep2Index]
	    varMap["lep2D0"][0] = tree.muonPF2PATDBPV[tree.zLep2Index]

	varMap["lep2Pt"][0] = zLep2.Pt()
	varMap["lep2Eta"][0] = zLep2.Eta()
	varMap["lep2Phi"][0] = zLep2.Phi()
	varMap["lepMass"][0] = ( zLep1 + zLep2 ).M()
        varMap["lepPt"][0] = n.sqrt(totPx * totPx + totPy * totPy)
	varMap["lepEta"][0] = ( zLep1 + zLep2 ).Eta()
	varMap["lepPhi"][0] = ( zLep1 + zLep2 ).Phi()
	varMap["wQuark1Pt"][0] = wQuark1.Pt()
	varMap["wQuark1Eta"][0] = wQuark1.Eta()
	varMap["wQuark1Phi"][0] = wQuark1.Phi()
	varMap["wQuark2Pt"][0] = wQuark2.Pt()
	varMap["wQuark2Eta"][0] = wQuark2.Eta()
	varMap["wQuark2Phi"][0] = wQuark2.Phi()
        totPx += jetVecs[0].Px()
        totPy += jetVecs[0].Py()
        if len(jetVecs) > 1:
            totPx += jetVecs[1].Px()
            totPy += jetVecs[1].Py()
        varMap["totPt2Jet"][0] = n.sqrt(totPx * totPx + totPy * totPy)
        for i in range(2,len(jets)):
            totPx+=jetVecs[i].Px()
            totPy+=jetVecs[i].Py()
        varMap["totPt"][0] = n.sqrt(totPx * totPx + totPy * totPy)
        totVec = (zLep1+zLep2)
        for i in range(len(jetVecs)):
            totVec += jetVecs[i]
        varMap["totEta"][0] = totVec.Eta()
        varMap["totPtVec"][0] = totVec.Pt()
        varMap["totVecM"][0] = totVec.M()
        varMap["mTW"][0] = n.sqrt(2*tree.jetPF2PATPt[tree.wQuark1Index]*tree.jetPF2PATPt[tree.wQuark2Index] * (1-n.cos(tree.jetPF2PATPhi[tree.wQuark1Index] - tree.jetPF2PATPhi[tree.wQuark2Index])))
        varMap["nJets"][0] = float(len(jets))
        varMap["nBjets"][0] = float(len(bJets))
        varMap["met"][0] = tree.metPF2PATEt
        varMap["bTagDisc"][0] = tree.jetPF2PATBDiscriminator[jets[bJets[0]]]
        varMap["leadJetbTag"][0] = tree.jetPF2PATBDiscriminator[jets[0]]
        varMap["secJetbTag"][0] = -1.
        varMap["secJetPt"][0] = -1.
        varMap["secJetEta"][0] = -500.
        varMap["secJetPhi"][0] = -500.
        if len(jetVecs) > 1:
            varMap["secJetPt"][0] = jetVecs[1].Pt()
            varMap["secJetEta"][0] = jetVecs[1].Eta()
            varMap["secJetPhi"][0] = jetVecs[1].Phi()
            varMap["secJetbTag"][0] = tree.jetPF2PATBDiscriminator[jets[1]]

#        print bTagDisc[0], bJets[0], tree.jetPF2PATBDiscriminator[jets[bJets[0]]], len(bJets), nBjets[0]
        varMap["topMass"][0] = (bJetVecs[0] + wQuark1 + wQuark2).M()
        varMap["topPt"][0] = (bJetVecs[0] + wQuark1 + wQuark2).Pt()
        varMap["topEta"][0] = (bJetVecs[0] + wQuark1 + wQuark2).Eta()
        varMap["topPhi"][0] = (bJetVecs[0] + wQuark1 + wQuark2).Phi()
        varMap["wZdelR"][0] = (zLep2 + zLep1).DeltaR(wQuark1 + wQuark2)
        varMap["wZdelPhi"][0] = (zLep2 + zLep1).DeltaPhi(wQuark1 + wQuark2)
        varMap["j1j2delR"][0] = -1.
        varMap["j1j2delPhi"][0] = -10.
        if len(jetVecs) > 1:
            varMap["j1j2delR"][0] = jetVecs[0].DeltaR(jetVecs[1])
            varMap["j1j2delPhi"][0] = jetVecs[0].DeltaPhi(jetVecs[1])
	varMap["zLepdelR"][0] = (zLep1).DeltaR(zLep2)
	varMap["zLepdelPhi"][0] = (zLep1).DeltaPhi(zLep2)
        varMap["minZJetR"][0] = 3.0
        jetHt = 0.
        for i in range(len(jetVecs)):
            jetHt += jetVecs[i].Pt()
            if jetVecs[i].DeltaR(zLep2 + zLep1) < varMap["minZJetR"][0]:
                varMap["minZJetR"][0] = jetVecs[i].DeltaR(zLep2 + zLep1)
            if jetVecs[i].DeltaPhi(zLep2 + zLep1) < varMap["minZJetR"][0]:
                varMap["minZJetPhi"][0] = jetVecs[i].DeltaPhi(zLep2 + zLep1)
        outTree.Fill()
        varMap["zlb1DelR"][0] = zLep1.DeltaR(jetVecs[bJets[0]])
        varMap["zlb1DelPhi"][0] = zLep1.DeltaPhi(jetVecs[bJets[0]])
        varMap["zlb2DelR"][0] = zLep2.DeltaR(jetVecs[bJets[0]])
        varMap["zlb2DelPhi"][0] = zLep2.DeltaPhi(jetVecs[bJets[0]])
        ht = 0.
        ht += zLep1.Pt() + zLep2.Pt()
        varMap["lepHt"][0] = ht
        varMap["jetHt"][0] = jetHt
        ht += jetHt
        varMap["totHt"][0] = ht
        varMap["totHtOverPt"][0] = ht / n.sqrt(totPx * totPx + totPy * totPy) 
        varMap["zMass"][0] = (zLep1+zLep2).M()
        varMap["zPt"][0] = (zLep2 + zLep1).Pt()
        varMap["zEta"][0] = (zLep2 + zLep1).Eta()
        varMap["zPhi"][0] = (zLep2 + zLep1).Phi()


def main():

    #Mapping of our mc names to IPHC names
    listOfMCs = {"WW1l1nu2q" : "WW", "WW2l2nu":"WW","ZZ4l":"ZZ","ZZ2l2nu":"ZZ","ZZ2l2q":"ZZ","WZjets":"WZ","WZ2l2q":"WZ","WZ1l1nu2q":"WZ","sChannel":"TsChan","tChannel":"TtChan","tbarChannel":"TbartChan","tWInclusive":"TtW","tbarWInclusive":"TbartW","tZq":"tZq","tHq":"THQ","ttW":"TTW","ttZ":"TTZ","ttbarInclusivePowerheg":"TT","wPlusJets":"Wjets","DYJetsToLL_M-50":"DYToLL_M-50","DYJetsToLL_M-10To50":"DYToLL_M10-50"}
#    listOfMCs = {}

    #Set-up JEC corrections
    jetUnc = JetCorrectionUncertainty("scaleFactors/Fall15_25nsV2_MC_Uncertainty_AK4PFchs.txt")

    #mapping of channels to dataTypes
    channelToDataset = {"ee":"DataEG","mumu":"DataMu"}

    #systematics list
    systs = ["","__trig__plus","__trig__minus","__jer__plus","__jer__minus","__jes__plus","__jes__minus","__pileup__plus","__pileup__minus","__bTag__plus","__bTag__minus","__pdf__plus","__pdf__minus","__ME_PS__plus","__ME_PS__minus"]

    #read what channel we're using here - changing this so that multiple things can be stored in the same file. i.e. should now be a list of channels to run over
    channels = eval(sys.argv[1])

    #Might make this customisable later, but don't really feel like I need to yet
    inputDir = "mvaTest/"
    if len(sys.argv) > 2:
        inputDir = sys.argv[2]
    
    outputDir = "mvaInputs/"
    if len(sys.argv) > 3:
        outputDir = sys.argv[3]
    inputVars = setupInputVars()

    #Loop over samples
    for sample in listOfMCs.keys():
        print "Doing " + sample + ": ",
        sys.stdout.flush()
        
        outFile = 0
        #update the appropriate root file
        outFile = TFile(outputDir+"histofile_"+listOfMCs[sample] + ".root","RECREATE")

        for syst in systs:
            #We now define the outtree out here, coz it seems like a more sensible option.
            outTree = TTree("Ttree_"+listOfMCs[sample]+syst, "Ttree_"+listOfMCs[sample]+syst)
            setupBranches(outTree,inputVars)
            for channel in channels:
                inFile = TFile(inputDir+sample+channel+"mvaOut.root","READ")
                tree = inFile.Get("tree"+syst)
                try:
                    print syst +  " : " + str(tree.GetEntriesFast())
                    sys.stdout.flush()
                    fillTree(outTree, inputVars, tree, listOfMCs[sample]+syst, channel, jetUnc)
                except AttributeError:
                    print syst + " : " + "0",
                    sys.stdout.flush()
                    #Various stuff needs to be saved in the same trees. Create new one if it doesn't exist, open current one if it does            
                inFile.Close()
            outFile.cd()
            outFile.Write()
            outTree.Write()
        #if tree exists just update that.
        #        if outFile.GetListOfKeys().Contains("Ttree_"+listOfMCs[sample]):
        #            outTree = outFile.Get("Ttree_"+listOfMCs[sample])
        #        else:
    #next do the data files
        outFile.Write()
        outFile.Close()
        print
    chanMap = {"ee":"eeRun2015","mumu":"mumuRun2015"}

    outChannels = ["DataEG","DataMu"]
    outChanToData = {}
    outChanToData["DataEG"] = ["ee"]
    outChanToData["DataMu"] = ["mumu"]

    for outChan in outChannels:
        print "Data ",outChan
        outTree = TTree("Ttree_"+outChan,"Ttree_"+outChan)
        setupBranches(outTree,inputVars)
        outFile = TFile(outputDir+"histofile_"+outChan+".root","RECREATE")
        for chan in outChanToData[outChan]:
            dataChain = TChain("tree")    
            for run in ["C","D"]:
                dataChain.Add(inputDir+chanMap[chan]+run+chan+"mvaOut.root")
            fillTree(outTree, inputVars, dataChain, outChan, chan, 0)
        outFile.cd()
        outFile.Write()
        outTree.Write()
        outFile.Close()

if __name__ == "__main__":
    main()

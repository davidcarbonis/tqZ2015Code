#!/bin/bash
echo Updating filelists for datasets used ...
echo First deleting old filelists ...

if [ -z "$TQZ_TOOLS_PATH" ]; then
    echo '$TQZ_TOOLS_PATH not set, setting to .'
    export TQZ_TOOLS_PATH='.'
fi


rm $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/*

echo Done!
echo Now outputting the lists of the dataset directories into their relevant files ...


# Normal datasets

ls /scratch/data/tZqSkimsRun2016/eeRun2016B_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016C_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016D_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016E/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016F/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016G/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/eeRun2016H/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/eeRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016B_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016C_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016D_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016E/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016F/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016G/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/emuRun2016H/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/emuRun2016Files.txt

ls /scratch/data/tZqSkimsRun2016/mumuRun2016B_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016C_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016D_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016E/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016F/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016G/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016H/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016Files.txt

ls /scratch/data/tZqSkimsRun2016/mumuRun2016B_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart1.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016C_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart1.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016D_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart1.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016E/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart1.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016F/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart1.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016G/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart2.txt
ls /scratch/data/tZqSkimsRun2016/mumuRun2016H/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/mumuRun2016FilesPart2.txt

ls /scratch/data/tZqSkimsRun2016/metRun2016B_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016C_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016D_rereco/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016E/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016F/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016G/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt
ls /scratch/data/tZqSkimsRun2016/metRun2016H/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/metRun2016Files.txt

ls /scratch/data/tZqSkimsRun2016/DYJetsToLL_M-10to50_amcatnlo/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/DYJets10To50Files.txt
ls /scratch/data/tZqSkimsRun2016/DYJetsToLL_M-10to50_madgraph/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/DYJets10To50MadgraphFiles.txt
ls /scratch/data/tZqSkimsRun2016/DYJetsToLL_M-50_amcatnlo/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/DYJets50Files.txt
ls /scratch/data/tZqSkimsRun2016/DYJetsToLL_M-50_madgraph/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/DYJets50MadgraphFiles.txt
ls /scratch/data/tZqSkimsRun2016/sChannel_4f/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/sChannelFiles.txt
ls /scratch/data/tZqSkimsRun2016/tbarChannel_4f/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tbarChannelFiles.txt
ls /scratch/data/tZqSkimsRun2016/tW_antitop_5f/* -1d  >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tbarWInclusiveFiles.txt
ls /scratch/data/tZqSkimsRun2016/tWZ_5f/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tWZ_ll_Files.txt
ls /scratch/data/tZqSkimsRun2016/tChannel_4f/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tChannelFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttbarDilepton/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttbarDileptonFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttbarInclusive_powerheg/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttbarInclusivePowerhegFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttWlnu/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttWlnuFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttW2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttW2qFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttZ2l2nu/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttZ2l2nuFiles.txt
ls /scratch/data/tZqSkimsRun2016/ttZ2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ttZ2qFiles.txt
ls /scratch/data/tZqSkimsRun2016/tW_top_5f/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tWInclusiveFiles.txt
ls /scratch/data/tZqSkimsRun2016/tZq_ll_4Flavour3Lepton/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZqFiles.txt
ls /scratch/data/tZqSkimsRun2016/tHq/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tHqFiles.txt
ls /scratch/data/tZqSkimsRun2016/wPlusJets/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/wPlusJetsFiles.txt
ls /scratch/data/tZqSkimsRun2016/WW1l1nu2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/WW1l1nu2qFiles.txt
ls /scratch/data/tZqSkimsRun2016/WW2l2nu/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/WW2l2nuFiles.txt
ls /scratch/data/tZqSkimsRun2016/WZ1l1nu2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/WZ1l1nu2q.txt
ls /scratch/data/tZqSkimsRun2016/WZ2l2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/WZ2l2q.txt
ls /scratch/data/tZqSkimsRun2016/WZJets/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/WZjets.txt
ls /scratch/data/tZqSkimsRun2016/ZZ2l2nu/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ZZ2l2nuFiles.txt
ls /scratch/data/tZqSkimsRun2016/ZZ2l2q/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ZZ2l2qFiles.txt
ls /scratch/data/tZqSkimsRun2016/ZZ4l/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/ZZ4lFiles.txt

# FCNC Datasets

ls /scratch/data/tZqSkimsRun2016/tZq_lll_Kappa_Zct/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_lll_Kappa_Zct.txt
ls /scratch/data/tZqSkimsRun2016/tZq_lll_Kappa_Zut/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_lll_Kappa_Zut.txt
ls /scratch/data/tZqSkimsRun2016/tZq_lll_Zeta_Zct/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_lll_Zeta_Zct.txt

ls /scratch/data/tZqSkimsRun2016/tZq_ll_Kappa_Zct/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_ll_Kappa_Zct.txt
ls /scratch/data/tZqSkimsRun2016/tZq_ll_Kappa_Zut/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_ll_Kappa_Zut.txt
ls /scratch/data/tZqSkimsRun2016/tZq_ll_Zeta_Zct/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_ll_Zeta_Zct.txt
ls /scratch/data/tZqSkimsRun2016/tZq_ll_Zeta_Zut/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZq_ll_Zeta_Zut.txt

# Synchronisation files
ls /scratch/data/tZqSkimsRun2016/synch/tZq/* -1d >> $TQZ_TOOLS_PATH/configs/2016/datasets/fileLists/tZqSynchFiles.txt

echo Done!
echo Filelists have been updated.
